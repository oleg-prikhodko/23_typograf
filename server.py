from flask import Flask, render_template, request
import typographer

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/api/process", methods=["POST"])
def process_by_typographer():
    # text = request.form["text"]
    # print("Received:", text)
    text = request.get_json().get("text")
    # print("Data:", )
    return typographer.process(text)


if __name__ == "__main__":
    app.run()
