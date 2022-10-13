from  bank.client import Client
 
class Director:
     """
     A perso who directs the game.
     The resposibilirty of a Director is to control the sequence of Bank
     
     """   
     
     def __init__(self):
        
        self.client = False
        self.insiring_client = Client()
        self.outpput = OutputService()
        
        
        