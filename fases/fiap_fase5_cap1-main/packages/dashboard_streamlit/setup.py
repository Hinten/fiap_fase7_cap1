from setuptools import setup, find_packages

setup(
    name="dashboard_streamlit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.49.1",
        "SQLAlchemy==2.0.43",
        "database==0.1.0"
    ],
)