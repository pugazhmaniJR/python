  # Basic Flask App

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(debug=True)


  #  Returning HTML
@app.route("/about")
def about():
    return "<h1>About Page</h1>"




  #  REST API with Flask   module 19



from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{"id": 1, "name": "Alice"}]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run()
