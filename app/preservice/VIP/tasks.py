from crewai import Task

class CreateTasks():

    def create_research_task(self,analyst,df):
        
        research_task = Task(
                            description=f"""Verilen veri kümesi ({df}) hakkında detaylı analiz yap ve konuyu araştır.""",
                            expected_output='Mevsim, uçak tipi , uçuş süresi gibi değişkenlerle fiyatlar arasındaki ilişkinin yorumlanması',
                            agent=analyst,
                            verbose=False
                        )
        
        return research_task
    
    def create_write_task(self,writer,expected_output):
        
        write_task = Task(
                        description=f"""Araştırmacının sağladığı bilgileri kullanarak bilgilendirici ve uzman diliyle yazılmış bir açıklama metini yaz. 
                        Metin, her değişken arasındaki ilişki için olası optimal fiyat aralıklarını vermeli ve sebeplerini açıklamalıdır.
                        """,
                        expected_output = expected_output,
                        agent=writer,
                        verbose=False
                    )
        
        return write_task
