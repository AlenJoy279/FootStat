import json

def jsonl_to_json(jsonl):
    # returns list of dictionaires - each dictionary is the tweet with data such as creation date, source, id, etc.

    with open(jsonl) as f:
        list_jsonl = list(f)

    return [json.loads(jline) for jline in list_jsonl]

