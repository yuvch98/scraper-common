from setuptools import setup, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="crawler_scraper_common_by_yuvch",  # Package name
    version="0.6.0",  # Version
    packages=find_packages(),  # Automatically find sub-packages
    install_requires=["requests", "beautifulsoup4"],  # Dependencies
    description="A shared library for web scraping utilities.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Yuval Chabra",  # Your name
    author_email="yuvalchabra100@gmail.com",  # Your email
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10"  # Minimum Python version
)
