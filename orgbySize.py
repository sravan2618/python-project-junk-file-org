import os
import shutil

class orgbySize:
    def __init__(self,path):
        self.current_dir = path

    def moveFiles(self):
        for file in os.listdir(self.current_dir):

            self.file_path = os.path.join(self.current_dir,file)
            self.file_size = os.path.getsize(self.file_path)
            self.file_size_kbs = round(self.file_size/1024)
            print(self.file_size_kbs)

            self.current_filepath = os.path.join(self.current_dir,file)

            if self.file_size_kbs <= 100:
                self.to_filepath = os.path.join(self.current_dir,'Below 100KB')
                self.to_path = os.path.join(self.to_filepath,file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)
            
            elif self.file_size_kbs > 100 and self.file_size_kbs <= 100000:
                self.to_filepath = os.path.join(self.current_dir,'100KB to 100 MB')
                self.to_path = os.path.join(self.to_filepath,file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)

            elif self.file_size_kbs > 100000 and self.file_size_kbs <= 1000000:
                self.to_filepath = os.path.join(self.current_dir,'100MB to 1GB')
                self.to_path = os.path.join(self.to_filepath,file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)
            
            elif self.file_size_kbs > 1000000:
                self.to_filepath = os.path.join(self.current_dir,'More than 1GB')
                self.to_path = os.path.join(self.to_filepath,file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)
