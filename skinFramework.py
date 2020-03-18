class SkinFramework:
    def __init__(self,*args,**kwargs):
        self.x=1440
        self.y=1080
        self.numX=10
        self.numY=6
        self.cellX=int(self.x/self.numX)
        self.cellY=int(self.y/self.numY)
        self.y=self.y-self.cellY
        
        

    def setVR(self):
        pass


    def test(self):
        pass
        print(self.cellY)  

SkinFramework().test()     