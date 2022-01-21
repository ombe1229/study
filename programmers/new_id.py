import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9\-_.]", "", new_id)
    new_id = re.sub("\.+", ".", new_id)
    new_id = re.sub("^[.]|[.]$", "", new_id)
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    new_id = re.sub("^[.]|[.]$", "", new_id)
    new_id = (
        new_id
        if len(new_id) > 2
        else new_id + "".join([new_id[-1] for i in range(3 - len(new_id))])
    )
    return new_id
