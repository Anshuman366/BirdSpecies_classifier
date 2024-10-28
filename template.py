import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s :')

package_name = "BirdSpecies_Classifier"

list_of_files=[
    ".github/workflows/.gitkeep" ,## .gitkeep will hwlp in uploading the empty files or folders into github
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"

]

for filepaths in list_of_files:
    filepaths=Path(filepaths)
    filedir,filename=os.path.split(filepaths)
    if filedir!="":
        # creating directory
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory created at {filedir} for file {filename}")
    if (not os.path.exists(filepaths)) or (os.path.getsize(filepaths)==0):
        with open(filepaths,"w") as f:
            pass ## creating empty file
            logging.info(f" file created with name {filepaths}")
    else:
        logging.info(f"{filename} already exists")