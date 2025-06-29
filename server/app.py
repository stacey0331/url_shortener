from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # todo: best to add origins later
# todo: not store credentials in code
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'
db = SQLAlchemy(app)

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original_url = db.Column(db.String(500), nullable=False)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

def encode_base62(num):
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = []
    base = len(BASE62)
    while num:
        rem = num % base
        num = num // base
        l.append(BASE62[rem])
    l.reverse()
    return ''.join(l)

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400
    if 'original_url' not in data or not data['originl_url'].strip():
        return jsonify({"error": "Field 'original_url' required"}), 400
    
    new_url = URLMap(original_url=data['original_url'])
    db.session.add(new_url)
    db.session.commit()
    return jsonify({"short_url": encode_base62(new_url.id)}), 200

# @app.route('/api/redirect')
# def redirect(url):
