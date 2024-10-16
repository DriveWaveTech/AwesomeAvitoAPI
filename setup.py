import setuptools

setuptools.setup(
    include_package_data=True,
    name='AwesomeAvitoAPI',
    version='0.2.13',
    description='Awesome async library for working with AvitoAPI!',
    url='https://github.com/Irrenriel/AwesomeAvitoAPI',
    author='Irrenriel',
    packages=setuptools.find_packages(),
    install_requires=[
        'aiohttp>=3.10.9',
        'pydantic>=2.9.2',
        'loguru>=0.7.2',
        'python-dateutil>=2.9.0.post0',
    ],
    long_description='Awesome async library for working with AvitoAPI!',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)