from flask import Flask, render_template, request, json, abort, Response
import typographer

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/api/process", methods=["POST"])
def process_by_typographer():
    text = request.get_json().get("text")
    if not text:
        abort(
            Response(
                status="400",
                mimetype="application/json",
                response=json.dumps({"message": "Text is empty"}),
            )
        )
    processed_text = typographer.process(text)
    return json.jsonify(text=processed_text)


if __name__ == "__main__":
    app.run()
