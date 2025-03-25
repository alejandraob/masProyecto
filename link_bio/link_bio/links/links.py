import reflex as rx
from rxconfig import config

# vamos a importar los links que estan en la carpeta links
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def links() -> rx.Component:
    return rx.vstack(
        title("Mis redes sociales"),
        link_button(
            "facebook", "mi vida personal", "https://www.facebook.com/alejandraob1"
        ),
        link_button(
            "instagram",
            "mi vida personal",
            "https://www.instagram.com/alejandraboisier/",
        ),
        link_button(
            "linkedin",
            "mi vida personal",
            "www.linkedin.com/in/maría-alejandra-ojeda-boisier-506015b3",
        ),
        width="100%",
        style={"gap": Size.MEDIUM.value}
        
    )
