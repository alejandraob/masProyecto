"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.links.links import links
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding="16px",
                margin_y=styles.Size.BIG.value,
            )
        ),
        footer(),
    )


app = rx.App(style=styles.BASE_STYLE)
app.add_page(index,
             title="Es alejandraob1",
             description="Alejandra Ojeda Boisier",
             )
