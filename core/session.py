import chainlit as cl


def set_user_profile(
        mssv,
        course
):

    cl.user_session.set(
        "profile",
        {
            "mssv": mssv,
            "course": course
        }
    )



def get_profile():

    return cl.user_session.get(
        "profile"
    )