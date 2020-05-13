import sys
import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import re
import shutil
class FileUtility:

    def get_extention(self,name):
        file_name = name.split('/')[-1]
        separated_name = file_name.split('.')
        extention = separated_name[-1]
        filename = file_name.split('.')[0]
        return extention,filename
        
    def place_file(self,name):
        extention,filename = self.get_extention(name)
        get_current_directory = os.getcwd()
        os.chdir('/home/rahul/Downloads/')
        if extention == 'crdownload':
            pass
        else:
            file_props = filename.split('_')
            target_folder = file_props[0]
            rename_file = file_props[-1]
            print('The file needs to be named {} and placed in {}'.format(rename_file, target_folder))
            dirs = os.listdir('.')
            os.rename('{}.{}'.format(filename,extention),'{}.{}'.format(rename_file,extention))
            new_file_name = '{}.{}'.format(rename_file,extention)
            if target_folder in dirs:
                shutil.move('/home/rahul/Downloads/{}'.format(new_file_name),'/home/rahul/Downloads/{}/{}'.format(target_folder,new_file_name))
            else:
                os.mkdir('/home/rahul/Downloads/{}'.format(target_folder))
                shutil.move('/home/rahul/Downloads/{}'.format(new_file_name),'/home/rahul/Downloads/{}/{}'.format(target_folder,new_file_name))
        os.chdir(get_current_directory)
        
    def set_file_name(self,name,path):
        index = 1


class FileHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        fu = FileUtility()
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            file_path = event.src_path
            fu.place_file(file_path)
        elif event.event_type == 'modified':
            print('File modified {}'.format(event.src_path))

class OnMyWatch:
    watch_directory = '/home/rahul/Downloads'

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = FileHandler()
        self.observer.schedule(event_handler,self.watch_directory)
        self.observer.start()
        try:
            while True:
                time.sleep(10)
        except:
            self.observer.stop()
            print('Observer Stopped')
        self.observer.join()

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
    