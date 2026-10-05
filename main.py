from uuid import uuid4

from fastapi import FastAPI, Depends, HTTPException, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles

from database import SessionLocal
from models import User
from schemas import UserRegister, UserResponse, UserLogin, Token
from auth import hash_password, verify_password, create_access_token, verify_token

security = HTTPBearer()
app = FastAPI(title="JWT Authentication API")


app.mount(
    "/frontend",
    StaticFiles(directory="frontend", html=True),
    name="frontend"
)


# -----------------------------
# DATABASE SESSION
# -----------------------------
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# -----------------------------
# HOME
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "JWT Authentication API is running"
    }


# -----------------------------
# REGISTER
# -----------------------------
@app.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register_user(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):

    # Check whether email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Hash the password
    hashed_password = hash_password(user_data.password)

    # Create new user
    new_user = User(
        id=str(uuid4()),
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        password=hashed_password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# -----------------------------
# LOGIN
# -----------------------------
@app.post("/login", response_model=Token)
def login_user(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    # Find user by email
    user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    # Check whether user exists
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
        user_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Create JWT token
    token = create_access_token(
        {
            "sub": user.id,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
# -----------------------------
# PROTECTED PROFILE
# -----------------------------
@app.get("/profile")
def get_profile(
    authorization: HTTPAuthorizationCredentials = Security(security)
):
    # Get token from Authorization header
    token = authorization.credentials

    # Verify JWT token
    payload = verify_token(token)

    return {
        "message": "You are authenticated",
        "user_id": payload["sub"],
        "role": payload["role"]
    }
# -----------------------------
# ADMIN-ONLY ENDPOINT
# -----------------------------
@app.get("/admin")
def admin_dashboard(
    authorization: HTTPAuthorizationCredentials = Security(security)
):
    # Get token from Authorization header
    token = authorization.credentials

    # Verify JWT token
    payload = verify_token(token)

    # Check user's role
    if payload.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return {
        "message": "Welcome to the admin dashboard!",
        "user_id": payload["sub"],
        "role": payload["role"]
    }