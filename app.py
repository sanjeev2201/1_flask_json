from flask import Flask
from flask_json import FlaskJSON, json_response
from datetime import datetime

app = Flask(__name__)
FlaskJSON(app)


@app.route('/get_time')
def get_time():
    now = datetime.now()
    name = "sanjeev"
    return json_response(time=now, name=name)


if __name__ == '__main__':
    app.run(debug=True)
