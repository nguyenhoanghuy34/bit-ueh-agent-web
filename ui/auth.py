import chainlit as cl

from core.session import set_user_profile


@cl.on_chat_start
async def auth():


    res = await cl.AskUserMessage(
        content="""
# 🎓 UEH AI Assistant

Vui lòng nhập thông tin:

Mã số sinh viên:
Khóa:
""",
        timeout=300
    ).send()


    if res:

        text = res["output"]


        data = text.split(",")


        mssv = data[0]
        course = data[1] if len(data)>1 else "unknown"


        set_user_profile(
            mssv,
            course
        )


        await cl.Message(
            content="""
# ✅ Xác thực thành công

Chào bạn 👋

Bạn có thể bắt đầu hỏi AI.
"""
        ).send()