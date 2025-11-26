from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is a simple Flask Web Server."

@app.route("/hello")
def hello():
    return "Welcome! You are visiting /hello page."

@app.route("/info", methods=["GET"])
def info():
    user_agent = request.headers.get("User-Agent")
    return f"Your browser is: {user_agent}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
