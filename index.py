from flask import Flask, request, jsonify
app=Flask(__name__)

@app.route("/api")
def home():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
#run the server