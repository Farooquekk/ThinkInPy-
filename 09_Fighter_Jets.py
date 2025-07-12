class Fighter_Jets:
    name=''
    country=''
    gen=0.0
    speed=0

    def __init__(self,name,country,gen,speed):
        self.name = name
        self.country = country
        self.gen = gen
        self.speed = speed

    @staticmethod 
    def greet():
        print('Welcome User, see the different Fighter Jets.')

    def getInfo(self):
        print('\nName : ',self.name,'\nCountry : ',self.country,'\nGen : ',self.gen, '\nSpeed : ',self.speed)

j35 = Fighter_Jets('J35','China',5,2400)
f35 = Fighter_Jets('F35','USA',5,2300)
jf_17 = Fighter_Jets('JF_17_thunder','Pak',4.5,2200)
rafael = Fighter_Jets('Dassult Rafeal','France',4.5,2150)
j35.greet()
j35.getInfo()
f35.getInfo()
jf_17.getInfo()
rafael.getInfo()