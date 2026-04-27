import uuid

class DeadlineStore:
    def __init__(self):
        self._deadlines = [
            {
                "id": str(uuid.uuid4()),
                "task": "Email Fulbright",
                "date": "2026-04-30",
                "status": "pending"
            }
        ]

    def get_deadlines(self):
        return sorted(self._deadlines, key=lambda x: x['date'])

    def add(self, task, date):
        new_entry = {
            "id": str(uuid.uuid4()),
            "task": task,
            "date": date,
            "status": "pending"
        }
        self._deadlines.append(new_entry)
        return new_entry

    def delete(self, deadline_id):
        self._deadlines = [d for d in self._deadlines if d['id'] != deadline_id]

store = DeadlineStore()