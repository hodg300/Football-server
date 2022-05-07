from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory
from marshmallow import Schema, fields
from Football import *

app = Flask(__name__, template_folder='templates')

spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

football = Football()
football.read_CSV()

@app.route('/')
def home():
    return "Ready to shuffle!"

@app.route('/Static/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())

@app.route('/api')
@app.route('/api/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/api')
    else:
        return send_from_directory('./static', path)

@app.route('/players',methods = ['GET'])
def login():
    return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug=True)