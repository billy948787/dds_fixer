import tkinter as tk
from tkinter import filedialog
import threading
from wand import image

def convert_dds_file(path):
    print(f"Converting {path}...")
    with image.Image(filename = path) as img:
        img.compression = "dxt1"
        img.save(filename = path)
    print(f"Converted {path}")
    

def convert_dds_files():

    root = tk.Tk()
    root.withdraw()
    
    file_paths = filedialog.askopenfilenames(
        title="Select DDS files to convert",
        filetypes=[("DDS Files","*.dds")]
    )

    threads = []
    for path in file_paths:
        t = threading.Thread(target=convert_dds_file, args=(path,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    convert_dds_files()