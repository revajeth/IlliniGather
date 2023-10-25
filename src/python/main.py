from flask import Flask, render_template, request, session
import os
import auth

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


@app.route('/verify/', methods=['POST', 'GET'])
def verify():
    if request.method == 'GET':
        return "Invalid Request"
    net_id = (request.form['netid']).strip()
    session["netid"] = net_id
    if (auth.verified(net_id+"@illinois.edu")):
        return render_template("homepage.html")
    else:
        auth.expireCode(net_id+"@illinois.edu")
        if (auth.sendVerification(net_id+"@illinois.edu")):
            return render_template("code.html")
        else:
            return "Failure to verify netid"


@app.route('/home/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return "Invalid Request"
    ver_code = (request.form['otp']).strip()
    if (auth.verify(session.get("netid", None) + "@illinois.edu", ver_code)):
        auth.expireCode(session.get("netid", None) + "@illinois.edu")
        auth.addToVerified(session.get("netid", None) + "@illinois.edu")
        return render_template("homepage.html")
    else:
        auth.expireCode(session.get("netid", None) + "@illinois.edu")
        return render_template("login.html")


if __name__ == '__main__':
    app.secret_key = 'dfgdfsfdgfds'
    app.run(debug=True)
