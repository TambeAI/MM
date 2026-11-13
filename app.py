
from flask import Flask, Response, abort
from pathlib import Path

app = Flask(__name__)

@app.route("/t/<int:practical_id>")
def show_practical(practical_id):

    file_path = Path(__file__).parent / f"{practical_id}.txt"

    if not file_path.is_file():
        abort(404)

    code = file_path.read_text(encoding="utf-8")

    return Response(code, content_type="text/plain; charset=utf-8")

if __name__ == "__main__":
    app.run()
