import os
import shutil

for file in os.listdir():
    if file.endswith(".html") and file != "index.html":
        name = file[:-10] if file.endswith("index.html") else file[:-5]
        os.mkdir(name)
        shutil.move(file, os.path.join(name, "index.html"))
