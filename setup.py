from setuptools import setup, find_packages

setup(
    name="pyorgandosimetryicrp",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        'pyorgandosimetryicrp': [
            'svalues/*.csv',
            'svalues/README.md',
            'examples/*.csv'
        ],
    },
    install_requires=[
        'numpy>=1.20.0',
        'pandas>=1.2.0',
        'scipy>=1.6.0',
    ],
    author="devhliu, claude 3.5, gemini 2.0 flash reasoning",
    author_email="huiliu.liu@gmail.com",
    description="Internal radiation dosimetry calculation package based on OLINDA 2.0",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devhliu/PyOrganDosimetryICRP",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires='>=3.8',
)