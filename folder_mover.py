import shutil
import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

root = tk.Tk()
root.withdraw()

# Open a file dialog box to select a folder path
folder_path = filedialog.askdirectory()

# Print the selected folder path
print(folder_path)
timestamp_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
timestamp_str = timestamp_str.split('-')
timestamp_str = ''.join(timestamp_str)


print(timestamp_str)

# Set the source and destination folder paths
src_folder = folder_path

# Use os.makedirs() to create the subfolder
subfolder_path = os.path.join('D:/fgg', timestamp_str)
# os.makedirs(subfolder_path)

# Use shutil.move() to move the folder and its contents to the new location
shutil.copytree(src_folder, subfolder_path)


