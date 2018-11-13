from flask import Flask, render_template, request, json, abort, Response
import typographer

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/api/process", methods=["POST"])
def process_by_typographer():
    if request.content_type != "application/json":
        abort(
            Response(
                status="400",
                mimetype="application/json",
                response=json.dumps({"message": "Not a JSON"}),
            )
        )
    elif "text" not in request.get_json():
        abort(
            Response(
                status="400",
                mimetype="application/json",
                response=json.dumps({"message": "No text field"}),
            )
        )
    text = request.get_json().get("text")
    processed_text = typographer.process(text) if text else ""
    return json.jsonify(text=processed_text)


if __name__ == "__main__":
    app.run()
