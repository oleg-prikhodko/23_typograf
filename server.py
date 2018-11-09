from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/api/process", methods=["POST"])
def process_by_typographer():
    # text = request.form["text"]
    # print("Received:", text)
    print("Data:", request.get_json().get("text"))
    return "OK"


if __name__ == "__main__":
    app.run()
