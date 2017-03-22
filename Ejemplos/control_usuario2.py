import telebot

bot = telebot.TeleBot('<TOKEN>', skip_pending=True)

usuarios = [line.strip('\n') for line in open('usuarios.txt', 'r')]

def es_usuario(cid):
    return str(cid) in usuarios

def add_usuario(cid):
    usuarios.append(str(cid))
    with open('usuarios.txt', 'wt') as f:
        f.write('\n'.join(usuarios))

def listener(messages):
    for m in messages:
      if m.content_type == 'text':
        print("[{}] {}: {}".format(m.chat.id, m.from_user.first_name, m.text))

bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def message_start(m):
    cid = m.chat.id
    nombre_usuario = m.from_user.first_name
    if not es_usuario(cid):
        bot.send_message(cid, "¡Hola {}! Bienvenido a @{}".format(nombre_usuario, bot.get_me().username))
        add_usuario(cid)

bot.polling(True)
