from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(include=['my_package', 'my_package.*', 'tests', 'tests.*']),
    description="Extracts and combines all code from a project into a markdown or txt file.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pygments',
    ],
    entry_points={
        'console_scripts': [
            'my_package=my_package.main:main',
        ],
    },
)
