import json

def load_chat_ids(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    

def save_chat_ids(filename, user_ids):
    with open(filename, 'w') as file:
        json.dump(user_ids, file)


def update_user_ids(filename, new_user_id):
    user_ids = load_chat_ids(filename)
    if new_user_id not in user_ids:
        user_ids.append(new_user_id)
        save_chat_ids(filename, user_ids)
        return True
    return False