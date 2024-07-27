from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = []
current_id = 1


# Example route for GET request
@app.route('/user', methods=['GET'])
def get_user():
    return jsonify(users)


# Example route for POST request
@app.route('/user', methods=['POST'])
def create_user():
    global current_id
    new_user = request.get_json()
    new_user['id'] = current_id
    users.append(new_user)
    current_id += 1
    response = {
        "message": "User created successfully",
        "user": new_user
    }
    return jsonify(response), 201


if __name__ == '__main__':
    app.run(debug=True)
