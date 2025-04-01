"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import myweb.styles.styles as styles
from myweb.styles.colors import Color, TextColor
from myweb.styles.fonts import Font, FontWeight
import myweb.pages.index as index

class State(rx.State):
    """The app state."""

    ...



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)


# La ruta de la página de inicio debe ser "/"
app.add_page(index, route="index")

