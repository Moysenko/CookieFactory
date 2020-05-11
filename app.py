from flask import Flask, render_template, send_file, request, send_from_directory
from werkzeug.utils import secure_filename
import logging
import os
import factory


app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')


@app.route('/', methods=['GET'])
def get():
    print('hehe')
    return render_template('index.html')


@app.route('/upload_save_file', methods=['GET', 'POST'])
def upload_save_file():
    time = request.form['time']
    file = request.files['userSave']
    file.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_saves', file.filename))
    factory.mine(time, file.filename)
    return send_from_directory(os.path.join(app.root_path, 'output_saves'), 'save.txt')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
