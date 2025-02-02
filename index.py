from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student data from JSON file
with open("q-vercel-python.json", "r") as file:
    
    student_data = json.load(file)

@app.route('/', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get all 'name' query parameters
   
    # Find the marks for each student name
    marks = []
    for name in names:
        student = next((item for item in student_data if item["name"] == name), None)
        if student:
            marks.append(student["marks"])
        else:
            marks.append("Not found")

    return jsonify({"marks": marks})
if __name__ == "__main__":
    app.run(debug=True)
