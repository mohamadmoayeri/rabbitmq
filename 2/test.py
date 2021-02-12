

class filemanager:

    def __init__(self,filename,mode):

        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):

        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_val,exc_tb):

        self.file.close()
        print(f'type:{exc_type}')
        print(f'value:{exc_val}')
        print(f'Traceback:{exc_tb}')
        return 2

with filemanager('hello.txt','r') as f:

    for i in f:
        print(i)
    

