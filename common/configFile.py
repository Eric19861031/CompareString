
class Myfile:

    fullpath = ''
    file = None

    def __init__(self,path,name,type):
        self.fullpath = path + name + '.'+type

    def open_W(self):
        self.file = open(self.fullpath,'w')

    def fclose(self):
        file.close()