from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
]

setup(
    name='model',
    version='0.1',
    author = 'Madhu Maddikera',
    author_email = 'mmadhusankar@gmail.com',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Image model in Cloud ML Engine',
    requires=[]
)
