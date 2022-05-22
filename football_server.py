from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory,request
from marshmallow import Schema, fields
from football import FootballManager
import json

app = Flask(__name__, template_folder='templates')
football = FootballManager()
spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)


@app.route('/')
def home():
    return "Ready to shuffle!"

#################### SWAGGER ##########################
@app.route('/api')
@app.route('/api/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/api')
    else:
        return send_from_directory('./static', path)

################### API ###########################

@app.route('/players',methods = ['GET'])
def get_all_players():  # noqa: E501
    """Get all players
     # noqa: E501
    :rtype: List[InlineResponse200]
    """
    if (request.method == 'GET'):
        return jsonify(football.get_all_players())

@app.route('/players/<string:name>',methods = ['DELETE'])
def delete_player(name):  # noqa: E501
    """Delete player&#x27;s Data

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: None
    """
    if football.delete_player(name):
        return "success", 204
    return "user not found", 400

@app.route('/players/<string:name>',methods = ['GET'])
def get_player_by_name(name):  # noqa: E501
    """Get Player by name

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: Player
    """
    return football.get_player_by_name(name)

@app.route('/player',methods = ['POST'])
def add_player():
    """Add Player to DB

     # noqa: E501

    :param body: Add player to the players DataBase
    :type body: dict | bytes

    :rtype: None
    """
    if request.data:
        body = request.get_data()  # noqa: E501
        football.add_player(body)
    return "success", 201

@app.route('/Teams',methods = ['POST'])
def get_teams():
    """Get Teams

    Get teams for Monday Football # noqa: E501

    :rtype: List[Team]
    """
    if request.data:
        body = request.get_data()  # noqa: E501
        data = football.get_teams(body)
        return jsonify(data), 201
    return "no data", 400

if __name__ == '__main__':
    app.run(debug=True)