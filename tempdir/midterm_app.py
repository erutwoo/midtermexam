from flask import Flask,render_template,request,redirect,url_for,session
import re

app = Flask(__name__)
@app.route('/')
@app.route("/login",methods=['POST'])
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("registration.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)