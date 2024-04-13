from setuptools import setup, find_packages

setup(
    name='robotframework-TrainingREST',
    version='0.1.2',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires = [
        'setuptools',
        'robotframework',
        'lxml'
    ],
    author='Artur Ziółkowksi',
    author_email='artur.k.ziolkowski@gmail.com',

)
