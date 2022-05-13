from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory
from marshmallow import Schema, fields
from football import *

app = Flask(__name__, template_folder='templates')
football = Football()
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
    return 'do some magic!'


def delete_player(name):  # noqa: E501
    """Delete player&#x27;s Data

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: None
    """
    return 'do some magic!'





def get_player_by_name(name):  # noqa: E501
    """Get Player by name

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: Player
    """
    return 'do some magic!'


def player_post(body):  # noqa: E501
    """Add Player to DB

     # noqa: E501

    :param body: Add player to the players DataBase
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Player.from_dict(connexion.request.get_data())  # noqa: E501
    return 'do some magic!'

def get_teams():  # noqa: E501
    """Get Teams

    Get teams for Monday Football # noqa: E501


    :rtype: List[Team]
    """
    return 'do some magic!'

if __name__ == '__main__':
    app.run(debug=True)