import os
import sys

from flask import Flask, request, redirect, send_from_directory, render_template
from flask_cors import CORS, cross_origin

from live.src.main import filter_trigger

os.chdir(sys.path[0])



# Initializing the Flask app
app = Flask(__name__)
# Setting up Flask application from config.py
app.config.from_object("config.ProductionConfig")
# Enabling `cross origin` for app
CORS(app=app, support_credentials=True)


# Setting upload route
@app.route('/upload', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def upload_file():
    """
    Upload file to static directory
    """
    if request.files:
        excel = request.files['excel']
        print('excel = ', excel)

        excel.save(os.path.join(app.config["STATIC_FILE_DIRECTORY"], excel.filename))
        print('excel saved..')
        if excel.filename == "":
            print("No filename")
        filter_trigger(filename=excel.filename)
        return redirect(request.url)
    return render_template('index.html')


# Setting residue download route
@app.route('/download_residue', methods=['GET'])
@cross_origin(support_credentials=True)
def download_resultant_file():
    """
    Download resultant file from output directory
    """
    return send_from_directory(app.config["OUTPUT_DIRECTORY"], "compiled_sheets.xls")


# Setting brs download route
@app.route('/download_brs', methods=['GET'])
@cross_origin(support_credentials=True)
def download_brs_file():
    """
    Download BRS Report from output directory
    """
    return send_from_directory(app.config["OUTPUT_DIRECTORY"], "brs.xls")


@app.route('/get_chord', methods=['GET'])
@cross_origin(support_credentials=True)
def get_chord_stats():
    """
    Get Statistical Data in Chord Diagrams
    """
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)
