from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = "admin-secret-key"

BACKEND_URL = "http://127.0.0.1:5001"

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["admin"] = True
            return redirect(url_for("backend"))
        return "Invalid credentials"

    return render_template("login.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

# ---------- REGISTER ----------
@app.route("/")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    student = {
        "name": request.form["name"],
        "age": request.form["age"],
        "qualification": request.form["qualification"],
        "graduation_year": request.form["graduation_year"],
        "address": request.form["address"],
        "email": request.form["email"]
    }

    try:
        response = requests.post(f"{BACKEND_URL}/students", json=student, timeout=3)
        result = response.json()
        message = result.get("message", "Unknown response")

    except Exception:
        message = "Backend service is not reachable"

    return render_template("register.html", message=message)

# ---------- BACKEND (PROTECTED) ----------
@app.route("/backend")
def backend():
    if not session.get("admin"):
        return redirect(url_for("login"))

    students = requests.get(f"{BACKEND_URL}/students").json()
    return render_template("backend.html", students=students)

if __name__ == "__main__":
    app.run(port=5000, debug=False)
