# -------------------------------
# Import required things from Flask
# -------------------------------
from flask import Flask, request, render_template, redirect, url_for, make_response

# Import JWT utilities from flask_jwt_extended
from flask_jwt_extended import (
    JWTManager,            # Initializes JWT support in Flask
    create_access_token,   # Creates a JWT token after login
    jwt_required,          # Protects routes (only valid JWT can access)
    get_jwt_identity       # Extracts user info from JWT
)

# -------------------------------
# Create Flask application
# -------------------------------
app = Flask(__name__)

# -------------------------------
# JWT CONFIGURATION
# -------------------------------

# Secret key used to SIGN and VERIFY JWT tokens
# If someone changes the token, verification will fail
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Tell Flask-JWT where to find the token
# Here: inside browser cookies
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]

# Cookie security
# False for localhost (HTTP)
# True for production (HTTPS)
app.config["JWT_COOKIE_SECURE"] = False

# CSRF protection disabled for simplicity
# (Enable this in real applications)
app.config["JWT_COOKIE_CSRF_PROTECT"] = False

# Initialize JWT system with Flask app
jwt = JWTManager(app)

# =====================================================
#                  NORMAL PAGES
# =====================================================

# -------------------------------
# Login Page (PUBLIC)
# -------------------------------
@app.route("/")
def login_page():
    # Shows login HTML form
    return render_template("login.html")

# -------------------------------
# Public Page (NO AUTH REQUIRED)
# -------------------------------
@app.route("/public")
def public_page():
    # Anyone can access this page
    return render_template("public.html")

# -------------------------------
# Verified Page (JWT REQUIRED)
# -------------------------------
@app.route("/verified")
@jwt_required()  #  This decorator BLOCKS access without valid JWT
def verified_page():
    # Extract user identity from JWT payload
    user = get_jwt_identity()

    # Render page only if JWT is valid
    return render_template("verified.html", user=user)

# =====================================================
#                  LOGIN LOGIC
# =====================================================

@app.route("/login", methods=["POST"])
def login():
    # Get username and password from HTML form
    username = request.form.get("username")
    password = request.form.get("password")

    # Dummy authentication (replace with DB check in real apps)
    if username == "admin" and password == "secret":

        # Create JWT token
        # identity = data stored inside JWT payload
        token = create_access_token(identity=username)

        # Redirect user to verified page
        response = make_response(redirect(url_for("verified_page")))

        # Store JWT in HTTP-only cookie
        # Browser sends this cookie automatically on every request
        response.set_cookie(
            "access_token_cookie",  # Cookie name expected by flask-jwt-extended
            token,                  # JWT token
            httponly=True           # JS cannot access this cookie (secure)
        )

        return response

    # If login fails
    return "Invalid credentials", 401

# =====================================================
#                  LOGOUT
# =====================================================

@app.route("/logout")
def logout():
    # Create response that redirects to login page
    response = make_response(redirect(url_for("login_page")))

    # Delete JWT cookie (user becomes logged out)
    response.delete_cookie("access_token_cookie")

    return response

# -------------------------------
# Run the Flask app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
