from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure database
db = SQL("sqlite:///okhayo.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/journal")
def journal():
    articles = db.execute("SELECT * FROM articles WHERE published = 1 ORDER BY created_at DESC")
    return render_template("journal.html", articles=articles)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        if len(rows) != 1:
            return render_template("login.html", error="User not found")
        from werkzeug.security import check_password_hash
        if not check_password_hash(rows[0]["password_hash"], password):
            return render_template("login.html", error="Wrong password")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        from werkzeug.security import generate_password_hash
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        if not username or not email or not password:
            return render_template("register.html", error="All fields required")
        hash = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                      username, email, hash)
        except:
            return render_template("register.html", error="Email already exists")
        return redirect("/login")
    return render_template("register.html")