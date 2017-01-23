from setuptools import setup, find_packages

__VERSION__ = '2017.1.23'

setup(
    name='conda-forge-pinning',
    version=__VERSION__,
    description='A package that defines version pinning for conda-forge feedstocks',
    author='Christian Roth',
    author_email='christian.roth@mpibpc.mpg.de',
    url='https://github.com/croth1/conda-forge-pinning',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
