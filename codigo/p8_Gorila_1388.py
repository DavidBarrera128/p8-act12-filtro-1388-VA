import cv2
# David Barrera NC = 1388
# Cargar la imagen
imagen = cv2.imread("Gorila.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen. Asegúrate de que 'Gorila.jpg' esté en el mismo directorio.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("original NC = 1388", imagen)
cv2.imshow("Filtro Gaussiano NC = 1388", imagen_suavizada)

# Guardar el resultado procesado
nombre_salida = "Gorila.jpg"  # Si prefieres guardarlo en la carpeta resultados, usa: "../resultados/Gorila.jpg"

cv2.imwrite(
    nombre_salida,
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print(nombre_salida)

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Imagen Gorila David Barrera NC = 1388")