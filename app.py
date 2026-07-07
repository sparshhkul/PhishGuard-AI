from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/email")
def email():
    return render_template("email.html")

@app.route("/url")
def url():
    return render_template("url.html")

@app.route("/sms")
def sms():
    return render_template("sms.html")

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )