import reflex as rx
from enum import Enum
import myweb.styles.colors as colors
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"



STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;500;700&display=swap",

]

#sizes // tamaños
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
#spacing // espaciado
class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value,
    font_weight=FontWeight.BOLD.value
)


# Styles // estilos
BASE_STYLE = {
    "font_family": Font.PRIMARY.value,
    "color": TextColor.WHITE.value,
    "background_color": Color.BODY.value
    }





# Estilos para la tarjeta
CARD_STYLE = {
    "background_color": colors.Color.PRIMARY.value,
    "border": f"2px solid {colors.Color.LIGHTSECONDARY.value}",
    "box_shadow": "0 4px 10px rgba(203, 156, 242, 0.3)",  # Sombra para profundidad
    "border_radius": "10px",
    "padding": "1em",
    "transition": "all 0.3s ease-in-out",
    "_hover": {
        "filter": "brightness(1.2)",  # Efecto hover
        "border_color": colors.TextColor.LIGHTSECONDARY_TEXT.value,
    },
}

# Estilos para el título
TITLE_STYLE = {
    "size": "4",
    "font_weight": "700",  # Negrita
    "color": colors.TextColor.WHITE.value,
}

# Estilos para el texto descriptivo
TEXT_STYLE = {
    "font_size": "2",
    "color": colors.TextColor.LIGHTSECONDARY_TEXT.value,
}

# Estilos para los links
LINK_STYLE = {
    "color": colors.TextColor.LIGHTSECONDARY_TEXT.value,
    "_hover": {"color": colors.TextColor.WHITE.value},  # Cambio de color al pasar el mouse
}