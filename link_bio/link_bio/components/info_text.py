import reflex as rx
from rxconfig import config
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title, font_weight="bold", color=Color.PRIMARY.value, as_="span"
        ),  # Aquí está el cambio
        f" {body}",
        font_size=Size.MEDIUM.value,  # Se debe usar rx.text para el body también
       color=TextColor.SECONDARY.value
    )
