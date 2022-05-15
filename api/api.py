import time
import os
from flask import Flask
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

FLASK_APP = os.getenv("FLASK_APP")


@app.route("/time")
def get_current_time():
    return {'time': time.time()}
