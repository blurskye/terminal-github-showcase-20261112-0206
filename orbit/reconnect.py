def recover(tasks):
    """Make interrupted work eligible for a new worker."""
    return [dict(task, state="queued") if task["state"] == "interrupted" else task for task in tasks]
