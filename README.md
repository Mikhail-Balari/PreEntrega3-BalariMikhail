# Mi Proyecto Django

Este es un proyecto Django que incluye las siguientes características:

- Herencia de HTML
- Tres clases en el modelo: Producto, Categoría y Orden
- Formulario para insertar datos en cada clase de modelo
- Formulario de búsqueda para buscar productos en la base de datos

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **mi_proyecto**: Carpeta principal del proyecto Django.
    - **mi_aplicacion**: Aplicación Django creada para este proyecto.
        - **migrations**: Carpeta que contiene las migraciones de la base de datos.
        - **templates/mi_aplicacion**: Carpeta que contiene los archivos HTML de la aplicación.
            - `resultados_busqueda.html`: Plantilla para mostrar los resultados de la búsqueda.
            - `buscar_producto.html`: Plantilla para el formulario de búsqueda de productos.
            - `exito.html`: Plantilla para mostrar un mensaje de éxito después de guardar los datos.
            - `insertar_datos.html`: Plantilla para el formulario de inserción de datos.
        - `forms.py`: Archivo que define los formularios de la aplicación.
        - `models.py`: Archivo que define los modelos de datos de la aplicación.
        - `urls.py`: Archivo que define las URL de la aplicación.
        - `views.py`: Archivo que define las vistas de la aplicación.
    - `settings.py`: Archivo de configuración principal del proyecto.
    - `urls.py`: Archivo que define las URL del proyecto principal.
    - `wsgi.py` y `asgi.py`: Archivos de configuración para el servidor web.
- `db.sqlite3`: Base de datos SQLite utilizada para el proyecto.
- `manage.py`: Script de administración de Django.

## Uso

Para utilizar este proyecto, asegúrate de tener Python y Django instalados en tu entorno de desarrollo. Luego, puedes clonar este repositorio y ejecutar el servidor Django con el siguiente comando:

`python manage.py runserver`

Después de ejecutar el servidor, puedes acceder a las siguientes URL para interactuar con la aplicación:

- Inserción de datos: [http://localhost:8000/insertar-datos/](http://localhost:8000/insertar-datos/)
- Búsqueda de productos: [http://localhost:8000/buscar-producto/](http://localhost:8000/buscar-producto/)

## Colaboración

Si deseas colaborar en este proyecto, ¡siéntete libre de hacer un fork y enviar tus pull requests!



