# nexis

"Nexis" conveys the idea of a core system where various data sources converge. The project emphasizes the role of serving as a central hub for integrating and linking different data flows, processing data, analysis, and reporting. This name describes an advanced platform that organizes and synchronizes data from multiple sources into a consistent and insightful output.

This project has been developed to determine optimal prices in flight data by automatically examining the relationships between the variables of the data and reporting price predictions.

First, we fetch and organize our data (add departure and arrival date). We split the data and connect to PostgreSql by creating tables and transfering the split data into the tables, filling them up. Using the id variable of the tables, we merge them and obtain the data we want to work on.

We want to use the CrewAI platform to make price predictions. We define agents (analyst, writer) and their tasks (research_task, writer_task) and create a crew to get the results.

To improve the results, we use the vector database Qdrant. Our goal is to take the output from Crew, save it to this database, and then use these vectors to achieve better results. We create a collection named "Flight" and define vector parameters. By performing operations on the output, we create points containing vectors and upload the points. We perform a vector query to conduct our semantic search and obtain the result.



## Installation

### Docker ve Anaconda Container Kurulumu

1. **Docker'ı İndirin ve Kurun:**
   Docker'ı indirmek ve kurmak için [Docker Kurulumu](https://docs.docker.com/get-docker/) talimatlarını izleyin.

2. **Anaconda Container'ı Oluşturun:**
   Docker kullanarak Anaconda container'ını indirin ve çalıştırın:
   
   ```bash
   # Anaconda image'ini indirin ve container'ı başlatın
   docker run -i -t continuumio/anaconda3 /bin/bash
