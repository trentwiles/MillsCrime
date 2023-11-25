from flask import Flask, Response
import json
import citizen
import opd

app = Flask(__name__)

@app.route('/')
def index():
    return Response(json.dumps({"message": "OK"}), content_type="application/json")

@app.route('/api/v1/all/<int:hrs>')
def all(hrs):
    return Response(json.dumps({"message": "OK", "citizen": citizen.getReports(hrs), "oaklandPolice": opd.getOpenData(hrs)}), content_type="application/json")


if __name__ == '__main__':
    app.run(debug=True)
