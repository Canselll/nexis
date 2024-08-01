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
- **Scikit-learn**: For machine learning tasks.
- **SQLAlchemy**: For SQL database interaction.
- **Qdrant-client**: For managing vectors in Qdrant.

## Installation

### Docker and Anaconda Container Installation

1. **Install Docker:**
   - Download and install Docker by following the instructions at [Docker Installation](https://docs.docker.com/get-docker/).

2. **Create and Run Anaconda Container:**
   - Pull the Anaconda image from Docker Hub and start a container:

     ```bash
     docker run -i -t continuumio/anaconda3 /bin/bash
     ```

3. **Set Up the Anaconda Environment:**
   - Inside the container, update `conda` and create a new environment:

     ```bash
     conda update conda
     conda create --name nexis_env python=3.10
     conda activate nexis_env
     ```

4. **Install Project Dependencies:**
   - Copy your project files into the container:

     ```bash
     docker cp ./project_directory container_id:/home/project_directory
     ```

   - Access the container and install dependencies:

     ```bash
     docker exec -it container_id /bin/bash
     cd /home/project_directory
     pip install -r requirements.txt
     ```

5. **Set Up PostgreSQL:**
   - Ensure PostgreSQL is running and create tables using SQL scripts:

     ```bash
     psql -h localhost -U postgres -d your_database
     \i create_tables.sql
     \i load_data.sql
     ```

6. **Configure CrewAI and Qdrant:**
   - Set up CrewAI and Qdrant according to their documentation:

     ```bash
     qdrant-client create-collection --name Flight --vector-size 300
     qdrant-client upload-vectors --collection Flight --vectors /path/to/vectors
     ```

## Configuration

1. **Database Configuration:**
   - Update the `database_config.py` file with your PostgreSQL connection details:

     ```python
     DATABASE = {
         'host': 'localhost',
         'port': 5432,
         'user': 'postgres',
         'password': 'your_password',
         'database': 'your_database'
     }
     ```

2. **CrewAI Configuration:**
   - Configure your CrewAI agents and tasks in `crewai_config.py`:

     ```python
     CREWAI = {
         'agents': ['analyst', 'writer'],
         'tasks': ['research_task', 'writer_task']
     }
     ```

3. **Qdrant Configuration:**
   - Define vector parameters and collection settings in `qdrant_config.py`:

     ```python
     QDRANT = {
         'collection_name': 'Flight',
         'vector_size': 300
     }
     ```

## Usage

1. **Run the Project:**
   - Execute the main script to make price predictions:

     ```bash
     python app.py --input data.txt --output result.txt
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

