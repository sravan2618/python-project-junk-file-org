import os
import shutil
import constants

class orgbyType:
    def __init__(self,path):
        self.current_dir = path

    def moveFiles(self):
        for file in os.listdir(self.current_dir):

            self.file_ext = (os.path.splitext(file)[1][1:].lower())
            
            self.current_filepath = os.path.join(self.current_dir,file)

            if self.file_ext in constants.DOCUMENTS:
                self.to_filepath = os.path.join(self.current_dir,'Documents')
                self.to_path = os.path.join(self.to_filepath, file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)
            
            if self.file_ext in constants.AUDIO:
                self.to_filepath = os.path.join(self.current_dir,'Audio')
                self.to_path = os.path.join(self.to_filepath, file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)

            if self.file_ext in constants.VIDEOS:
                self.to_filepath = os.path.join(self.current_dir,'Video')
                self.to_path = os.path.join(self.to_filepath, file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)

            if self.file_ext in constants.IMAGES:
                self.to_filepath = os.path.join(self.current_dir,'Images')
                self.to_path = os.path.join(self.to_filepath, file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)

            if self.file_ext in constants.COMPRESSED:
                self.to_filepath = os.path.join(self.current_dir,'Compressed Files')
                self.to_path = os.path.join(self.to_filepath, file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)

            if self.file_ext in constants.SOFTWARE:
                self.to_filepath = os.path.join(self.current_dir,'Software')
                self.to_path = os.path.join(self.to_filepath, file)
                if not os.path.isdir(self.to_filepath):
                    os.mkdir(self.to_filepath)
                shutil.move(self.current_filepath,self.to_path)
