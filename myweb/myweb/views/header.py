import reflex as rx
from rxconfig import config
import myweb.styles.styles as styles
from myweb.styles.colors import Color, TextColor
from myweb.styles.fonts import Font, FontWeight
from myweb.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # Imagen del logo
            rx.avatar(
                src="yo.jpg",
                width="auto",
                height=styles.Size.VERY_BIG.value,
                alt="MyWeb logo"
            ),
            # Contenedor vertical para el título y la información
            rx.vstack(
                rx.heading(
                    "MyWeb",  # Título
                    size="7",
                    font_weight=FontWeight.BOLD.value,
                    color=TextColor.WHITE.value,
                ),
                rx.text(
                    "El Lorem Ipsum fue concebido como un texto de relleno, "
                    "formateado de una cierta manera para permitir la presentación de"
                    " elementos gráficos en documentos,"
                    " sin necesidad de una copia formal. ",  # Texto de información
                    font_size="2",
                    color=TextColor.WHITE.value,
                ),
                align_items="start"
            ),
        ),
        # Íconos de enlace abajo
        rx.hstack(
            link_icon(
                image="icons8-github-48.png",  # Ruta del primer ícono
                url="https://github.com/alejandraob",
                alt="GitHub"
            ),
            link_icon(
                image="icons8-linkedin-48.png",  # Ruta del segundo ícono
                url="www.linkedin.com/in/maría-alejandra-ojeda-boisier-506015b3",
                alt="LinkedIn"
            ),
            spacing=styles.Spacing.BIG.value
        ),
        align_items="center",
        spacing=styles.Spacing.LARGE.value
    )
