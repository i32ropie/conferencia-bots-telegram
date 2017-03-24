import telebot
import requests

bot = telebot.TeleBot('<TOKEN>', skip_pending=True)

url = "http://telegramforo.com/apis/letras.php"

@bot.message_handler(commands=['dobles','cursivas','peques'])
def funcion_letras(m):
    cid = m.chat.id
    comando = m.text.split(" ", 1)[0].strip("/")
    if len(m.text.split()) == 1:
        bot.send_message(cid, "Error, se necesita un texto a trasnformar.")
    else:
        texto_escrito = m.text.split(" ", 1)[1]
        parametros = {
            "texto": texto_escrito,
            "formato": comando
        }
        r = requests.get(url, parametros)
        if r.status_code != 200:
            bot.send_message(cid, "Error conectándose al servidor.")
        else:
            r_json = r.json()
            if r_json["ok"]:
                texto_transformado = r_json["resultado"]["texto"]
                bot.send_message(cid, texto_transformado)
            else:
                texto_error = r_json["resultado"]["error"]
                bot.send_message(cid, texto_error)


bot.polling(True)
