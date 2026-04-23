from setuptools import setup,find_packages
from typing import List


def get_requirements(file_path:str)->List[str]: 
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements

setup(
name='ml_project',
version='0.1',
author='verma',
packages=find_packages(),
install_requires=['numpy','pandas']




)