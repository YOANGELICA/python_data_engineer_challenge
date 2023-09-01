# Python Data Engineer Challenge
Welcome to the Python Data Engineer Challenge. In this project, we are going to analyze, manipulate and visualize data from candidates who participated in recruitment processes.

The main goal is to gather some useful insights about the tendencies in hiring processes for candidates from multiple countries. We have a randomly generated CSV file from which we will get the information from, but first, it's needed to analyze, manipulate and migrate the data to a relational database with tools like MySQL, SQLAlchemy, Pandas and Matplotlib.

## Tools used

- **SQLAlchemy:** Used to make queries, create the database model and migrate the data into a MySQL database.

- **Pandas:** Pandas was used to explore the dataset and store the results of the queries.

- **Matplotlib:** Was used to generate the graphics for this repository.

## Dataset

This project uses an artificially generated dataset that emulates data from candidates who participated in recruitment processes.
It has 50k rows and originally contains the following columns:

- First Name
- Last Name
- Email
- Application Date
- Country
- YOE (years of experience)
- Seniority
- Technology
- Code Challenge Score
- Technical Interview Score

## How to run this project

1. Clone the repository

    ```python
    git clone https://github.com/YOANGELICA/python_data_engineer_challenge
    ```

2. Install python 3.x

3. Install Mysql Server 8.0 and create a database.

4. Create a virtual environment.
   
    ```python
    python -m venv [your_env]
    ```
6. Activate said environment

    ```python
    [your_env]/scripts/activate
    ```
7. Install dependencies

    ```python
    pip install -r requirements.txt
    ```
    
8. Create database credentials file 'dg_config.json' with the following content:
      ```
      {
        "user": "your_username",
        "password": "your_password",
        "host": "your_host"
        "server": "your_server",
        "db": "your_database"
      }
      ```

    > **Note:** This file is necessary, by not having it you won't be able to access the database unless you state the credentials directly (not recommended). If you choose to give it a different name or location, you must change the the access route in the code.
    > 

9. Launch Jupyter and choose the kernel associated with the recently created virtual environment.

    ```python
    jupyter notebook
    ```
 
## Author
Maria Angelica Portocarrero Quintero
