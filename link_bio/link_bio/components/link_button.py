import reflex as rx
from rxconfig import config
from link_bio.styles import styles


def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            ##text,width="100%"
            rx.hstack(
                rx.icon(
                    "moon",
                    tag="moon",
                    width=styles.Size.DEFAULT.value,
                    height=styles.Size.DEFAULT.value,
                    margin=styles.Size.MEDIUM.value,
                ),
            ),
            rx.vstack(
                rx.text(title, style=styles.button_title_style),
                rx.text(body, style=styles.button_body_style),
                align_items="start",
                margin=styles.Size.ZERO.value,
                style={"gap": styles.Size.BIG.value}
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
    )
