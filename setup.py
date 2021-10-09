from setuptools.command.install import install
from setuptools import setup, find_packages
import setuptools
import subprocess
import os

class InstallCommand(install):
    def run(self):
        install.run(self)
        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        create_service_script_path = os.path.join(current_dir_path, 'setup.sh')
        subprocess.check_output([create_service_script_path])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    
    name='streamlit-basic',
    version='1.0.0',
    author='tomioke',
    author_email='tomiirvan@gmail.com',
    description='Belajar membuat streamlit web apps',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomioke/streamlit-basic-title",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={'install': InstallCommand}
)