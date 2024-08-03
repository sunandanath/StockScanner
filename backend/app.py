from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from process_file import process_file

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return jsonify({
        'message': 'Flask API is running',
        'info': 'Welcome to the Flask API. Use /api/data or /api/upload for specific operations.'
    }), 200

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    ma_period1 = int(request.form.get('ma_period1', 10))
    ma_period2 = int(request.form.get('ma_period2', 20))

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        csv_filename, html_filename = process_file(filepath, ma_period1, ma_period2)
        return jsonify({
            'message': 'File Successfully Processed',
            'csv_file': f'/api/results/{csv_filename}',
            'html_file': f'/api/results/{html_filename}'
        })
    except Exception as e:
        return jsonify({'message': f'Error processing file: {e}'}), 500

@app.route('/api/results/<filename>', methods=['GET'])
def get_results(filename):
    try:
        if filename not in ['stock_ranking.csv', 'stock_ranking.html']:
             raise FileNotFoundError('File not found')
        return send_from_directory(RESULTS_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({'message': f'Error retrieving results: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(host="0.0.0.0", port=5000, debug=True)

