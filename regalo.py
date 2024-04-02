import streamlit as st
import streamlit_lottie
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components    
import PIL.Image
from io import BytesIO
import json

st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'> Una parte de mi para ti</h1>",unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Con todo mi corazón&#128156;</h2>",unsafe_allow_html=True)
st.markdown("<hr style='border-top: 2px solid #ff0000;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>&#128007;&#128007;&#128007; </h2>",unsafe_allow_html=True)
parrafo = """
<p style="text-align: justify;">Hola Elsa bonita, feliz cumpleaños espero que tengas hoy un increible día hoy.</p>
<p style="text-align: justify;">Estoy escribiendo esto para que veas que quiero formar parte de tu vida, mi granito de arena en este día. Me hubiera gustado disfrutarlo allí contigo. Dejo aquí plasmado lo importante que eres para mi, lo que me has aportado y ayudado a seguir adelante.</p>
"""
st.markdown(parrafo, unsafe_allow_html=True)
st.image("elsa.jpg", width=300)

parrafo1 = """
<p style="text-align: justify;">Recuerdo la primera vez que nos vimos, fui la persona más feliz del mundo, me encantaba poder estar contigo en persona, abrazarte, verte reir y sonreir. El escuchar esta canción y acordarme de nosotros:</p>
"""

st.markdown(parrafo1, unsafe_allow_html=True)
st.audio("quevedo.mp3")
st.markdown("<hr style='border-top: 2px solid #ff0000;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>&#128536;&#128536;&#128536; </h2>",unsafe_allow_html=True)

parrafo2="""
<p style="align: justify;"> Recuerdo también el regalo sorpresa que me diste, lo tengo atesorado con su bolsita y el mensaje que me pusiste. Una vez al mes me hace estar feliz.

"""

st.image("elsa3.jpg", width=300)
parrafo3="""
<p style="align: justify;"> Hemos pasado muy buenos momentos juntos, algunos no tan buenos pero creo que hemos podido solucionarlo juntos, esta canción te representa mucho ya que nos conocimos en un mal momento mio, le diste luz y color y le diste toda la vuelta a mi mundo, una razón para seguir adelante.

"""
st.markdown(parrafo3,unsafe_allow_html=True)
st.audio("niñaimantada.mp3")
st.markdown("<hr style='border-top: 2px solid #ff0000;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>&#129392;&#129392;&#129392; </h2>",unsafe_allow_html=True)

st.image("elsa4.jpg", width=300)
st.image('zaragoza.jpg', width=300)
parrafo4="""
<p style="align:justify;">Hace poco me salió esta notificación es increible como hace un año pude ir a verte, como me enseñabas la ciudad, me picabas y como me cuidabas, me hubiera gustado cuidarte cuando viniste pero no me dejabas(maldita 7.7), ver tus lugares favoritos, espero volver y verlos de nuevo contigo e ir a más lugares, también espero que vengas aquí porque tengo cosas pendientes contigo.
Luego vino la euskal, fue corto pero intenso, la mejor coincidencia nada más llegar encontrarme contigo, no nos vimos mucho pero lo poco que fue lo agradezco. Te pongo esta canción que se que te gusta mucho 
"""
st.markdown(parrafo4,unsafe_allow_html=True)
st.audio("girl.mp3")

st.markdown("<hr style='border-top: 2px solid #ff0000;'>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>&#128538;&#128538;&#128538;</h2>",unsafe_allow_html=True)


st.image("elsa2.jpg", width=300)




parrafo5="""
Estoy como un niño pequeño cuando iba a regalar algo por su cumple a algún amigo suyo super contento y nervioso por ver como te quedas con esto que te doy, ahora mismo son las 3 de la mañana y pensando que más cosas bonitas ponerte, mucho me has dado ya
voy a ponerte varias canciones que siempre me recuerdan a ti. el unico favor que te pido es que el día de tu cumple despues que recibas esto quiero ver tu cara, una foto tuya, seguro que estás preciosa y saber que ese día nació una increible persona.

"""

st.markdown(parrafo5,unsafe_allow_html=True)
st.audio("lesbian.mp3")
st.audio("cupido.mp3")
st.audio("apareciste.mp3")
st.markdown("<hr style='border-top: 2px solid #ff0000;'>", unsafe_allow_html=True)



poesia="""En tanto que de rosa y de azucena
se muestra la color en tu mejilla,
y en tanto que el cabello, que en la villa
no tiene igual, al viento se despena,

goza, goza, oh, bella flor de España,
de la juventud, que en ti florece;
y antes que tu hermosura se marchite,
coge la flor que el tiempo te ofrece.

No mires, no, que la edad ligera
huye sin volver, y en un momento
se lleva tras sí la primavera
que alegra el campo y el pensamiento.

Coge, pues, el tiempo, y goza, oh, bella,
de la juventud, que en ti florece. -Garcilaso de la Vega"""
st.markdown(poesia,unsafe_allow_html=True)
st.markdown("<hr style='border-top: 2px solid #ff0000;'>", unsafe_allow_html=True)
html_content = """
<div class="corazon"></div>

"""

# Muestra el contenido en Streamlit

st.markdown(html_content, unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)

st.image("carta.gif")
st.image("mano.gif")

st.write("Te quiero muchisimo Elsa, Fin.")
