import chainlit as cl

from core.chat import ask_model
from ui.components import (
    show_suggestions,
    show_edit_button,
    show_file_result
)


@cl.on_message
async def chat(message: cl.Message):

    question = message.content


    # =========================
    # Hiện câu hỏi người dùng
    # =========================

    await cl.Message(
        content=f"""
### ❓ Câu hỏi của bạn

{question}
"""
    ).send()



    # =========================
    # Xử lý file upload
    # =========================

    if message.elements:

        for file in message.elements:

            await show_file_result(
                file.name,
                "Đã nhận file, đang phân tích..."
            )


            # sau này:
            # PDF Agent
            # Vision Agent
            # Document Agent



    # =========================
    # Response model
    # =========================

    answer = await ask_model(
        question
    )


    response = cl.Message(
        content=""
    )

    await response.send()


    # streaming giả lập
    await response.stream_token(
        answer
    )



    # =========================
    # Action
    # =========================

    await show_edit_button(
        question
    )


    # =========================
    # Gợi ý
    # =========================

    await show_suggestions()