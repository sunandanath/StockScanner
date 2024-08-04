from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import os
from process_file import process_file
from auth import auth, bcrypt, jwt

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')

# Initialize extensions
bcrypt.init_app(app)
jwt.init_app(app)

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')

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
@jwt_required()
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
@jwt_required()
def get_results(filename):
    try:
        if filename not in ['stock_ranking.csv', 'stock_ranking.html']:
             raise FileNotFoundError('File not found')
        return send_from_directory(RESULTS_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({'message': f'Error retrieving results: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)



# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required
# import os
# from process_file import process_file
# import datetime

# app = Flask(__name__)
# CORS(app)
# bcrypt = Bcrypt(app)
# app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# jwt = JWTManager(app)

# UPLOAD_FOLDER = 'uploads'
# RESULTS_FOLDER = 'results'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(RESULTS_FOLDER, exist_ok=True)

# users = {}

# @app.route('/')
# def index():
#     return jsonify({
#         'message': 'Flask API is running',
#         'info': 'Welcome to the Flask API. Use /api/data or /api/upload for specific operations.'
#     }), 200

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     if username in users:
#         return jsonify({'message': 'User already exists'}), 400
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     users[username] = hashed_password
#     return jsonify({'message': 'User registered successfully'}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     if username not in users or not bcrypt.check_password_hash(users[username], password):
#         return jsonify({'message': 'Invalid credentials'}), 401
#     access_token = create_access_token(identity=username)
#     return jsonify({'access_token': access_token}), 200

# @app.route('/api/upload', methods=['POST'])
# @jwt_required()
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'message': 'No file part'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'message': 'No selected file'}), 400

#     ma_period1 = int(request.form.get('ma_period1', 10))
#     ma_period2 = int(request.form.get('ma_period2', 20))

#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)

#     try:
#         csv_filename, html_filename = process_file(filepath, ma_period1, ma_period2)
#         return jsonify({
#             'message': 'File Successfully Processed',
#             'csv_file': f'/api/results/{csv_filename}',
#             'html_file': f'/api/results/{html_filename}'
#         })
#     except Exception as e:
#         return jsonify({'message': f'Error processing file: {e}'}), 500

# @app.route('/api/results/<filename>', methods=['GET'])
# @jwt_required()
# def get_results(filename):
#     try:
#         return send_from_directory(RESULTS_FOLDER, filename, as_attachment=True)
#     except Exception as e:
#         return jsonify({'message': f'Error retrieving results: {e}'}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
