# nexis

"Nexis" conveys the idea of a core system where various data sources converge. The project emphasizes the role of serving as a central hub for integrating and linking different data flows, processing data, analysis, and reporting. This name describes an advanced platform that organizes and synchronizes data from multiple sources into a consistent and insightful output.

This project has been developed to determine optimal prices in flight data by automatically examining the relationships between the variables of the data and reporting price predictions.

First, we fetch and organize our data (add departure and arrival date). We split the data and connect to PostgreSql by creating tables and transfering the split data into the tables, filling them up. Using the id variable of the tables, we merge them and obtain the data we want to work on.

We want to use the CrewAI platform to make price predictions. We define agents (analyst, writer) and their tasks (research_task, writer_task) and create a crew to get the results.

To improve the results, we use the vector database Qdrant. Our goal is to take the output from Crew, save it to this database, and then use these vectors to achieve better results. We create a collection named "Flight" and define vector parameters. By performing operations on the output, we create points containing vectors and upload the points. We perform a vector query to conduct our semantic search and obtain the result.


## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Troubleshooting & FAQ](#troubleshooting--faq)
6. [Maintainers](#maintainers)

## Requirements

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Anaconda**: [Install Anaconda](https://docs.anaconda.com/anaconda/install/)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- **PostgreSQL**: Ensure PostgreSQL is set up for database management.
- **CrewAI**: Required for price prediction using AI agents.
- **Qdrant**: Vector database for improved search results.

## Recommended Modules

- **Pandas**: For data manipulation.
- **SQLAlchemy**: For SQL database interaction.
- **Qdrant-client**: For managing vectors in Qdrant.

## Installation

### Docker and Anaconda Container Installation

1. **Install Docker:**
   - Download and install Docker by following the instructions at [Docker Installation](https://docs.docker.com/get-docker/).

2. **Create and Run Anaconda Container:**
   - Pull the Anaconda image from Docker Hub and start a container:

       ```bash
        docker run -d \
        --name anaconda \
        -p 8888:8888 \
        -p 8000:8000 \
        -v /path/to/your/local/directory:/home/jovyan/anaconda \
        jupyter/pyspark-notebook
     ```

     **Note:** The above command runs the container in detached mode (`-d`), names the container `anaconda`, maps ports 8888 and 8000, and mounts the local directory to `/home/jovyan/anaconda` inside the container. Make sure to replace `/path/to/your/local/directory` with the actual path to your local directory.


3. **Set Up the Anaconda Environment:**
   - Inside the container, update `conda` and create a new environment:

     ```bash
     conda update conda
     conda create --name nexis python=3.10.8
     conda activate nexis
     ```

4. **Install Project Dependencies:**
   - Access the container and install dependencies:

     ```bash
     docker exec -it container_id bash
     cd /home/project_directory
     pip install -r requirements.txt
     ```

5. **Set Up PostgreSQL:**
   - Run PostgreSQL in a Docker container:

     ```bash
     docker run --name postgres-container \
         -e POSTGRES_PASSWORD=your_password \
         -p 5432:5432 \
         -v postgres-data:/var/lib/postgresql/data \
         -d postgres
     ```

     **Note:** Replace `your_password` with a secure password of your choice.

    - After starting the PostgreSQL container, connect to it and set up your database and tables. Here’s how you can set up the database and tables:

     ```bash
     docker exec -it postgres-container psql -U postgres
     ```

   - In the PostgreSQL prompt, create your database:

     ```sql
     CREATE DATABASE your_database;
     \c your_database
     ```

   - Create tables by running the following SQL script. Below is an example script you might use (adjust according to your project requirements):

     ```sql
     -- Create the tables
     CREATE TABLE airline_table (
                                id SERIAL PRIMARY KEY,
                                airline VARCHAR NOT NULL
                            );

     -- Create the classes_table
     CREATE TABLE classes_table (
                                id SERIAL PRIMARY KEY,
                                class VARCHAR NOT NULL
                            );

     -- Create the flight_table
     CREATE TABLE flight_table (
                                id SERIAL PRIMARY KEY,
                                flight VARCHAR NOT NULL,
                                source_city VARCHAR NOT NULL,
                                stops VARCHAR NOT NULL,
                                destination_city VARCHAR NOT NULL,
                                duration FLOAT,
                                days_left INTEGER,
                                price INTEGER,
                                departure_date TIMESTAMP,
                                arrival_date TIMESTAMP
                            );
                            
    ```




## Configuration

1. **Database Configuration:**
   - Update the `base.py` file with your PostgreSQL connection details:

     ```python
     POSTGRES = {
         'user': 'postgres',
         'password': 'your_password',
         'host': 'postgres',
         'port': 5432,
         'dbname': 'your_database'
     }
     ```
     
## Usage

1. **Run the Project:**
   - Execute the main script to make price predictions:

     ```bash
     python app.py --key ''  --env dev
     ```

2. **Review Results:**
   - Check the `result.txt` file for the predictions.

## Troubleshooting & FAQ

- **Issue: Docker container fails to start.**
  - **Solution:** Ensure Docker is correctly installed and running. Check for errors in the Docker logs.

- **Issue: Dependencies not installing properly.**
  - **Solution:** Verify your `requirements.txt` file is correctly formatted. Ensure you are in the correct environment.

- **Issue: Database connection errors.**
  - **Solution:** Double-check your PostgreSQL configuration details and ensure the database server is running.

## Maintainers

- **Your Name** - *Project Lead* - [Your GitHub Profile](https://github.com/YourGitHubProfile)

- **Contributor Name** - *Contributor* - [Contributor GitHub Profile](https://github.com/ContributorGitHubProfile)

