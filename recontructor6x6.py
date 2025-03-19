import matplotlib.pyplot as plt
import numpy as np

# Definir los patrones
fig1 = [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 
        1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1]
fig2 = [1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 
        -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1]
fig4 = [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 
        -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1]
fig3 = [1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 
        1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1]

fila = []
matriz = [[1 if i == j else 0 for j in range(36)] for i in range(36)]

newfig = []
newfig2 = []
newfig3 = []
matrizaprendizaje = []
cont = 0
cont2 = 0

# Calcular pesos para fig1
for i in range(len(fig1)):
    fila = []
    for j in range(len(fig1)): 
        valor = fig1[i] * fig1[j] - matriz[i][j]
        fila.append(valor)
        cont += 1
    newfig.append(fila)

# Calcular pesos para fig2
for i in range(len(fig2)):
    fila = []
    for j in range(len(fig2)): 
        valor = fig2[i] * fig2[j] - matriz[i][j]
        fila.append(valor)
        cont2 += 1
    newfig2.append(fila)

# Calcular pesos para fig4
for i in range(len(fig4)):
    fila = []
    for j in range(len(fig4)): 
        valor = fig4[i] * fig4[j] - matriz[i][j]
        fila.append(valor)
    newfig3.append(fila)

# Sumar pesos para matrizaprendizaje
for i in range(len(newfig)):
    fila = []
    for j in range(len(newfig[i])):
        valor = newfig[i][j] + newfig2[i][j] + newfig3[i][j]
        fila.append(valor)
    matrizaprendizaje.append(fila)

# Proceso de reconocimiento con fig3
resultado = [0] * 36
for i in range(len(fig3)):
    suma = 0
    for j in range(len(fig3)):
        suma += fig3[j] * matrizaprendizaje[j][i]
    resultado[i] = 1 if suma > 0 else -1 if suma < 0 else fig3[i]

# Función para convertir lista 1D a matriz 6x6 y mostrarla
def mostrar_imagen(vector, titulo):
    matriz_imagen = np.array(vector).reshape(6, 6)
    plt.imshow(matriz_imagen, cmap='gray_r', vmin=-1, vmax=1)
    plt.title(titulo)
    plt.axis('off')

# Crear una figura con subplots para mostrar todas las imágenes
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
mostrar_imagen(fig1, "Figura 1 (Patrón almacenado)")

plt.subplot(2, 2, 2)
mostrar_imagen(fig2, "Figura 2 (Patrón almacenado)")

plt.subplot(2, 2, 3)
mostrar_imagen(fig4, "Figura 4 (Patrón almacenado)")  # Corregido: mostrar fig4

plt.subplot(2, 2, 4)  # Corregido: posición 4 en lugar de 5
mostrar_imagen(fig3, "Figura 3 (Entrada)")

# Añadir resultado en una nueva figura o subplot adicional si deseas
plt.figure(figsize=(6, 6))  # Nueva figura para el resultado
mostrar_imagen(resultado, "Resultado reconocimiento")

plt.tight_layout()
plt.show()

# Imprimir resultados en consola también
print("Patrón de entrada (fig3):", fig3)
print("Resultado reconocimiento:", resultado)