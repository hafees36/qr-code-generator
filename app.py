from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_generated = False

    if request.method == "POST":
        data = request.form["data"]

        qr = qrcode.make(data)
        qr.save("static/qr.png")

        qr_generated = True

    return render_template("index.html", qr_generated=qr_generated)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

