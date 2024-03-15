from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:  ##create func to read requirements.txt file using file_path
    requirements=[]
    with open(file_path) as file_obj:       ##open file_path
        requirements=file_obj.readlines()   ##read file line by line using file_obj
        requirements=[req.replace("\n","") for req in requirements]     ##replace \n from requirements.txt file


        if HYPEN_E_DOT in requirements:         ##remove -e . from requirements.txt file
            requirements.remove(HYPEN_E_DOT)


    return requirements




setup(
    name='RegressorProject',
    version='0.0.1',
    author='sneha',
    author_email='snehawaydande@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)