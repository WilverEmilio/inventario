# 📦 Sistema de Inventario para Negocio

Este proyecto tiene como objetivo llevar un control efectivo del inventario de un negocio, permitiendo realizar un seguimiento detallado de los productos disponibles, así como del stock de cada uno.



---

## 🧱 Estructura del Proyecto

Este sistema está dividido en dos partes independientes:

### 📱 Aplicación Móvil (Frontend)
- **Tecnología:** React Native  
- **Funcionalidad:** Muestra los datos del inventario y permite realizar acciones como agregar, editar o eliminar productos mediante peticiones al backend.

### 🖥️ Backend (este repositorio)
- **Tecnología:** FastAPI  
- **Funcionalidad:** Gestiona la base de datos y responde a las solicitudes provenientes de la aplicación móvil.

> ⚠️ **Nota:** La aplicación móvil será desarrollada en un proyecto separado para evitar complicaciones al momento de desplegar en un servidor.

---

## 🧰 Tecnologías Utilizadas

| Área               | Tecnología        |
|--------------------|-------------------|
| Aplicación Móvil   | React Native      |
| Backend            | FastAPI           |
| Base de Datos      | MySQL Workbench   |
| Diseño de UI       | Figma             |

---

## 👨‍💻 Desarrollador

**Wilver Emilio Xiá Ixcot** – Desarrollador Full Stack  
🗓️ **Duración estimada del proyecto:** 4 meses

---

## 📫 Contacto

- 📧 Email: [ixcotwilver@gmail.com](mailto:ixcotwilver@gmail.com)  
- 💼 LinkedIn: [Wilver Emilio Xiá Ixcot](https://www.linkedin.com/in/wilver-emilio-xia/)  
- 🐱 GitHub: [WilverEmilio](https://github.com/WilverEmilio)

---

## ⚙️ Cómo levantar el proyecto (Backend - FastAPI)

### ✅ Requisitos previos

- Python 3.10+
- MySQL Workbench
- Git y pip
- (Opcional) Entorno virtual con `venv`

### 📥 Clonar repositorio

```bash
git clone https://github.com/WilverEmilio/inventario.git
cd inventario
```

### Crear entorno virtual
⚠️ **Nota:** Si no deseas usar un entorno virtual, puedes omitir este paso y continuar con la instalación de dependencias directamente. Sin embargo, se recomienda utilizar un entorno virtual para evitar conflictos entre dependencias de diferentes proyectos.

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac 

#Para activar el entorno virtual en Windows
.venv\Scripts\Activate.ps1    # PowerShell
.venv\Scripts\activate.bat   # CMD
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar base de datos
1. Abre MySQL Workbench y crea una nueva base de datos llamada `inventario`.
2. Levantar el proyecto con el siguiente comando:
⚠️ **Nota:** Crea la base de datos automaticamente, si no existe. 
```bash
uvicorn main:app --reload
```

## Licencia
Este proyecto está bajo la Licencia MIT.

## Contribuciones
Si deseas contribuir a este proyecto, no dudes en abrir un issue o pull request. Todas las contribuciones son bienvenidas.

## Derechos de autor
Este proyecto es de propiedad de Wilver Emilio Xiá Ixcot. Todos los derechos reservados.


Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\Scripts\Activate.ps1