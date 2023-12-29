from flask import Flask, jsonify, request

app = Flask(__name__)
users = []


# GET /users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users}), 200


@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    new_user = {
        'name': request_data['name'],
        'age': request_data['age'],
        'occupation': request_data['occupation']
    }
    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(port=5000, debug=True)
