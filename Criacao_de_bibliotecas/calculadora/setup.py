from setuptools import setup, find_packages

setup(
    name='calculadora',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['numpy==2.1.2'],  # Dependências da biblioteca
    description='Uma biblioteca para calculos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Salvador Netto',
    author_email='salvv.netto@gmail.com',
    url='https://github.com/salvnetto/calculadora',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)