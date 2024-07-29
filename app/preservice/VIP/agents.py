from crewai import Agent

class CreateAgencs():
    def create_analyst_agent(self):

        analyst = Agent(
                        role='Veri Analisti',
                        goal='Verilen veri kümesi hakkında detaylı analiz yap ve veri ile ilgili bilgileri araştır.',
                        backstory="""
                        Sen uzman bir araştırmacısın. 
                        Araştırma yaparken İngilizce kullanıyorsun.
                        Teknik konulara hakimsin. 
                        Belirli bir veri kümesi hakkında derinlemesine bilgi toplaman gerekiyor.
                        """,
                        verbose=False,
                        allow_delegation=False
                        )
      
        return analyst

    def create_write_agent(self):

        writer = Agent(
                        role='Raporlayıcı',
                        goal='Araştırmacının sağladığı bilgileri kullanarak en yüksek geliri elde edebilmek için uçak fiyatları nasıl belirlenmelidir hangi parametreler daha etkilidir yorumlamalar yap.',
                        backstory="""
                        Sen uzman bir fiyat raporlayıcısısın. 
                        Teknik konulara hakimsin. 
                        Teknik ve bilgilendirici içerik üretmek senin uzmanlık alanın.
                        Olabildiğince kısa ve anlaşılır cümleler kuruyorsun.
                        Eğer kullanacağın bilgilerde eksikler varsa, araştırmacıya soruyorsun.
                        """,
                        verbose=False,
                        allow_delegation=False  

                    )
        return writer
        