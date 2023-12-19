import os
from pathlib  import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(mesage)s:')

project_name = "cnn_classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    os.path.join('src',project_name,'__init__.py'),
    os.path.join('src',project_name,'components','__init__.py'),
    os.path.join('src',project_name,'utils','__init__.py'),
    os.path.join('src',project_name,'config','__init__.py'),
    os.path.join('src',project_name,'config','configuration.py'),
    os.path.join('src',project_name,'pipeline','__init__.py'),
    os.path.join('src',project_name,'entity','__init__.py'),
    os.path.join('src',project_name,'constants','__init__.py'),
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)

    # print(filedir,filename)

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(file_path) or (os.path.getsize(file_path)==0)):
        with open(file_path,'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")

    else:
        logging.info(f"{filename} already exists")
