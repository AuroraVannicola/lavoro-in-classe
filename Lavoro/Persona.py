class Persona:
    def __init__(self, n:str, c:str, r:int):
        self.nome       =   n
        self.cognome    =   c
        self.colonnascelta= r
    def info(self)->str:
        return str(self.nome) +" " +self.cognome+" " +self.colonnascelta
   