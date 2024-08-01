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
   - Download and install Docker by following the instructions provided at [Docker Installation](https://docs.docker.com/get-docker/).

2. **Create and Run Anaconda Container:**
   - Pull the Anaconda image from Docker Hub and start a container:
   
   ```bash
   # Download the Anaconda image and start the container
   docker run -i -t continuumio/anaconda3 /bin/bash

   ```bash

conda update conda
conda create --name abr python= 3.10.8
conda activate abr

