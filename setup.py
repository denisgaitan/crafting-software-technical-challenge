from setuptools import find_packages, setup
from crafting import __version__

setup(
    name="crafting",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Technical challenge solution inquired by Crafting Software team",
    author="Denis Gaitan",
    author_email="denis.gaitan@yahoo.com",
)
