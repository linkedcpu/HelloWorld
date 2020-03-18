import configparser
import os
class Css:
    def __init__(self,*args,**kwargs):
        if len(args)==0:
            self.__targetPath=r'D:\skins\test\port\res\default.css'
        else:
            self.__targetPath=args[0]
        



    def readCss(self,path):
        strPath=os.path.join(self.__targetPath,path)
        print(strPath)

        parser=configparser.RawConfigParser()
        parser.optionxform=str
        parser.read(strPath,encoding='utf-8')
        initNum=0
        for section in parser.sections():
            if 'GLOBAL' not in section:
                print(section)
                for option in parser[section]:
                    if 'SHOW' in option:
                        print(parser[section][option]) 
            # if parser.has_option(section,'SHOW')==False:
            #     initNum+=1
            #     # print(parser.options(section))
            #     print(parser[section])
            #     print(initNum)

    def setPy9(self):
        pass




__targetPath=r'D:\skins\test\port\gen.ini'
__targetPath=r'D:\skins\test\port'

Css(__targetPath).readCss('res\default.css')