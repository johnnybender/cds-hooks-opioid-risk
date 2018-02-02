from flask import json
from flask import Flask
from flask import jsonify
from flask import Response
from flask_cors import CORS
from flask import request
from flask import send_file

app = Flask(__name__)
CORS(app)

@app.route('/cds-services', methods = ['GET'])
def api_cds_services():
    data = {
        "services": [
        {
            "hook": "medication-prescribe",
            "title": "Opioid Addiction Risk Stratification Tool",
            "description": "A Clinical Decision Support service that stratifies patients into addiction risk categories based on several indicators",
            "id": "opioid-risk-stratification",
            "prefetch": {
            "patient": "Patient/{{Patient.id}}",
            "medications": "MedicationOrder?patient={{Patient.id}}"
            }
        }
        ]
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://127.0.0.1:5000/cds-services'
    
    return resp

@app.route('/img')
def image():
    filename = './images/IMG.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/cds-services/opioid-risk-stratification', methods = ['POST'])
def api_risk_stratification():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        data = request.json
        formatted = json.dumps(data, sort_keys = True, indent = 4, separators=(',', ': '))
        a = open('data.json', 'w')
        a.write(formatted)
        cards = {
            "cards": [
            {
                "summary": "Opioid Addiction Risk Score",
                "indicator": "warning",
                "detail": "### Result: 84% Risk of addiction",
                "source": {
                "label": "NHS Digital",
                "url": "https://digital.nhs.uk/",
                "icon": "http://127.0.0.1:5000/img"
                },
                "links": [
                    {
                    "label": "Fill in additional data here",
                    "url": "https://digital.nhs.uk/",
                    "type": "absolute"
                    }
                ],
                "suggestions": [
                    {
                    "label": "Consider addiction support programs"
                    }
                ]
                }
            ]
        }
        return "no cards"
        return json.dumps(cards)
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run(debug=True)