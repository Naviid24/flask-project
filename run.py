import os
# The capital F indicates that this is a class.
# Instead of writing HTML tags inside the Python file, we can use render_template.
from flask import Flask, render_template

# Create an instance of the Flask class.
app = Flask(__name__)

# Telling Flask which URL triggers the function.
# A decorator starts with @, which is also called pie notation.
# A decorator is a way of wrapping functions.
@app.route("/")
def index():
    # Flask will look for the 'templates' folder to find the HTML file we referenced in parentheses.
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# Ensure there are two blank lines between functions for PEP8 compliance.
if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
