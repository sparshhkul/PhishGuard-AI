from flask import Flask, render_template

app = Flask(__name__)

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# SCANNER SELECTION
# ==========================================

@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


# ==========================================
# EMAIL SCANNER
# ==========================================

@app.route("/email")
def email():
    return render_template("email.html")


# ==========================================
# URL SCANNER
# ==========================================

@app.route("/url")
def url():
    return render_template("url.html")


# ==========================================
# SMS SCANNER
# ==========================================

@app.route("/sms")
def sms():
    return render_template("sms.html")


# ==========================================
# RESULT PAGE
# ==========================================

@app.route("/result")
def result():
    return render_template("result.html")


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )