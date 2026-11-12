def bounded_delay(attempt, maximum=60):
    """Cap retry time without sleeping inside the queue controller."""
    return min(2 ** min(max(0, attempt), 16), maximum)
