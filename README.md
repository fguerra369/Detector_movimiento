🎥 Detector de Movimiento y Rostros en Python
---
🔹 Descripción

Este proyecto permite detectar **movimiento** usando la cámara de tu computadora y, opcionalmente, detectar **rostros** dentro del área de movimiento usando **OpenCV**.  
Ideal para aprendizaje de **visión por computadora**, sistemas de **monitoreo** o **proyectos de seguridad**.  

---
🗂 Estructura del proyecto

detector-movimiento/

├─ detector_movimiento.py # Script principal

├─ README.md # Este archivo

├─ .gitignore # Archivos que Git ignora

└─ assets/ 

---
🛠 Requisitos

- **Python 3.x** (recomendado 3.9 o superior)  
- **OpenCV**

Instalar OpenCV:

pip install opencv-python

> ⚠️ No uses `opencv-python-headless` si quieres que las ventanas de la cámara funcionen en Windows.

---
🚀 Ejecución paso a paso

1. Clonar el repositorio:

git clone https://github.com/fguerra369/detector-movimiento.git

2. Entrar a la carpeta del proyecto:

cd detector-movimiento

3. Ejecutar el script:

python detector_movimiento.py

4. Observa la ventana de la cámara:  
   - 🟩 Rectángulos verdes: movimientos detectados  
   - 🟦 Rectángulos azules: rostros detectados (opcional)  

5. Presiona **`q`** para cerrar la ventana.

---
⚙️ Cómo funciona

1. **Captura de video**: se toma un frame inicial como referencia.  
2. **Detección de movimiento**:  
   - Se compara el frame actual con el anterior.  
   - Filtra movimientos pequeños para evitar falsos positivos.  
   - Dibuja rectángulos verdes sobre movimientos significativos.  
3. **Detección de rostros**:  
   - Usa un clasificador Haar dentro del área de movimiento.  
   - Dibuja rectángulos azules sobre los rostros detectados.

---

💡 Consejos para principiantes
- Ajusta `cv2.contourArea(contour) > 2000` para cambiar sensibilidad al movimiento.  
- Puedes usar la carpeta `assets/` para imágenes o videos de prueba.  
- Mantén tu proyecto bajo control de versiones con Git y súbelo a GitHub.  

---
👨‍💻 Sobre el autor

**Fabián Guerra**  
- Ingeniero Informático | Python & Data Analysis  
- GitHub: [fguerra369](https://github.com/fguerra369)  
- Contacto: opcional (https://www.linkedin.com/in/fabi%C3%A1n-guerra-512608245/)  

---
📌 Licencia
Este proyecto es **educativo y de uso personal**. Puedes adaptarlo para aprendizaje o pruebas.  
---

<img width="477" height="358" alt="Visbilidad" src="https://github.com/user-attachments/assets/0de630ca-1409-456b-b9d6-5423141552fb" />

