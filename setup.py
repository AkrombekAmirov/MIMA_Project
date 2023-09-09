from setuptools import setup, find_packages

setup(
    name='backend',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
       "fastapi",
       "uvicorn==0.23.2",
       "SQLAlchemy==1.4.41",
       "sqlmodel==0.0.8",
       "pydantic==2.3.0",
        "python-environ==0.4.54",
        "python-dotenv==1.0.0"
    ],
    authors='Akrom Amirov',
    license='MIT',
)
