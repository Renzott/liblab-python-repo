from flask import Flask, request,jsonify
from flask_cors import CORS,cross_origin
from data import sbs,sentinel
import json

app = Flask(__name__)
cors = CORS(app)

app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return  '''<h1>API de Sentinel y Superintendecia de Banca y Seguros</h1>
<p>Esta es una API Ficticia solo con fines de exposion.</p>
<p>Los datos mostrados en esta api son datos estaticos y no modificables</p>

<p>Rutas:</p>

<code>GET api/sentinel/{dni|ruc} </code>
</br>
<code>GET api/sbs/{dni|ruc} </code>

'''

@app.route('/api/sentinel/<int:dni>', methods=['GET'])
@cross_origin()
def api_sentinel(dni):
    for item in sentinel:
        if int(item['dni']) == dni:
            return jsonify(item)

    return jsonify([0,"No hay Data"])  
    

@app.route('/api/sbs/<int:dni>', methods=['GET'])
@cross_origin()
def api_sbs(dni):
    for item in sbs:
        if int(item['dni']) == dni:
            return jsonify(item)

    return jsonify([0,"No hay Data"])  

if __name__ == '__main__':
    app.run(port='5000')