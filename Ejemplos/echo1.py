# Importamos el módulo
import telebot

# Declaramos el bot
bot = telebot.TeleBot('<TOKEN>')

# Declaramos la función que recibirá todos los mensajes que el bot reciba
# Esta función recibirá como parámetro una lista de mensajes (Los recibidos
# con cada update pedido a Telegram)
def listener(messages):
    # Iteramos sobre la lista de mensajes y
    for m in messages:
        # por cada mensaje, comprobamos que sea de texto y
        if m.content_type == 'text':
            # enviamos al chat que ha escrito al bot el mismo texto que recibimos
            bot.send_message(m.chat.id, m.text)

# Indicamos que la función recién creada será la que reciba los mensajes
bot.set_update_listener(listener)

# Indicamos que queremos empezar a solicitar los nuevos mensajes a Telegram
bot.polling(True)
