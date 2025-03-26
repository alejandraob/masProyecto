import reflex as rx
from enum import Enum
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
   
}




