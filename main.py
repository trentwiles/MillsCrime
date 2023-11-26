from flask import Flask, Response, render_template
import json
import citizen
import opd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", hours = 6)

@app.route('/<time>')
def hours(time):
    return render_template("index.html", hours=time)


@app.route('/api/v1/all/<int:hrs>')
def all(hrs):
    return Response(json.dumps({"message": "OK", "citizen": citizen.getReports(hrs), "oaklandPolice": opd.getOpenData(hrs)}), content_type="application/json")


if __name__ == '__main__':
    app.run(debug=True)
