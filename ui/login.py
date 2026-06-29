import gradio as gr


def build_login_ui():

    with gr.Column() as container:

        gr.Markdown(
            """
            # UEH AI Assistant

            Vui lòng xác thực
            """
        )


        mssv = gr.Textbox(
            label="MSSV",
            placeholder="Nhập MSSV"
        )


        khoa = gr.Textbox(
            label="Khóa",
            placeholder="Ví dụ: K49"
        )


        button = gr.Button(
            "Xác thực",
            variant="primary"
        )


    return {
        "container": container,
        "mssv": mssv,
        "khoa": khoa,
        "button": button
    }