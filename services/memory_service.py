from db.redis_db import redis_client


def get_history(
    session_id: str
):

    history = redis_client.get(session_id)

    if history:
        return history

    return ""


def save_history(
    session_id: str,
    user_question: str,
    answer: str
):

    previous = get_history(session_id)

    updated = f"""
    {previous}

    User: {user_question}

    Assistant: {answer}
    """

    redis_client.set(
        session_id,
        updated
    )