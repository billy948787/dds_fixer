# DDS Fixer

DDS Fixer is a tool for batch converting DDS files. This tool uses Python and Tkinter for file selection and the Wand library for image processing.

## Installation

Before using this tool, you need to install the necessary Python libraries. Run the following command to install the Wand library:

```sh
pip install wand
```

You also need to ensure that the C++ header files are set up correctly. This can be done by selecting the "Install development headers for C and C++" option during the ImageMagick installation and installing the necessary development tools and libraries for your operating system.

## Usage

1. Run the `dds_fixer.py` script.
2. Select the DDS files you want to convert in the file selection dialog that appears.
3. The program will automatically convert the selected files and save them.

## Code

Here is the code for `dds_fixer.py`:

```python
import tkinter as tk
from tkinter import filedialog
import threading
from wand import image

def convert_dds_file(path):
    print(f"Converting {path}...")
    with image.Image(filename=path) as img:
        img.compression = "dxt1"
        img.save(filename=path)
    print(f"Converted {path}")

def convert_dds_files():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select DDS files to convert",
        filetypes=[("DDS Files", "*.dds")]
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
```

## Notes

- Ensure that you have installed ImageMagick and that its executables are added to your system's PATH environment variable.

For any issues, please refer to the [ImageMagick documentation](https://imagemagick.org/script/index.php) or the [Wand documentation](https://docs.wand-py.org/).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
