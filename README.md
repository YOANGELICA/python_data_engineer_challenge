# python_data_engineer_challenge

It is expected to analyze, manipulate and visualize data from candidates who participated in recruitment processes.

## How to run this project

1. Clone the repository

    ```python
    git clone https://github.com/YOANGELICA/python_data_engineer_challenge
    ```

2. Install python 3.10.11

3. Install Mysql Server 8.0 y create a database.

4. Create a virtual environment

    `python -m venv env`

5. Activate said environment

    `env/scripts/activate`

6. Install dependencies

    ```python
    pip install -r requirements.txt
    ```

7. Create database credentials file 'dg_config.json' with the following content:

    {
        "user":"",
        "password":"",
        "host":"",
        "server": "",
        "db":""
    }

> **Note:** This file is necessary, by not having it you won't be able to access the database unless you state the credentials directly (not recommended). If you choose to give it a different name or location, you must change the the access route in the code.
> 

8. launch Jupyter and choose the kernel associated with the recently created virtual environment.

    ```python
    jupyter notebook
    ```