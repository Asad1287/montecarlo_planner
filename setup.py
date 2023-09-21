from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name="monte_carlo_planner",  
    version="0.1",
    author="Asad Zaman",
    author_email="asadali047@gmail.com",
    description="Run Monte Carlo simulations for financial planning, capital planning, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asad1287/montecarlo_planner"
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.7',
)

