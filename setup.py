from setuptools import setup, find_packages

setup(
    name="orchestration",
    version="1.0",
    url="https://opensds.io",
    description="A service catalog manager for OpenSDS",
    author="OpenSDS Authors",
    author_email="Opensds-tech-discuss@lists.opensds.io",
    maintainer='Erik Xu',
    maintainer_email='lynheell@gmail.com',
    license="Apache 2.0",
    packages=find_packages(exclude=("tests", "tests.*")),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=[
        'six>=1.5.2',
        ],
)
