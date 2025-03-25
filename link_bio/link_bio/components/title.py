import reflex as rx
from rxconfig import config

from link_bio.styles import styles

def title(text:str)-> rx.Component:
    return rx.heading(
        text,
        size="5",
       style=styles.title_style,
  
          )