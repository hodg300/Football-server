from flask import Flask, jsonify, render_template, send_from_directory,request
from flask_cors import CORS
from football import FootballManager
import json
import os

app = Flask(__name__, template_folder='templates')
CORS(app)
football = FootballManager()

@app.route('/')
def home():
    print("READY!")
    return "Ready to shuffle!"

def create_response(messege: str) -> json:
    respone = {}
    respone['message'] = messege
    return json.loads(json.dumps(respone))

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
    print("get_all_players CALLED")

    if (request.method == 'GET'):
        return jsonify(football.get_all_players()), 200

@app.route('/players/<string:name>',methods = ['DELETE'])
def delete_player(name):  # noqa: E501
    """Delete player&#x27;s Data

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: None
    """
    print("delete_player CALLED")

    if football.delete_player(name):
        return jsonify(create_response("Player deleted successfully")), 204
    return jsonify(create_response("Cannot find player")), 400

@app.route('/players/<string:name>',methods = ['GET'])
def get_player_by_name(name):  # noqa: E501
    """Get Player by name

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: Player
    """
    print("get_player_by_name CALLED")
    jsonData = football.get_player_by_name(name)
    if jsonData != {}:
        return jsonify(football.get_player_by_name(name)), 200
    return jsonify(create_response("Cannot find player")), 400

@app.route('/player',methods = ['POST'])
def add_player():
    """Add Player to DB

     # noqa: E501

    :param body: Add player to the players DataBase
    :type body: dict | bytes

    :rtype: None
    """
    print("add_player CALLED")

    if request.data:
        body = request.get_data()  # noqa: E501
        if football.add_player(body):
            return jsonify(create_response("Player Added successfully")), 201
    return jsonify(create_response("Cannot add player, wrong input")), 400

@app.route('/Teams',methods = ['POST'])
def get_teams():
    """Get Teams

    Get teams for Monday Football # noqa: E501

    :rtype: List[Team]
    """
    print("get_teams CALLED")
    if request.data:
        body = request.get_data()  # noqa: E501
        data = football.get_teams(body)
        if len(data) != 0:
            return jsonify(data), 201
    return jsonify(create_response("Cannot create teams, please check the data")), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
