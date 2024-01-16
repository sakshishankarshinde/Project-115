import os 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/HP/Downloads/main.txt"
dest = "C:/Users/HP/Downloads/newfile.txt"

result = os.rename(source,dest)

print("Source path renamed to destination path successfully")