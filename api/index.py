from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json

from fastapi.middleware.cors import CORSMiddleware

app = Flask(__name__)
CORS(app)
# Load student data from JSON filevhgvhgvhvhhb
with open("api/q-vercel-python.json", "r") as file:
    
    student_data = json.load(file)

@app.route('/api', methods=['GET']) #hjknkj
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
