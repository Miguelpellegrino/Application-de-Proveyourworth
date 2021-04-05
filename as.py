import requests
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw,ImageFont



def autenticacion(urls_lvl3, session):
    request = session.get(urls_lvl3[0])
    html_body = BeautifulSoup(request.text, 'html.parser')
    lvl3_pass = session.get(urls_lvl3[1]+f'={html_body}')
    return True if (lvl3_pass,request,html_body) else False

def crearimagen(autenticacion):
    if autenticacion == True:
        requestt = session.get(urls_lvl3[2],stream=True)
        image = requestt.raw
        image = Image.open(image)
        draw = ImageDraw.Draw(image)
        draw.text((5,5), f"Miguel Armando Pellegrino Cardenas, \n miguelpellegrino2019@gmail.com \n Programador en Python",fill=(255,255,255,128))
<<<<<<< HEAD:as.py
        image.save("foto.jpg","JPEG")
=======
        image.save("image.jpg","JPEG")
>>>>>>> a44ed8595d8f6665e193ed2b2a15515e4c33204f:code/create_img.py
    else:
        print("Fallo en la autenticacion de las URL")


def enviar(urls_lvl3):
    payload = session.get(urls_lvl3[2])
    enviar = f"{payload.headers['X-Post-Back-To']}"
    file = {
        "code":open("as.py","rb"),
        "resume":open("C_V(MiguelPellegrino).pdf","rb"),
        "image":open("foto.jpg","rb")
    }
    data = {
        "email":"miguelpellegrino2019@gmail.com",
        "name":"Miguel Armando Pellegrino Cardenas",
    }
    request = session.post(enviar, data=data, files=file)


urls_lvl3= ['http://www.proveyourworth.net/level3/start', 
            'http://www.proveyourworth.net/level3/activate?statefulhash', 
            'http://www.proveyourworth.net/level3/payload']
session = requests.Session()

crearimagen(autenticacion(urls_lvl3,session))
enviar(urls_lvl3)