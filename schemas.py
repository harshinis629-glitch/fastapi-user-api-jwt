from pydantic import BaseModel, EmailStr


# Data required during registration
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str


# Data required during login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Data returned to the client
class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    role: str

    class Config:
        from_attributes = True


# JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str