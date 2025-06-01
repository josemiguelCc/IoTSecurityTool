# IoTSecurityTool
# Escáner de Vulnerabilidades con Flask y Nmap

Este proyecto es una aplicación web desarrollada con **Flask** que utiliza **Nmap** para escanear objetivos en red, identificar puertos abiertos y detectar vulnerabilidades conocidas (CVE) usando el script `vulners`.  

---

## Tabla de Contenidos

1. [Descripción]
2. [Características]
3. [Tecnologías Utilizadas]
4. [Estructura del Proyecto]
5. [Requisitos Previos]
6. [Instalación y Configuración]
    1. [Clonar el Repositorio]
    2. [Crear y Activar un Entorno Virtual]
    3. [Crear `requirements.txt`]
    4. [Instalar Dependencias]
    5. [Verificar Instalación de Nmap]
7. [Uso]
    1. [Ejecutar la Aplicación] 
    2. [Acceder a la Interfaz Web]
    3. [Escanear un Objetivo]
8. [Notas y Advertencias] 
9. [Mejoras Futuras]
10. [Créditos] 
11. [Licencia] 

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

