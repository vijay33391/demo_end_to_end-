from setuptools import find_packages,setup  # find package for required 
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # when use the readlines  after reading the every line  it  add new line .for remove /n use list commerenceing replace /n with blank
        requirements=[req.replace("\n","") for req in requirements]

        # -e. also read by readline function. for removeing the -e.

        if HYPEN_E_DOT in requirements: # remove -e . for installation perpose in the requirements
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# meta data about the project 
setup(
name='mlproject',
version='0.0.1',
author='vijay',
author_email='pvijayavardhan@gmail.com',
packages=find_packages(),# useing  the module of find packages for install and build the package
install_requires=get_requirements('requirements.txt')

)

''' 
1. build src folder as package .

relation of setup.py and src folder explained below 

2.  (working)    when ever find find package  running . 
he just go and see how many folder have __init__.py file  for buliding package .
then he find out there is one folder called src . 
then build the src as package (aim as excuted)'''


'''
when ever trying to install the requeriment.txt  at same setup.py file so run for building the packages 
so use -e. (automatically trigger the setup.py when running the requeriments ) 
'''

'''
mlproject.egg-info is indicate your package is installed . your ready for deploy the package pyp
'''