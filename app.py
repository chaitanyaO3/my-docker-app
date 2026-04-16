from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 🟢 HOME PAGE
@app.route("/", methods=["GET", "POST"])
def home():
    name = ""

    if request.method == "POST":
        user = request.form.get("username")
        name = f"Hello {user} 👋"

    return render_template("index.html", name=name)

# 🟢 ABOUT PAGE
@app.route("/about")
def about():
    return render_template("about.html")

# 🟢 CONTACT PAGE
@app.route("/contact")
def contact():
    return render_template("contact.html")

# 🟢 RUN APP
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
