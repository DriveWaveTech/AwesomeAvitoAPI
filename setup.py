from setuptools import setup, find_packages

setup(
    name="awesomeavitoapi",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.10.9',
        'pydantic==2.9.2',
        'loguru==0.7.2',
        'python-dateutil==2.9.0.post0',
    ],
    include_package_data=True,
    python_requires=">=3.11",
)
