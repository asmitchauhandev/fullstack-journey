# =====================================
# DAY 14: FLASK BASIC WEB APP
# =====================================

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My First Flask App 🚀"

@app.route("/about")
def about():
    return "This is Day 14 of my Full Stack Journey 😎"

@app.route("/contact")
def contact():
    return "Contact: asmitchauhan66@gmail.com"

if __name__ == "__main__":
    app.run(debug=True)