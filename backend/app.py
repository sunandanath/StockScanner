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

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        process_file(filepath)
        return jsonify({
            'message': 'File successfully processed',
            'csv_file': '/api/results/stock_ranking.csv',
            'html_file': '/api/results/stock_ranking.html.html'
        })
    except Exception as e:
        return jsonify({'message': f'Error processing file: {e}'}), 500

@app.route('/api/results/<filename>', methods=['GET'])
@app.route('/api/results/<filename>', methods=['GET'])
def get_results(filename):
    try:
        if filename not in ['stock_ranking.csv', 'stock_ranking.html']:
            raise FileNotFoundError('File not found')

        return send_from_directory(RESULTS_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({'message': f'Error retrieving file: {e}'}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)




# from flask import Flask, request, send_file, make_response
# from flask_cors import CORS
# import io

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def index():
#     return "Welcome to the Flask API. Use /api/data or /api/upload for specific operations."

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = {
#         'message': 'Hello from Flask!',
#         'status': 'success'
#     }
#     return jsonify(data)

# @app.route('/api/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'message': 'No file part', 'status': 'error'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'message': 'No selected file', 'status': 'error'}), 400
#     if file:
#         # Process the file here
#         content = file.read().decode('utf-8')  # Assuming the file is a text file
#         # Here you can add your processing logic
#         processed_content = content.upper()  # Example processing

#         # Generate HTML content
#         html_content = f"""
#         <html>
#         <head><title>Processed Data</title></head>
#         <body>
#             <h1>Processed Data</h1>
#             <pre>{processed_content}</pre>
#         </body>
#         </html>
#         """

#         # Create a file-like object to send as an HTML file
#         output = io.BytesIO()
#         output.write(html_content.encode('utf-8'))
#         output.seek(0)

#         return send_file(output, as_attachment=True, download_name='processed_data.html', mimetype='text/html')
#     return jsonify({'message': 'File upload failed', 'status': 'error'}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)



""" from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from process_file import process_file

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

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

@app.route('/api/results', methods=['GET'])
def get_results():
    try:
        return send_from_directory(RESULTS_FOLDER, 'stock_ranking.csv')
    except Exception as e:
        return jsonify({'message': f'Error retrieving results: {e}'}), 500

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
 """