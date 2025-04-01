import reflex as rx
from rxconfig import config
from myweb.components.card import card
import myweb.styles.styles as styles
import myweb.styles.colors as colors

def card_view() -> rx.Component:
    """Genera una vista de tarjeta con imagen, título, descripción y enlace."""
    return rx.grid(
        rx.foreach(
            [
                {
                    "image": "/img/form-100.png",
                    "title": "Proyecto 1",
                    "description": "Descripción del proyecto 1.",
                    "link": "/proyecto1",
                },
                {
                    "image": "/img/checklist-100.png",
                    "title": "Proyecto 2",
                    "description": "Descripción del proyecto 2.",
                    "link": "/proyecto2",
                },
                {
                    "image": "/img/table-100.png",
                    "title": "Proyecto 3",
                    "description": "Descripción del proyecto 3.",
                    "link": "/proyecto3",
                },
                {
                    "image": "/img/img-100.png",
                    "title": "Proyecto 4",
                    "description": "Descripción del proyecto 4.",
                    "link": "/proyecto4",
                },
                {
                    "image": "/img/qr-100.png",
                    "title": "Proyecto 5",
                    "description": "Descripción del proyecto 5.",
                    "link": "/proyecto5",
                },
                {
                    "image": "/img/chart-100.png",
                    "title": "Proyecto 6",
                    "description": "Descripción del proyecto 6.",
                    "link": "/proyecto6",
                },
            ],
            lambda item: card(
                image=item["image"],
                title=item["title"],
                description=item["description"],
                link=item["link"],
            )  # Eliminé la coma innecesaria aquí
        ),
        columns="3",
        spacing="4",
        width="100%",
    )  # Ajusté la indentación del cierre del paréntesis
