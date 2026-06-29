import gradio as gr

from ui.login import build_login_ui
from ui.chat import build_chat_ui
from ui.theme import theme


def create_app():

    with gr.Blocks(
        theme=theme(),
        title="UEH AI Assistant"
    ) as app:


        login = build_login_ui()

        chat = build_chat_ui()


        login["button"].click(
            fn=lambda mssv, khoa: (
                gr.update(visible=False),
                gr.update(visible=True)
            ),
            inputs=[
                login["mssv"],
                login["khoa"]
            ],
            outputs=[
                login["container"],
                chat["container"]
            ]
        )


    return app



if __name__ == "__main__":

    app = create_app()

    app.launch(
        server_name="127.0.0.1",
        server_port=7860
    )