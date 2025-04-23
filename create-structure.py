import os

structure = {
    "ai-trip-planner": {
        "backend": {
            "llm": ["itinerary_generator.py"],
            "planner": ["flights.py", "hotels.py", "daysplitter.py"],
            "models": ["activity_model.py", "hotel_model.py"],
            "routes": ["trip_routes.py", "flight_routes.py"],
            "__files__": ["server.py"]
        },
        "data": ["activities.json", "hotels.json"],
        "__files__": ["app.py", "requirements.txt", "README.md"]
    }
}

def create_tree(base_path, tree):
    for name, content in tree.items():
        if name == "__files__":
            for file in content:
                file_path = os.path.join(base_path, file)
                with open(file_path, 'w') as f:
                    f.write("")  # empty file
        else:
            dir_path = os.path.join(base_path, name)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(content, dict):
                create_tree(dir_path, content)
            elif isinstance(content, list):
                for file in content:
                    file_path = os.path.join(dir_path, file)
                    with open(file_path, 'w') as f:
                        f.write("")  # empty file

create_tree(".", structure)
