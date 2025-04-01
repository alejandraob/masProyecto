import reflex as rx
from rxconfig import config
import myweb.styles.styles as styles
import myweb.styles.colors as colors
import myweb.styles.fonts as fonts

#Aqui importamos todos los componentes necesarios para armar el index

from myweb.components.navbar import navbar
from myweb.components.footer import footer
from myweb.views.proyectos import card_view
from myweb.views.header import header

@rx.page(
    title="MyWeb",
    description="A simple web app"

)
#Bueno aqui crearemos el index de la pagina
def index():
    return rx.box(
      
           navbar(),
          rx.container(header()),
            rx.container(
                card_view(),
            ),

           footer()


        )
    