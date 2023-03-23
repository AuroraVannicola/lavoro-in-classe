from Persona import Persona
class IO:
    def acqPersona():
      s=Persona("")
      s.nome=input("Nome: ")
      s.cognome=input("Cognome. ")
      s.colonnascelta= input("colonna scelta ")   
      return s
    def visualizzacolonne(colonnaVincente):
        print(colonnaVincente())
    def visualizzaListaColonneRimaste(lista):
        index=0
        for x in lista:
            index+=1
            print(index())

   