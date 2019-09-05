def enough(cap, on, wait):
    if wait <= cap - on:
        return 0
    return wait - (cap - on)