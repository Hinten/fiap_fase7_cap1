from setuptools import setup, find_packages

setup(
    name="database",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "greenlet==3.2.4",
        "numpy==2.3.2",
        "pandas==2.3.2",
        "python-dateutil==2.9.0.post0",
        "pytz==2025.2",
        "six==1.17.0",
        "SQLAlchemy==2.0.43",
        "typing_extensions==4.15.0",
        "tzdata==2025.2",
        "matplotlib==3.10.6",
    ],
)