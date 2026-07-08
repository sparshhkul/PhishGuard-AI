from flask import Flask, render_template, request
from utils.predictor import predict_email

app = Flask(__name__)

# ==========================
# HOME
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# SCANNER PAGE
# ==========================
@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


# ==========================
# EMAIL PAGE
# ==========================
@app.route("/email")
def email():
    return render_template("email.html")


# ==========================
# URL PAGE
# ==========================
@app.route("/url")
def url():
    return render_template("url.html")


# ==========================
# SMS PAGE
# ==========================
@app.route("/sms")
def sms():
    return render_template("sms.html")


# ==========================
# EMAIL AI
# ==========================
@app.route("/predict-email", methods=["POST"])
def predict_email_route():

    email_text = request.form["email"]

    result = predict_email(email_text)

    return render_template(
        "result.html",
        prediction=result["label"],
        risk=result["risk"],
        color=result["color"]
    )


# ==========================
# URL DEMO RESULT
# ==========================
@app.route("/result-demo-url")
def result_demo_url():

    return render_template(
        "result.html",
        prediction="Suspicious URL",
        risk=89,
        color="red"
    )


# ==========================
# SMS DEMO RESULT
# ==========================
@app.route("/result-demo-sms")
def result_demo_sms():

    return render_template(
        "result.html",
        prediction="Scam SMS",
        risk=94,
        color="red"
    )


# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)