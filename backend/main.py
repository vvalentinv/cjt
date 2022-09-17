from dotenv import dotenv_values
from flask import Flask
from controller.user_controller import uc
from controller.auth_controller import ac
from controller.tour_controller import tc
from flask_cors import CORS
from flask_session import Session


config = dotenv_values(".env")

if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = config['secret_key']
    app.config['SESSION_TYPE'] = 'filesystem'

    CORS(app, origins=['http://ec2-35-165-134-192.us-west-2.compute.amazonaws.com', 'http://127.0.0.1:5500'],
         supports_credentials=True)

    Session(app)

    app.register_blueprint(uc)
    app.register_blueprint(ac)
    app.register_blueprint(tc)
    app.run(host="0.0.0.0", port=8080, debug=True)


