import telepot
import os
import time
import config
from datetime import datetime

def obtener_temp():
    salida = os.popen("vcgencmd measure_temp").read()
    solo_numero = salida.replace("temp=","").replace("'C\n", "")
    return float(solo_numero)

def manejar_mensaje(msg):
    chat_id = msg['chat']['id']
    comando = msg['text']
    
    print(f" Recibido: {comando}")
    
    if comando == "/temp":
        lectura = obtener_temp()
        bot.sendMessage(chat_id, f" Mi temperatura actual es: {lectura}")
    elif comando == "/hola":
        bot.sendMessage(chat_id, f" ¡Hola, jefe! Estoy vigilando el sistema.")
    elif comando =="/historial":
        resumen = leer_historial()
        bot.sendMessage(chat_id, f"Ultimos incidentes:\n{resumen}")
    else:
        bot.sendMessage(chat_id, "No entiendo este comando. Prueba con /temp")
        

def guardar_en_log(temperatura):
    # Conseguimos la fecha y la hora actual
    ahora = datetime.now().strftime("%H:%M:%S")
    
    # Abrimos el archivo para que escriba el log con append
    with open("log_temperatura.txt", "a") as archivo:
        archivo.write(f"[{ahora}] Temperatura: {temperatura}ºC\n")
    
    
def leer_historial():
    try:
        with open("log_temperatura.txt", "r") as archivo:
            #Leemos las últimas 10 lineas para no colapsar el chat
            lineas = archivo.readlines()
            ultimas = lineas[-10:]
            return "".join(ultimas)
    except FileNotFoundError:
        return "El diario está vacío. ¡Todo ha ido bien hasta ahora!"
    
# Configuración del Bot
bot = telepot.Bot(config.TOKEN_TELEGRAM)
bot.message_loop(manejar_mensaje) # Aquí es donde se queda "escuchando"

print(" El Centinela Obediente está en marcha ...")

# Bucle infinito para que el script no se cierre

while True:
    t = obtener_temp()
    if t > 50.0:
        guardar_en_log(t)
        print("Log guardado con exito.")
        time.sleep(60)
    print(f"Temperatura actual: {t}")    
    time.sleep(1)