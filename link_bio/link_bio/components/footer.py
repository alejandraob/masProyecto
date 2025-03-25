import reflex as rx
from rxconfig import config
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

import datetime


def footer() -> rx.Component:
    """The footer component."""
    return rx.hstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"Made with Reflex desde 2024 - {datetime.date.today().year}",
            href="https://reflexjs.org",
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.text("Made with Reflex", font_size=Size.MEDIUM.value, margin_top="0px !important" ),
        margin_botton=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_y=Size.SMALL.value,
        bg=Color.BACKGROUND.value,
        color=TextColor.FOOTER.value,
        justify_content="center",
        align_items="center",
        width="100%"

    )
