#this is for installing the localpackages like QAwithPDF in the current virtual environment

from setuptools import find_packages, setup

setup(
    name='QApplication',
    version='0.0.1',
    author='nikita',
    author_email='nikitaarora4521@gmail.com',
    packages=find_packages(), #this is used to automaticalaly discover all packages in cwd. This means it will look for all directories that contain an __init__.py file and include them in the package.
    install_requires=[] #there are no external dependencies.
)

#this package can be installed in the current virtual environment. 