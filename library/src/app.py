import json

from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
import pathlib
import os
from src.utils.helper import  Helper
from src.utils.read_write_utils import read_data_excel, read_data_csv
from werkzeug.utils import secure_filename
from src.assets.questions import questions

app = Flask(__name__)
CORS(app)

ROOT = str(pathlib.Path().absolute())
uploads_dir = os.path.join('uploads')
os.makedirs(uploads_dir, exist_ok=True)
helper = Helper()

@app.route('/', methods=['POST'])
def uploaded_file():
    if request.method == 'POST':
        helper_data = json.loads(request.form['helper_data'])
        print(helper_data["question_id"])
        input_file_if_exist = request.files['file']
        if input_file_if_exist:
            filename = input_file_if_exist.filename
            input_file_if_exist.save(secure_filename(input_file_if_exist.filename))

            data = read_data_excel(f'{filename}')
            helper.helper(data, helper_data)
        return jsonify(helper_data)

    if __name__ == '__main__':
        app.run(port='5000', host='0.0.0.0')

@app.route('/get_questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

if __name__ == '__main__':
    app.run()
