import os
import time
from datetime import datetime

contador = 0
limite = 5

print("El Notario Ciego empieza su turno...")

while contador < limite:
    ahora = datetime.now().strftime("%H:%M:%S")
    print (f"[{ahora}] Todo tranquilo en la Raspberry...")
    contador += 1
    time.sleep(3)
    
# Al salir del bucle (Salida limpia)
print("Turno terminado. Guardando acta...")

with open("diario_notario.txt", "a") as f:
    f.write(f"Turno completado el {datetime.now()}\n")
    
    