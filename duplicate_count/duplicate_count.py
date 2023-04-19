def duplicate_count(text):
    text = text.lower()
    return len(set([x for x in text if text.count(x) > 1]))
