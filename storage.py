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

    def add_deadline(self, task, date, status):
        new_entry = {
            "id": str(uuid.uuid4()),
            "task": task,
            "date": date,
            "status": status
        }
        self._deadlines.append(new_entry)
        return new_entry

    def update(self, deadline_id, task, date, status):
        for d in self._deadlines:
            if d['id'] == deadline_id:
                d['task'] = task
                d['date'] = date
                d['status'] = status
                return True
        return False

    def delete_deadline(self, deadline_id):
        self._deadlines = [d for d in self._deadlines if d['id'] != deadline_id]

store = DeadlineStore()