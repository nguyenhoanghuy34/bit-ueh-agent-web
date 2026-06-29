import gradio as gr

from services.agent import chat_response



def build_chat_ui():


    with gr.Column(
        visible=False
    ) as container:


        gr.Markdown(
            """
            # UEH AI Assistant

            ---
            """
        )


        chatbot = gr.Chatbot(
            height=600,
            bubble_full_width=False,
            type="messages"
)


        textbox = gr.Textbox(
            placeholder="Nhập câu hỏi...",
            show_label=False
        )


        textbox.submit(
            fn=chat_response,
            inputs=[
                textbox,
                chatbot
            ],
            outputs=[
                chatbot
            ]
        )


    return {
        "container": container,
        "chatbot": chatbot
    }