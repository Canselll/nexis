from pandas import DataFrame
from crewai import Crew ,Process
from ..data.dao.postgres_dao import SaveIntoPostgres , LoadFromPostgres
from ..config.process.parser import config
from .VIP.agents import CreateAgencs
from .VIP.tasks import CreateTasks
from .VIP.embedding import Vectorize
from ..data.dao.sql_query_dao import query


class Apply(SaveIntoPostgres,LoadFromPostgres,
            CreateAgencs,CreateTasks,Vectorize):
    
    def apply_data_processing(self):

        rows = self.load_entity_from_postgres(query = query, data = (config["DATES"]['start date'],config["DATES"]['end date']))

        df = DataFrame(rows , columns= config["COLUMNS"])

        return df


    def apply_crew_kick_off(self , df):

        analyst = self.create_analyst_agent()
        writer  = self.create_write_agent()
        research_task = self.create_research_task(analyst ,df)
        write_task = self.create_write_task(writer,expected_output=self.vectorize_text('flights'))
        

        crew = Crew(
                    agents=[analyst, writer],
                    tasks=[research_task, write_task],
                    verbose=0,
                    process=Process.sequential  
        )

        result = crew.kickoff()

        return result
    

  
