import os
#The Capital f indicates that is a class
#Instead of writing HTML tags inside the python file we can use render_template
from flask import Flask, render_template

#Create instance of this class
app = Flask(__name__);

#Telling flask what URL trigger the function
#a decorator start with @ which is also called pie notation
#a decorator is a way of wrapping functions
@app.route("/")
def index():
    #return "<h1>Hello,</h1> <h2> World</h2>"
    #flask will looking for temoplates folder to find html file we refrenssed in pranteces
    return render_template("index.html")

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug = True
    )