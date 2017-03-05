""" setup.py """

from setuptools import setup

setup(
    name="metabolitepo",
    packages=["metabolitepo"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
