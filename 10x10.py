import matplotlib.pyplot as plt
import numpy as np

# Definir los patrones (convertimos 0 a -1 y mantenemos 1 como 1)
fig1 = [-1 if x == 0 else 1 for x in [
    0,0,1,1,1,1,1,1,0,0,
    0,1,0,0,0,0,0,0,1,0,
    1,0,0,0,0,0,0,0,0,1,
    1,0,1,0,0,0,0,1,0,1,
    1,0,1,0,0,0,0,1,0,1,
    1,0,0,0,0,0,0,0,0,1,
    1,0,1,0,0,0,0,1,0,1,
    1,0,0,1,1,1,1,0,0,1,
    0,1,0,0,0,0,0,0,1,0,
    0,0,1,1,1,1,1,1,0,0
]]

fig2 = [-1 if x == 0 else 1 for x in [
    0,0,1,1,1,1,1,1,0,0,
    0,1,0,0,0,0,0,0,1,0,
    1,0,0,0,0,0,0,0,0,1,
    1,0,0,1,0,0,1,0,0,1,
    1,0,0,1,0,0,1,0,0,1,
    1,0,0,0,0,0,0,0,0,1,
    1,0,0,0,1,1,0,0,0,1,
    1,0,0,1,0,0,1,0,0,1,
    0,1,0,0,0,0,0,0,1,0,
    0,0,1,1,1,1,1,1,0,0
]]

fig3 = [-1 if x == 0 else 1 for x in [
    0,0,1,1,1,1,1,1,0,0,
    0,1,0,0,0,0,0,0,1,0,
    1,0,0,0,0,0,0,0,0,1,
    1,0,1,0,0,0,0,1,0,1,
    1,0,0,1,0,0,1,0,0,1,
    1,0,1,0,0,0,0,1,0,1,
    1,0,0,0,0,0,0,0,0,1,
    1,0,0,1,1,1,1,0,0,1,
    0,1,0,0,0,0,0,0,1,0,
    0,0,1,1,1,1,1,1,0,0
]]

# Matriz identidad de 10x10 (100 elementos)
matriz = [[1 if i == j else 0 for j in range(100)] for i in range(100)]

newfig = []
newfig2 = []
newfig3 = []
matrizaprendizaje = []

# Calcular pesos para fig1
for i in range(len(fig1)):
    fila = []
    for j in range(len(fig1)): 
        valor = fig1[i] * fig1[j] - matriz[i][j]
        fila.append(valor)
    newfig.append(fila)

# Calcular pesos para fig2
for i in range(len(fig2)):
    fila = []
    for j in range(len(fig2)): 
        valor = fig2[i] * fig2[j] - matriz[i][j]
        fila.append(valor)
    newfig2.append(fila)

# Calcular pesos para fig3 (como patrón almacenado)
for i in range(len(fig3)):
    fila = []
    for j in range(len(fig3)): 
        valor = fig3[i] * fig3[j] - matriz[i][j]
        fila.append(valor)
    newfig3.append(fila)

# Sumar pesos para matrizaprendizaje
for i in range(len(newfig)):
    fila = []
    for j in range(len(newfig[i])):
        valor = newfig[i][j] + newfig2[i][j] + newfig3[i][j]
        fila.append(valor)
    matrizaprendizaje.append(fila)

# Proceso de reconocimiento con fig3 (como entrada)
resultado = [0] * 100
for i in range(len(fig3)):
    suma = 0
    for j in range(len(fig3)):
        suma += fig3[j] * matrizaprendizaje[j][i]
    resultado[i] = 1 if suma > 0 else -1 if suma < 0 else fig3[i]

# Función para convertir lista 1D a matriz 10x10 y mostrarla
def mostrar_imagen(vector, titulo):
    matriz_imagen = np.array(vector).reshape(10, 10)
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
mostrar_imagen(fig3, "Figura 3 (Patrón almacenado y Entrada)")

plt.subplot(2, 2, 4)
mostrar_imagen(resultado, "Resultado reconocimiento")

plt.tight_layout()
plt.show()

# Imprimir resultados en consola también
print("Patrón de entrada (fig3):", fig3)
print("Resultado reconocimiento:", resultado)