from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app) # todo: best to add origins
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original_url = db.Column(db.String(500), nullable=False)

def encode_base62(num: int) -> str:
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = []
    base = len(BASE62)
    while num:
        rem = num % base
        num = num // base
        l.append(BASE62[rem])
    l.reverse()
    return ''.join(l)

def decode_base62(s: str) -> int:
    s = s.strip()
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = 0
    base = len(BASE62)
    for c in s:
        value = value * base + BASE62.index(c)
    return value

def is_valid_url(url: str, timeout: int) -> bool:
    try:
        res = requests.head(url, allow_redirects=True, timeout=timeout)
        if res.status_code < 400:
            return True
        if res.status_code in [403, 405]: # some site might not support HEAD
            res = requests.get(url, allow_redirects=True, timeout=timeout)
            return res.status_code < 400
    except requests.RequestException:
        return False
    return False

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json(silent=True)
    original_url = data['original_url']
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400
    if 'original_url' not in data or not original_url.strip():
        return jsonify({"error": "Field 'original_url' required"}), 400
    
    if not original_url.startswith("https://") and not original_url.startswith("http://"):
        original_url = "https://" + original_url
    
    res = URLMap.query.filter_by(original_url=original_url).first()
    if res:
        return jsonify({"short_url": encode_base62(res.id)}), 200

    if not is_valid_url(original_url, 5):
        return jsonify({"error": "Original url not reachable"}), 400

    new_url = URLMap(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
    return jsonify({"short_url": encode_base62(new_url.id)}), 200

@app.route('/<short_url>')
def redirect_to_short_url(short_url):
    decoded_id = decode_base62(short_url)
    url_map = URLMap.query.filter_by(id=decoded_id).first()
    if url_map:
        return redirect(url_map.original_url)
    else:
        return "URL not found", 404

# creates all db tables that correspond to SQLAlchemy models
with app.app_context():
    db.create_all()
