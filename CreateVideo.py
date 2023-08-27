import os
import cv2

# Ruta del origen
print("Cambia la ruta de la carpeta de las imagenes")
path = "D:/BYJUS_FUTURE_SCHOOL/python/tareas/ACTIVIDAD C117/images"

# Variable
images = []

# Comprueba los archivos en la carpeta
for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.png', '.jpeg', '.gif', '.jfif']:
        file_name = os.path.join(path, file)
        print(file_name)
        images.append(file_name)

# Cuenta los archivos en la carpeta
count = len(images)

# Crear el objeto VideoWriter
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Agregar las imágenes al video
for i in range(count):
    img = cv2.imread(images[i])
    if img is not None:
        cv2.imshow('album', img)  # Mostrar imagen en ventana emergente
        out.write(img)
        cv2.waitKey(2000)  # Esperar 200 ms antes de mostrar la siguiente imagen
    else:
        print(f"Error al cargar la imagen: {images[i]}")

# Liberar el objeto VideoWriter, cerrar ventanas y mensaje de fin
out.release()
cv2.destroyAllWindows()
print("Fin")