
import json
from http.server import BaseHTTPRequestHandler

# Load student data from the JSON file
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

        # Extract student names from query parameters
        names = self.parse_query_parameters()

        # Get marks for the names in the query
        marks = {"marks": [student_data.get(name, "Not found") for name in names]}
        
        # Send the JSON response
        self.wfile.write(json.dumps(marks).encode('utf-8'))

    def parse_query_parameters(self):
        query = self.path.split('?')[-1]
        query_dict = {}
        if query:
            for param in query.split('&'):
                key, value = param.split('=')
                query_dict[key] = value
        return query_dict.get('name', [])
