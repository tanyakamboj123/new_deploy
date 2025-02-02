from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load student data from the JSON file
with open("q-vercel-python.json", "r") as file:
    students_data = json.load(file)

# Create a dictionary for quick look-up by name
students_dict = {student["name"]: student["marks"] for student in students_data}
print(students_dict)

# Define the API endpoint

@app.get("/api")
async def get_marks(names:Optional[List[str]]=Query(None, alias="name")):
    # Split names by comma if provided as a single string
    
    print(f"Names received in query: {names}")  # Debug print

    marks = []
    for name in names:
        if name in students_dict:
            marks.append(students_dict[name])
        else:
            marks.append("Not Found")

    print(f"Marks for the requested names: {marks}")  # Debug print
    return JSONResponse(content={"marks": marks})
