# IoTSecurityTool
# Escáner de Vulnerabilidades con Flask y Nmap

Este proyecto es una aplicación web desarrollada con **Flask** que utiliza **Nmap** para escanear objetivos en red, identificar puertos abiertos y detectar vulnerabilidades conocidas (CVE) usando el script `vulners`.  

---

## Descripción

Esta aplicación web proporciona una interfaz sencilla sobre Flask para ejecutar escaneos de red usando Nmap. Permite:

- Ingresar una dirección IP (o rango) desde un navegador.
- Realizar un escaneo completo de puertos (`-p-`).
- Detectar servicios y versiones (`-sV`).
- Ejecutar el script `vulners` para buscar posibles vulnerabilidades (CVE) asociadas a los servicios detectados.
- Mostrar los resultados agrupados por IP y puerto, con información clave de cada vulnerabilidad encontrada.

Está pensada para entornos controlados o educativos. No debe usarse en redes ajenas sin autorización.

---

## Características

- **Interfaz Web con Flask**: formulario web para ingresar objetivos y mostrar resultados en formato legible.  
- **Escaneo Completo de Puertos**: utiliza `nmap -p-` para descubrir todos los puertos abiertos.  
- **Detección de Servicios y Versiones**: agrega la opción `-sV`.  
- **Análisis de Vulnerabilidades**: ejecuta el script `--script vulners` de Nmap para identificar CVE relevantes.  
- **Salida Agrupada**: información organizada por IP → puerto → servicio → posibles CVEs.  

---

## Tecnologías Utilizadas

- **Python 3.x**  
- **Flask**  
- **python-nmap** (wrapper de Nmap en Python)
- **ExploitDB** (base de datos de exploits, instalada como herramienta de línea de comandos) 
- **Nmap** (instalación nativa en el sistema)  
- **HTML + Jinja2** (para plantillas)  

---

## Estructura del Proyecto

```plaintext
PI/
├── .venv/                  # Entorno virtual (no rastreado por Git)
├── main.py                 # Archivo principal de la aplicación Flask
├── requirements.txt        # Lista de dependencias de Python
├── templates/
│   ├── index.html          # Formulario para ingresar la IP/rango
│   └── resultado.html      # Muestra resultados del escaneo
└── static/                 # (Opcional) Archivos CSS, JS, imágenes, etc.
```


## Requisitos Previos

Antes de instalar y ejecutar la aplicación, asegúrate de tener instalado lo siguiente en tu sistema:

1. **Git**  
   - Para clonar el repositorio.  
   - Verifica con:
     ```bash
     git --version
     ```

2. **Python 3**  
   - Para ejecutar la aplicación Flask.  
   - Verifica con:
     ```bash
     python3 --version
     ```
   - Si en tu sistema el comando es `python`, usa `python --version`.

3. **pip**  
   - El gestor de paquetes de Python para instalar dependencias.  
   - Verifica con:
     ```bash
     pip --version
     ```

4. **Virtualenv** (opcional pero recomendado)  
   - Para aislar las dependencias del proyecto en un entorno virtual.  
   - Si no lo tienes, instala con:
     ```bash
     pip install virtualenv
     ```

5. **Nmap**  
   - Herramienta de escaneo de red que utiliza la aplicación.  
   - En Linux (Debian/Ubuntu):
     ```bash
     sudo apt update
     sudo apt install nmap
     ```
   - En macOS (Homebrew):
     ```bash
     brew install nmap
     ```
   - En Windows:
     1. Descarga e instala desde https://nmap.org/download.html  
     2. Asegúrate de agregar la ruta de `nmap.exe` al PATH.  
   - Verifica con:
     ```bash
     nmap --version
     ```

6. **exploitdb**  
   - Base de datos de vulnerabilidades pública  
   - En Linux (Debian/Ubuntu):
     ```bash
     sudo apt update
     sudo apt install exploitdb
     ```
     -Verificamos con
     ```bash
     searchsploit --version
     ```
     

---

## Cómo Descargar e Instalar

Sigue estos pasos **en el orden indicado**:

1. **Clonar el repositorio desde GitHub**  
   Abre tu terminal y ejecuta:
   ```bash
   git clone https://github.com/josemiguelCc/IoTSecurityTool
   cd IoTSecurityTool
2. **Crear y activar entorno virtual**  
   Abre tu terminal y ejecuta:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
2. **Instalar dependencias**  
   Abre tu terminal y ejecuta:
   ```bash
   pip install Flask
   pip install python-nmap
2. **Inicializar el programa**  
   Abre tu terminal y ejecuta:
   ```bash
   python3 main.py
