import flask
from datetime import datetime
import psutil
import json
import os

class HWSerial(dict):
    def __init__(self, param:str):
        dict.__init__(self, param=param)

app = flask.Flask(__name__)

@app.route('/api/v1/time', methods=['GET'])
def get_time_in_utc():
    return str(datetime.utcnow())

@app.route('/api/v1/status', methods=['GET'])
def get_cpu_uti():
    return f'{psutil.cpu_percent(interval=1)} %'

@app.route('/api/v1/serializer/<param>', methods=['GET'])
def get_serialized_object(param):
    return json.dumps(HWSerial(param))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
