'''packing the ml models'''
from setuptools import setup, find_packages
HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    '''this function will return the list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

'''packing the ml models'''
from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''this function will return the list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject_1',
    version='0.1',
    author='Sunnyttc',
    author_email='sunnyttc@umich.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
