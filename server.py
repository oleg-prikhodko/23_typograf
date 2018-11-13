from flask import Flask, render_template, request, json, abort, Response
import typographer

app = Flask(__name__)

BAD_REQUEST_STATUS_CODE = 400
JSON_CONTENT_TYPE = "application/json"


class ErrorResponse(Response):
    def __init__(self, message):
        super().__init__(
            status=BAD_REQUEST_STATUS_CODE,
            mimetype=JSON_CONTENT_TYPE,
            response=json.dumps({"message": message}),
        )


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/api/process", methods=["POST"])
def process_by_typographer():
    if request.content_type != JSON_CONTENT_TYPE:
        abort(ErrorResponse("Not a JSON"))
    elif "text" not in request.get_json():
        abort(ErrorResponse("No text field"))

    text = request.get_json().get("text")
    processed_text = typographer.process(text) if text else ""
    return json.jsonify(text=processed_text)


if __name__ == "__main__":
    app.run()
