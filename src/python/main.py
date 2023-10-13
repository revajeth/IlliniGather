from flask import Flask, render_template
import os


temp = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.dirname(os.path.dirname(temp))
template_dir = os.path.join(template_dir, 'src')
template_dir = os.path.join(template_dir, 'pages')
template_dir = os.path.join(template_dir, 'templates')
static_dir = os.path.dirname(os.path.dirname(temp))
static_dir = os.path.join(static_dir, 'src')
static_dir = os.path.join(static_dir, 'pages')
static_dir = os.path.join(static_dir, 'static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@app.route('/')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()
