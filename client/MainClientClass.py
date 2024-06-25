from ClientConnect import ClientСonnect

class MainClientClass(ClientСonnect):
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.send_data()


MCC = MainClientClass()
MCC.run()