from setuptools import setup, find_packages

setup(
    name="code_to_text",
    version="0.1",
    packages=find_packages(include=['code_to_text', 'code_to_text.*']),
    description="Extracts and combines all code from a project into a markdown or txt file.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="David van der Byl",
    author_email="your.email@example.com",
    url="https://github.com/David-vanderByl/code_to_text.git",
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
            'all_code=code_to_text.main:main',
        ],
    },
)
