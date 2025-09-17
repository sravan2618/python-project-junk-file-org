import os.path, time
import shutil

class orgbyDate:
    def __init__(self,path):
        self.current_dir = path

    def moveFiles(self):
        for file in os.listdir(self.current_dir):

            self.file_path = os.path.join(self.current_dir,file)

            # To get last modified date and time
            self.modified_time = os.path.getmtime(self.file_path)
            self.convert_time = time.localtime(self.modified_time)
            self.file_date = time.strftime('%d'+'-'+'%m'+'-'+'%Y', self.convert_time)

            self.current_filepath = os.path.join(self.current_dir,file)

            self.to_filepath = os.path.join(self.current_dir,self.file_date)
            self.to_path = os.path.join(self.to_filepath,file)

            # If folder not present already create one
            if not os.path.isdir(self.to_filepath):
                os.mkdir(self.to_filepath)
            shutil.move(self.current_filepath,self.to_path)
