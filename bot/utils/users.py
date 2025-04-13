from repo.json_storage import get_all_users


def get_all_users_ids() -> list[int]:
    """Return a list of integers representing user IDs."""
    users = get_all_users()
    return [int(user['tg_id']) for user in users]
