from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    r.set(user_id, json.dumps(data))
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    cached_user = r.get(user_id)
    if cached_user:
        return jsonify(json.loads(cached_user)), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

