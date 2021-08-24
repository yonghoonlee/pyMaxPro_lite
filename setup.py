import os
from setuptools import find_packages
from numpy.distutils.core import setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "pymaxpro_lite")

about = {}
with open(os.path.join(src_dir, "__about__.py")) as f:
    exec(f.read(), about)

pkgs = find_packages()

if __name__ == "__main__":
    metadata = dict(
            name = about["__title__"],
            version = about["__version__"],
            description = about["__description__"],
            author = about["__author__"],
            license = about["__license__"],
            url = about["__uri__"],
            packages = pkgs,
            install_requires = ['numpy', 'scipy'],
            python_requires = '>=3.6',
    )
    setup(**metadata)

