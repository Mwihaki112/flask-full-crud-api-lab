# Events Manager (Flask REST API)

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instuctions)
- [How to Use](#how-to-use)
- [API Endpoints](#api-endpoints)
- [Folder Structure](#folder-structure)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Project Description
Events Manager is a simple RESTful API built with Python and Flask that allows users to manage event data.
The application demonstrates core backend development concepts including RESTful routing, JSON handling, and full CRUD (Create, Read, Update, Delete) operations using in-memory storage.
It focuses on building clean API structure, proper HTTP methods, and meaningful responses.

## Features
- Add new events
- View all events
- Update event titles
- Delete events
- Input validation for required fields
- Proper error handling with clear messages
- RESTful API structure

## Technologies Used
Backend
- Python 3
- Flask
- Pipenv (virtual environment & dependency management)
- Flask JSON handling (jsonify)
- Flask request handling (request.get_json())

Concepts
- REST API design
- CRUD operations
- HTTP methods (GET, POST, PATCH, DELETE)
- In-memory data storage

## Setup Instructions
1. Clone the repository
git clone https://github.com/Mwihaki112/flask-full-crud-api-lab.git
cd flask-full-crud-api-lab
2. Set up virtual environment using Pipenv
pipenv --python 3
pipenv install
3. Activate the environment
pipenv shell
4. Run the application
python app.py
The API will run on: http://127.0.0.1:5000

## How to Use
- Start the Flask server
- Use the terminal(curl) or browser
- Send requests to the API endpoints
- View JSON responses

## API Endpoints
Base Route
GET / → Welcome message

Events Routes
GET /events → Retrieve all events
POST /events → Create a new event
PATCH /events/<id> → Update event title
DELETE /events/<id> → Delete an event

## Example Requests & Responses
- GET /events
curl http://127.0.0.1:5000/events

json
[
  { "id": 1, "title": "Tech Meetup" },
  { "id": 2, "title": "Python Workshop" }
]


- POST /events
 curl -X POST http://127.0.0.1:5000/events -H "Content-Type: application/json" -d '{"title": "Hackathron"}'
 json
{ "id": 3, 
  "title": "Hackathon" 
}


- PATCH /events/1
curl -X PATCH http://127.0.0.1:5000/events/1 -H "Content-Type: application/json" -d '{"title": "Hackathron 2026"}'

json
{ "id": 1, "title": "Hackathon 2026" }


- DELETE /events/2
curl -X DELETE http://127.0.0.1:5000/events/2

json
{ "message": "Event 2 deleted successfully" }

## Folder Structure
flask-full-crud-api-lab/
│
├── app.py
├── Pipfile
├── Pipfile.lock
└── README.md

## Future Improvements
- Add database integration (SQLite / PostgreSQL)
- Add authentication (JWT)
- Improve project structure using Flask Blueprints
- Deploy API (Render / Railway / Vercel)
- Add input validation library (Marshmallow / WTForms)

## Author
Agnes Ng’anga
GitHub: https://github.com/Mwihaki112⁠