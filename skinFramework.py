class SkinFramework:
    def __init__(self,*args,**kwargs):
        self.x=1440
        self.y=1080
        self.numX=10
        self.numY=6
        self.cellX=int(self.x/self.numX)
        self.cellY=int(self.y/self.numY)
        self.y=self.y-self.cellY
        self.numY=self.numY-1
        
        

    def setList26VR(self):
        list26VR=[]

        for numY in range(self.numY):
            for numX in range(self.numX):
                tupleVR=(numX*self.cellX,numY*self.cellY,self.cellX,self.cellY)
                if numY==3:
                    if numX==0:
                        tupleVR=(numX*self.cellX,numY*self.cellY,int(self.cellX*1.5),self.cellY)
                    elif numX==self.numX-1:
                        tupleVR=(int((numX-0.5)*self.cellX),numY*self.cellY,int(self.cellX*1.5),self.cellY)
                    elif numX==1:
                        continue
                    else:
                        tupleVR=(int((numX-0.5)*self.cellX),numY*self.cellY,self.cellX,self.cellY)
                elif numY==self.numY-1:
                    if numX==4:
                        tupleVR=(numX*self.cellX,numY*self.cellY,int(self.cellX*2),self.cellY)
                    elif numX>4:
                        continue

                list26VR.append(str(tupleVR)[1:-1])
        return list26VR
                

        


    def test(self):
        pass
        # print(self.listVR)

        print(len(self.setList26VR()))
        

sf=SkinFramework()
import pprint
pprint.pprint(sf.setList26VR())
sf.test()   