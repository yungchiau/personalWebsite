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


@app.route("/profile")
def get_profile():
    # fetch json file in cloud storage?
    return 1

@app.route('/history')
def get_history():
    # get the history of this infomation
    pass

@app.route("/download")
def download():
    # download my resume(pdf)
    pass