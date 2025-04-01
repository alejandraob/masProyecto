import reflex as rx
from rxconfig import config
import myweb.styles.styles as styles
import myweb.styles.colors as colors
import myweb.styles.fonts as fonts

def footer()->rx.Component:
    return rx.box(
        rx.text("© 2025 MyWeb", 
                color_scheme="indigo",
                high_contrast=True,
                align="center",
                font_size=fonts.FontWeight.LIGHT.value),
        bg=colors.Color.BODY.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        justify="center",
        align="center",
        border_top="1px solid rgba(247, 247, 247, 0.2)",
        position="sticky",
        bottom="0",
        z_index="999"
    )