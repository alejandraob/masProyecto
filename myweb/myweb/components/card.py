import reflex as rx
from rxconfig import config
import myweb.styles.styles as styles
import myweb.styles.colors as colors

def card(image: str, title: str, description: str, link: str) -> rx.Component:
    """Genera una tarjeta con una imagen, título, descripción y un enlace."""
    return rx.card(
        # Contenedor de la tarjeta
        rx.vstack(
            # Imagen de la tarjeta
            rx.image(
                src=image,
                width="100%",
                height="auto",
                alt=title,
                border_radius=styles.Size.SMALL.value,
            ),
            # Título de la tarjeta
             rx.heading(title, **styles.TITLE_STYLE),  # Usa el estilo modularizado
            # Descripción de la tarjeta
            rx.text(description, **styles.TEXT_STYLE),  # Usa el estilo modularizado
            # Enlace de la tarjeta
             rx.link("Ver más", href=link, **styles.LINK_STYLE),  # Usa el estilo modularizado
        ),
        # Estilos de la tarjeta
        **styles.CARD_STYLE,  # Aplica todos los estilos de la tarjeta

    )