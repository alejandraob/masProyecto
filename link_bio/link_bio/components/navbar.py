import reflex as rx
from rxconfig import config
from link_bio.styles import styles
from link_bio.styles.styles import navbar_title_style
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color

def navbar() -> rx.Component:
    """The navbar component."""
    return rx.hstack(
        rx.box(
            rx.text("MAOB", as_="span"),  # Esto es lo correcto
            "91",  # Quitamos la interpolación innecesaria
            style=styles.navbar_title_style  # Se usa "style" en vez de "styles"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=9999,
        top=0,
    )
