from setuptools import setup, find_packages

from cf_pinning import __version__

setup(
    name='conda-forge-pinning',
    version=__version__,
    description='A package that defines version pinning for conda-forge feedstocks',
    author='Christian Roth',
    author_email='christian.roth@mpibpc.mpg.de',
    url='https://github.com/croth1/conda-forge-pinning',
    packages=find_packages(),
    test_suite='nose.collector',
    include_package_data=True,
    zip_safe=False,
)
