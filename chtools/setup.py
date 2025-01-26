from setuptools import setup, find_packages

setup(
    name='chtools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='daveG',
    author_email='scubamut@gmail.com',
    description='A package to interact with the UK Companies House API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/scubamut/companies-house-project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: ubuntu',
    ],
    python_requires='>=3.10'
)