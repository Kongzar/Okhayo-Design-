from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.secret_key = "okhayo-design-secret-key-change-in-production"
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

@app.route("/journal/<int:id>")
def article(id):
    articles = db.execute("SELECT * FROM articles WHERE id = ? AND published = 1", id)
    if len(articles) == 0:
        return render_template("404.html"), 404
    return render_template("article.html", article=articles[0])

from functools import wraps
from flask import flash

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("user_id"):
            return redirect("/login")
        # Check if user is admin
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        if len(user) == 0 or user[0]["is_admin"] != 1:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated

@app.route("/admin")
@admin_required
def admin_dashboard():
    articles = db.execute("SELECT * FROM articles ORDER BY created_at DESC")
    return render_template("admin/dashboard.html", articles=articles)

@app.route("/admin/new", methods=["GET", "POST"])
@admin_required
def admin_new():
    if request.method == "POST":
        title = request.form.get("title")
        category = request.form.get("category")
        excerpt = request.form.get("excerpt")
        body = request.form.get("body")
        author = request.form.get("author", "Okhayo Design")
        image_url = request.form.get("image_url", "")
        published = 1 if request.form.get("published") else 0

        if not title or not category or not body:
            flash("Title, category and body are required", "error")
            return render_template("admin/editor.html")

        db.execute("""
            INSERT INTO articles (title, category, excerpt, body, author, image_url, published)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, title, category, excerpt, body, author, image_url, published)

        flash("Article published successfully", "success")
        return redirect("/admin")

    return render_template("admin/editor.html", article=None)

@app.route("/admin/edit/<int:id>", methods=["GET", "POST"])
@admin_required
def admin_edit(id):
    article = db.execute("SELECT * FROM articles WHERE id = ?", id)
    if len(article) == 0:
        return redirect("/admin")

    if request.method == "POST":
        title = request.form.get("title")
        category = request.form.get("category")
        excerpt = request.form.get("excerpt")
        body = request.form.get("body")
        author = request.form.get("author", "Okhayo Design")
        image_url = request.form.get("image_url", "")
        published = 1 if request.form.get("published") else 0

        db.execute("""
            UPDATE articles
            SET title=?, category=?, excerpt=?, body=?, author=?, image_url=?, published=?
            WHERE id=?
        """, title, category, excerpt, body, author, image_url, published, id)

        flash("Article updated", "success")
        return redirect("/admin")

    return render_template("admin/editor.html", article=article[0])

@app.route("/admin/delete/<int:id>", methods=["POST"])
@admin_required
def admin_delete(id):
    db.execute("DELETE FROM articles WHERE id = ?", id)
    flash("Article deleted", "success")
    return redirect("/admin")


@app.route("/profile")
def profile():
    if not session.get("user_id"):
        return redirect("/login")
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    favourites = db.execute("""
        SELECT objects.* FROM objects
        JOIN favourites ON objects.id = favourites.object_id
        WHERE favourites.user_id = ?
        ORDER BY favourites.saved_at DESC
    """, session["user_id"])
    return render_template("profile.html", user=user[0], favourites=favourites)

@app.route("/favourite/<int:object_id>", methods=["POST"])
def toggle_favourite(object_id):
    if not session.get("user_id"):
        return redirect("/login")
    existing = db.execute("""
        SELECT * FROM favourites
        WHERE user_id = ? AND object_id = ?
    """, session["user_id"], object_id)
    if existing:
        db.execute("""
            DELETE FROM favourites
            WHERE user_id = ? AND object_id = ?
        """, session["user_id"], object_id)
        flash("Removed from favourites", "success")
    else:
        db.execute("""
            INSERT INTO favourites (user_id, object_id)
            VALUES (?, ?)
        """, session["user_id"], object_id)
        flash("Saved to favourites", "success")
    return redirect(request.referrer or "/")