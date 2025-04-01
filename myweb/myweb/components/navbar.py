import reflex as rx
from rxconfig import config
import myweb.styles.styles as styles
import myweb.styles.colors as colors

def navbar()->rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src="mi_logo.png",
                width="auto",
                height=styles.Size.VERY_BIG.value,
                justify="start",
                alt="MyWeb logo"
            ),
            href="index"
        ),
        bg=colors.Color.BODY.value,
        position="sticky",
        border_bottom="1px solid rgba(247, 247, 247, 0.2)",
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
