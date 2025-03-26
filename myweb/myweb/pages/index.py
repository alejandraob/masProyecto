import reflex as rx
from rxconfig import config
import myweb.styles.styles as styles
import myweb.styles.colors as colors
import myweb.styles.fonts as fonts

@rx.page(
    title="MyWeb",
    description="A simple web app"

)
#Bueno aqui crearemos el index de la pagina
def index():
    return rx.box(
        rx.text("La puta que te pariooooo!!!")
        )
    