# Ahorcado
Trabajo Práctico - Metodologías Ágiles

--------------------------------------

import os
import sys

# Archivo de bloqueo
lock_file = 'programa.lock'

# Ver si el archivo de bloqueo existe
if os.path.exists(lock_file):
    print("El programa ya está en ejecución.")
    sys.exit(1)  # Salir si ya está en ejecución

# Crear el archivo de bloqueo
with open(lock_file, 'w') as f:
    f.write("Este archivo indica que el programa está en ejecución.")

try:
    # Código principal del programa
    print("El programa se está ejecutando...")

finally:
    # Eliminar el archivo de bloqueo cuando termine la ejecución
    os.remove(lock_file)