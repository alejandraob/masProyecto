"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import myweb.styles.styles as styles
import myweb.styles.colors as colors
import myweb.styles.fonts as fonts
import myweb.pages.index as index

class State(rx.State):
    """The app state."""

    ...



app = rx.App(
    stylesheets=styles.STYLESHEETS,
)


# La ruta de la página de inicio debe ser "/"
app.add_page(index, route="index")

