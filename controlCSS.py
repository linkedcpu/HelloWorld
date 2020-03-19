import configparser
import os
import pprint
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


    def set26SCS(self):
        import variable
        strStyle='STYLE'
        targetPath=r'D:\skins\test\port\res\default.css'
        list26SCS=variable.list26SCS
        parser=configparser.RawConfigParser()
        parser.optionxform=str
        parser.read(targetPath,encoding='utf-8')
        flag=0
        for section in parser.sections():
            if section.startswith(strStyle):
                tmp=int(section[len(strStyle):])
                if flag<tmp:
                    flag=tmp
        print(flag)
        for i in range(len(list26SCS)):
            # print(i)
            strSection=strStyle+str(flag+i+1)
            if strSection in parser.sections():
                print('已存在,请检查')
                exit()
            parser[strSection]={
                'SHOW':list26SCS[i],
                'NM_COLOR':'ffffff',
                'HL_COLOR':'ffffff',
                'FONT_SIZE':'56'
                }
            with open ('test.css','w',encoding='utf-8') as file:
                parser.write(file)
            
            # for options in parser[strSection]:
            #     print(parser[strSection][options])
        # print(list26SCS)

    def setPy9(self):
        pass




__targetPath=r'D:\skins\test\port\gen.ini'
__targetPath=r'D:\skins\test\port'

# Css(__targetPath).readCss('res\default.css')
css=Css()
css.set26SCS()