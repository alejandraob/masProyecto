import reflex as rx
from rxconfig import config
from link_bio.styles import styles
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def link_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            "link",
            tag="link"

        ),
        href=url,
        is_external=True,
        color=TextColor.SECONDARY.value

    )