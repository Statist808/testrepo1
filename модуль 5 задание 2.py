class save():
    import json
    try:
        with open('1.json', "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

