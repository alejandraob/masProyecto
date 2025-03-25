# Description: This file contains the styles for the website
import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#Constants for the website
MAX_WIDTH ="600px"

class Size(Enum):
    """A class to define the spacing for the website."""
    ZERO="0px"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"

##Styles for the website
BASE_STYLE = {
    "font_family": Font.BODY.value,
    "background_color": Color.BACKGROUND.value,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border-radius":Size.SMALL.value,
        "color":TextColor.WHITE.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value,
        }	
    },
    rx.link:{
        "text-decoration":"none",
        "color":"black",
        "_hover":{}
    },
}


navbar_title_style=dict(

    font_size=Size.LARGE.value,  # Se debe usar rx.text para el body también
    font_family=Font.LOGO.value, 
    color=TextColor.WHITE.value

)




button_title_style=dict(

    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    padding_top=Size.SMALL.value,
    width="100%",
    font_family=Font.PRIMARY.value

)

button_body_style=dict(

    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
    padding_top=Size.SMALL.value,
    width="100%",
    padding_bottom=Size.SMALL.value,
    font_familia=Font.PRIMARY.value
)

title_style=dict(

    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.WHITE.value,
    font_size=Size.DEFAULT.value,
    font_family=Font.DEFAULT.value

)