from dataclasses import dataclass


@dataclass
class Task:
    name: str
    attempts: int = 0
    state: str = "queued"


def retry_delay(attempt: int) -> int:
    """Return a bounded exponential retry delay in seconds."""
    bounded_attempt = min(max(0, attempt), 6)
    return min(1 << bounded_attempt, 60)


def summarize(tasks: list[Task]) -> dict[str, int]:
    counts = {"queued": 0, "running": 0, "done": 0}
    for task in tasks:
        counts[task.state] = counts.get(task.state, 0) + 1
    return counts
