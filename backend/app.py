from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from process_file import process_file

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        process_file(filepath)
        return jsonify({'message': 'File successfully processed'})
    except Exception as e:
        return jsonify({'message': f'Error processing file: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
