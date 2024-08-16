import json

class MemoryAI:
    def __init__(self, storage_file="memory.json"):
        self.storage_file = storage_file
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def update_memory(self, key, information):
        self.memory[key] = information
        self.save_memory()

    def save_memory(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def recall(self, key):
        return self.memory.get(key, "I don't have any knowledge about that yet.")
