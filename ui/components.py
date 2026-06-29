import chainlit as cl

from config import APP_NAME, LOGO_PATH


async def show_header():
    """
    Header của ứng dụng
    """

    await cl.Message(
        content=f"""
# 🎓 {APP_NAME}

Trợ lý AI hỗ trợ học tập

---
"""
    ).send()



async def show_welcome():

    await cl.Message(
        content="""
Xin chào 👋

Bạn có thể:

📄 Upload PDF / PPT  
🖼️ Gửi hình ảnh  
💬 Đặt câu hỏi  
📝 Yêu cầu phân tích tài liệu

"""
    ).send()



async def show_suggestions():

    suggestions = [
        "📄 Tóm tắt tài liệu này",
        "🔍 Phân tích nội dung PDF",
        "🖼️ Phân tích hình ảnh",
        "✍️ Viết báo cáo"
    ]


    actions = []


    for item in suggestions:

        actions.append(
            cl.Action(
                name="suggest",
                label=item,
                value=item
            )
        )


    await cl.Message(
        content="### 💡 Gợi ý câu hỏi",
        actions=actions
    ).send()



async def show_logo():

    await cl.Message(
        content="🎓 UEH AI Assistant",
        elements=[
            cl.Image(
                path=LOGO_PATH,
                name="logo",
                display="inline"
            )
        ]
    ).send()



async def show_file_result(
        filename,
        message
):

    await cl.Message(
        content=f"""
### 📎 File

`{filename}`


{message}
"""
    ).send()



async def show_edit_button(
        question
):

    await cl.Message(
        content="Bạn muốn chỉnh sửa câu hỏi?",
        actions=[
            cl.Action(
                name="edit_question",
                label="✏️ Sửa câu hỏi",
                value=question
            )
        ]
    ).send()