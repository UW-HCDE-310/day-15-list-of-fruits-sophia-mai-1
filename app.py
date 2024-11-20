from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    requirements_met = []
    for fruit in fruits:
        if fruit["name"].startswith("o") and fruit["quantity"] >= 3:
            requirements_met.append(fruit)

    return render_template("index.html", fruits=requirements_met)
