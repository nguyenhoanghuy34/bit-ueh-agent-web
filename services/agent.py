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
        {
            "role": "user",
            "content": message
        }
    )


    history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    return history