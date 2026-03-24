from typing import List, Dict


class TaskStorage:
    def __init__(self):
        self._tasks: List[Dict] = [
            {"id": 1, "title": "Learn Docker", "done": False},
            {"id": 2, "title": "Prepare for Kubernetes", "done": False},
        ]

    def list_tasks(self) -> List[Dict]:
        return self._tasks

    def add_task(self, title: str) -> Dict:
        new_task = {
            "id": len(self._tasks) + 1,
            "title": title,
            "done": False,
        }
        self._tasks.append(new_task)
        return new_task