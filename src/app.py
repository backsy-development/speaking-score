from flask import Flask
from config.config import AppConfig
from controllers.junbro1016 import junbro1016
from controllers.health_check import health_check

app = Flask(__name__)

app.register_blueprint(junbro1016)
app.register_blueprint(health_check)

app.run(None, port=AppConfig.port)