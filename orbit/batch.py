def coalesce(events):
    """Keep the newest state for each task, preserving insertion order."""
    latest = {}
    for task_id, state in events:
        latest[task_id] = state
    return list(latest.items())
