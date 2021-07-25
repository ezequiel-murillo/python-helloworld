from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Main request succesful")
    return "Hello Docker!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
    app.run(host='0.0.0.0', port=8080)
