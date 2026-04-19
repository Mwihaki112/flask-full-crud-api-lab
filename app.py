from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

next_id = 3

# Welcome message
@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Events API"})

# Get all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_id = max(event.id for event in events) + 1 if events else 1

    #Create a new event object and add it to the list
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    # TODO: Task 3 - Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:

            # Validate input
            if not data or "title" not in data:
                return jsonify({"error": "Title is required"}), 400

            # Update title
            event.title = data["title"]    
# TODO: Task 4 - Return and Handle Results
            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404

    

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    for event in events:
        if event.id == event_id:
            events.remove(event)


            return jsonify({"message": "Event deleted successfully"}), 200

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
