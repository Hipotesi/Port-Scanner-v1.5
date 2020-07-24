import socket
import subprocess
import sys
from datetime import datetime

# Limpiar la pantalla
subprocess.call('cls', shell=True)

# Preguntar por la IP
remoteServer = input("Escribe una IP remota para escanear: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Imprir una bonita pancarta con información sobre qué host estamos a punto de escanear
print("-" * 60)
print("Porfavor espera, escaneando el host remoto", remoteServerIP)
print("-" * 60)

# Compruebe a qué hora comenzó el escaneo
t1 = datetime.now()

# Usando la función de rango para especificar puertos (aquí escaneará todos los puertos entre 1 y 1024)

# También incluimos algunos manejos de errores para detectar errores

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Puerto {}: 	 Abrir".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Has presionado Ctr+C")
    sys.exit()

except socket.gaierror:
    print('El nombre de host no se pudo resolver. Saliendo')
    sys.exit()

except socket.error:
    print("No se puedo conectar con el servidor")
    sys.exit()

# Comprobando el tiempor otra vez
t2 = datetime.now()

#Calcula la diferencia de tiempo, para ver cuánto tiempo llevó ejecutar el script
total = t2 - t1

# Escribiendo la información en la pantalla
print('Escaneo Completo en: ', total)
