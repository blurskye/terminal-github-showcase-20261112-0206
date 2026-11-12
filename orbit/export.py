import json

def export_tasks(tasks):
    return json.dumps({"version": 1, "tasks": tasks}, ensure_ascii=False, indent=2)
