import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='idpay',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    author='Amir Koulivand',
    author_email='vispa.amir@gmail.com',
    license='GPLv3',
    description='Python package for payment API of IDPay gateway.',
    url='https://github.com/vispamir/python-idpay',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python'
    ],
)
