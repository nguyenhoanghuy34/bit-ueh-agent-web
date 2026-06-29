def chat_response(
    message,
    history
):

    history = history or []


    answer = (
        "Bạn vừa hỏi: "
        + message
    )


    history.append(
        (message, answer)
    )


    return history