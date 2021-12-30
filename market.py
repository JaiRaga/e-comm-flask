from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "<h2>Pattu Pappa</h2>"

@app.route("/about/<username>")
def about_page(username):
  return f"<h1>Made by {username}</h1>"