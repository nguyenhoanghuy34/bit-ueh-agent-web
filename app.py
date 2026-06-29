import gradio as gr

from ui.login import build_login_ui
from ui.chat import build_chat_ui
from ui.theme import theme


def create_app():

    with gr.Blocks(
        theme=theme(),
        title="UEH AI Assistant"
    ) as app:


        login_page = build_login_ui()

        chat_page = build_chat_ui()


        # mặc định ẩn chat
        chat_page.visible = False


        login_btn = login_page["button"]


        login_btn.click(
            fn=lambda mssv, khoa: (
                gr.update(visible=False),
                gr.update(visible=True)
            ),
            inputs=[
                login_page["mssv"],
                login_page["khoa"]
            ],
            outputs=[
                login_page["container"],
                chat_page["container"]
            ]
        )


    return app



if __name__ == "__main__":

    app = create_app()

    app.launch(
        server_name="0.0.0.0",
        server_port=7860
    )