# Proyecto: Bitácora de Consumo de Agua

**Autor(a): ASHLEY ANNABELLE CARRERA RUIZ 
**Curso:** Lógica de Programación – Paso 1 y Paso 2


Este proyecto es un ejemplo **simple** para cumplir el *Paso 1* y *Paso 2* del deber de **Lógica de Programación**. Incluye:
- Código en Python con **estructuras lógicas** (`if/elif/else`) y **estructuras repetitivas** (`while` y `for`).
- **Diagrama de flujo** en formato Mermaid (`flowchart.mmd`) que puedes visualizar en GitHub o VS Code.
- Archivos listos para subir a **GitHub**.

> Requisitos: Windows 10/11, conexión a Internet, una cuenta en GitHub.

### Posición del estudiante (Paso 1)
Elegí este tema porque me permite practicar condicionales y bucles con datos numéricos simples, sin distraerme con interfaces gráficas. Priorizo claridad y trazabilidad del flujo en consola. Reconozco como límite la falta de persistencia automática; la dejo como mejora futura (CSV/JSON).
### Conclusiones y logros (Paso 1)
- Logré un menú funcional con validación de entradas y comparación con meta.
- El repositorio público contiene código, diagrama y README con mi reflexión.
- Próximo paso priorizado: guardar y recargar datos automáticamente.



---

## 0) Instalar herramientas (una sola vez)
1. **Python 3.11+**: https://www.python.org/downloads/ (marca la casilla *Add Python to PATH* durante la instalación).
2. **Git**: https://git-scm.com/downloads
3. **Visual Studio Code**: https://code.visualstudio.com/ (recomendado instalar la extensión *Python* y *Markdown Preview Mermaid Support*).

## 1) Ejecutar el programa
1. Descarga este proyecto y descomprímelo.
2. Abre la carpeta en VS Code.
3. Abre una terminal en VS Code (``Ctrl+` ``) y ejecuta:
   ```bash
   python main.py
   ```
4. Sigue el **menú interactivo** y registra datos de consumo de agua para varios días. Prueba también definir una **meta** para activar la **alerta**.

## 2) Ver el **diagrama de flujo**
- Abre `flowchart.mmd` en VS Code. Si instalaste *Markdown Preview Mermaid Support*, presiona `Ctrl+Shift+V` para previsualizar.
- Alternativa: Sube el archivo a GitHub; GitHub renderiza Mermaid automáticamente en Markdown/`.mmd`.

## 3) Preparar **GitHub** y subir tu avance
1. Crea una cuenta: https://github.com (si no tienes).
2. Crea un repositorio nuevo llamado, por ejemplo, `logica-programacion` (marca **Add a README** si quieres, no es obligatorio).
3. Copia la URL del repositorio (ej.: `https://github.com/usuario/logica-programacion.git`).
4. En la terminal, dentro de esta carpeta del proyecto, ejecuta (reemplaza la URL por la tuya):
   ```bash
   git init
   git add .
   git commit -m "Primer avance: código + diagrama"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/logica-programacion.git
   git push -u origin main
   ```

## 4) Entregables sugeridos en tu GitHub
- `main.py` (avance de codificación)
- `flowchart.mmd` (diagrama de flujo)
- `README.md` (instrucciones para ejecutar)
- (Opcional) `demo.gif` o `capturas/` con pantallazos del programa corriendo

## 5) Video explicativo (requisito del trabajo)
- **Windows**: presiona `Win+G` (Xbox Game Bar) para grabar la pantalla.
- O usa **OBS Studio**: https://obsproject.com/
- Qué mostrar en el video (2-5 min):
  1. El repositorio en GitHub con el **código** y **diagrama**.
  2. Ejecutar el programa y demostrar:
     - registro de consumos,
     - cálculo de promedio,
     - meta/alerta,
     - salidas del menú.
  3. Explicar brevemente el diagrama de flujo.

## 6) Cómo este proyecto cumple los requisitos técnicos
- **Estructuras lógicas**: uso de `if/elif/else` para validar entradas y activar alertas.
- **Estructuras repetitivas**: `while True` para el menú y `for`/`sum` para cálculos.
- **Comentarios**: en las partes más “complejas” (validaciones y cálculos) verás comentarios detallados.
- **Diagrama de flujo**: describe el flujo principal del menú.

> Sugerencia para tu reflexión final: Comenta por qué elegiste el tema (p. ej., gestión de agua), qué aprendiste de condicionales y bucles, y qué mejorarías (p. ej., exportar a CSV o guardar datos persistentes).

---

© 2025 Estudiante.
