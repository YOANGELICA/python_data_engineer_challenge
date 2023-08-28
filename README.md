# python_data_engineer_challenge

## Cómo correr el repositorio

1. Clonar el repositorio 

    ```python
    git clone https://github.com/YOANGELICA/python_data_engineer_challenge
    ```

2. Instalar python 3.10.11

3. Instalar Mysql Server 8.0 y crear una base de datos.

4. Crear un entorno virtual

    `python -m venv [nombre]`

5. Activar el entorno

    `[nombre]/scripts/activate`

6. Instalar dependencias

    ```python
    pip install -r requirements.txt
    ```

7. Crear archivo de credenciales de base de datos db_config.json con el siguiente contenido:

    {
        "user":"",
        "password":"",
        "host":"",
        "server": "",
        "db":""
    }

8. Lanzar Jupyter y elegir el kernel asociado con el entorno virtual creado recientemente.

    ```python
    jupyter notebook
    ```