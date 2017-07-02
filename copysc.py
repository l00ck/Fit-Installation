import shutil
import os
import configparser

class Copy:

    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("config.ini")
        self.source= parser.get('Files','sourcepath')
        self.destination=parser.get('Files', 'destinationpath')


#------- not in use ----------
    def makedir(self):
        if os.path.exists(self.destination):
            print("exist")
        else:
            os.makedirs(self.destination)
#------- not in use ----------



    def copyfile(self):

        if os.path.exists(self.destination):
            shutil.rmtree(self.destination)

        shutil.copytree(self.source,self.destination)


copy = Copy()
copy.copyfile()