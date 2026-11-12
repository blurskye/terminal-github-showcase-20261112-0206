def search(names, query):
    """Rank case-insensitive task-name matches without changing source names."""
    needle = query.casefold().strip()
    return sorted((name for name in names if needle in name.casefold()), key=len)
