from flask import Flask, render_template, abort, redirect
app = Flask(__name__)	

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def posts():
    return render_template("posts.html")


@app.route('/social-media')
def socialmedia():
    return render_template("social-media2.html")

@app.route('/notfound')
def notfound():
    return render_template("notfound.html")


@app.route('/contact')
def contact():
    return render_template("contact1.html")

@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0",5000,debug=True)
