from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in iqraa/__init__.py
from iqraa import __version__ as version

setup(
	name="iqraa",
	version=version,
	description="Iqraa",
	author="Jabir",
	author_email="jabir@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
