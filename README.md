# python_data_engineer_challenge
In this project, we are going to analze, manipulate and visualize data from candidates who participated in recruitment processes.

The main goal is to gather some useful insights about the tendencies in hiring processes for candidates from multiple countries. We have a randomly generated CSV file from which we will get the information from, but first, it's needed to analyze, manipulate and migrate the data to a relational database with tools like MySQL, SQLAlchemy, Pandas and Matplotlib.

## Tools used

**Database management:** SQLAlchemy was used to make queries, create the database model and migrate the data into a MySQL database.
**Visualization:** Pandas to store the result of the queries along with Matplotlib to generate the graphics for this repository.

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

8. Launch Jupyter and choose the kernel associated with the recently created virtual environment.

    ```python
    jupyter notebook
    ```
 
## Author
Maria Angelica Portocarrero Quintero