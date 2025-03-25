import reflex as rx
from rxconfig import config
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="Ale", size="6",radius="full",
                      src="patito.jpg",
                      padding="2px",
                      border="4px",
                      border_color=Color.PRIMARY.value,
                      ),
            rx.vstack(
                rx.heading("Alejandra", size="3", style=styles.title_style),
                rx.text(
                    "quien corno creo reflex", size="1", margin_top="0px !important",
                    color=TextColor.SECONDARY.value
                ),
                rx.hstack(
                    link_icon("www.facebook.com"),
                    link_icon("www.facebook.com"),
                    link_icon("www.facebook.com"),
                    link_icon("www.facebook.com")
                ),
                aling_items="start"
            ),
                style={"gap": Size.BIG.value}
        ),
        rx.flex(info_text("0", "experiencia en reflex"),
                rx.spacer(),
                info_text("0", "experiencia en reflex"),
                rx.spacer(),
                info_text("0", "experiencia en reflex"),
                width="100%",

                
                ),
        rx.text(
            "Purus convallis congue ut egestas nostra habitasse gravida,"
            " euismod nisl suscipit rutrum vehicula porttitor commodo, rhoncus "
            "augue tempor lacus lobortis torquent. Lacus est nibh morbi himenaeos "
            "porttitor per pellentesque venenatis augue, egestas a purus senectus"
            " luctus lectus proin curabitur. Blandit magnis dapibus suscipit"
            " ultricies lectus scelerisque pulvinar,"
            " fermentum pharetra habitant duis ante taciti class quisque, ornare "
            "condimentum aliquam volutpat sociis senectus.",
            color=TextColor.SECONDARY.value,
            size="2",
            margin_top="0px !important",
            width="100%",
            margin_bottom=Size.BIG.value

        ),
        style={"gap": Size.BIG.value},
        aling_items="start",
    )
