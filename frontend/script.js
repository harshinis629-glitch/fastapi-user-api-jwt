const API_URL="http://127.0.0.1:8000";

// =============================
// REGISTER
// =============================

const registerForm = document.getElementById("registerForm");
const registerMessage = document.getElementById("registerMessage");

registerForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const userData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        age: Number(document.getElementById("age").value),
        password: document.getElementById("password").value
    };

    try {

        const response = await fetch("/register", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(userData)
        });

        const data = await response.json();

        if (response.ok) {

            registerMessage.textContent =
                "Registration successful!";

            registerForm.reset();

        } else {

            registerMessage.textContent =
                data.detail;

        }

    } catch (error) {

        registerMessage.textContent =
            "Unable to connect to server.";

        console.error(error);
    }
});


// =============================
// LOGIN
// =============================

const loginForm = document.getElementById("loginForm");
const loginMessage = document.getElementById("loginMessage");

loginForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const loginData = {
        email: document.getElementById("loginEmail").value,
        password: document.getElementById("loginPassword").value
    };

    try {

        const response = await fetch("/login", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(loginData)
        });

        const data = await response.json();

        if (response.ok) {

            // Save JWT token in browser
            localStorage.setItem(
                "access_token",
                data.access_token
            );

            loginMessage.textContent =
                "Login successful!";

            loginForm.reset();

            console.log("JWT Token:", data.access_token);

        } else {

            loginMessage.textContent =
                data.detail;

        }

    } catch (error) {

        loginMessage.textContent =
            "Unable to connect to server.";

        console.error(error);
    }
});
// =============================
// VIEW PROFILE
// =============================

const profileButton = document.getElementById("profileButton");
const profileMessage = document.getElementById("profileMessage");

profileButton.addEventListener("click", async function () {

    // Get the JWT saved during login
    const token = localStorage.getItem("access_token");

    if (!token) {
        profileMessage.textContent = "Please log in first.";
        return;
    }

    try {
        const response = await fetch("/profile", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        const data = await response.json();

        if (response.ok) {
            profileMessage.textContent =
                `User ID: ${data.user_id} | Role: ${data.role}`;
        } else {
            profileMessage.textContent =
                data.detail || "Unable to load profile.";
        }

    } catch (error) {
        profileMessage.textContent = "Unable to connect to server.";
        console.error(error);
    }
});