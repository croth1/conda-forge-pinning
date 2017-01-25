Overview
--------

`conda-forge-pinning` is a python package that defines and imports conda-forge dependency pinnings.


[![Build Status](https://travis-ci.org/croth1/conda-forge-pinning.svg)](https://travis-ci.org/croth1/conda-forge-pinning)


Pinning syntax
--------------

`cf_pinning/pinning.json` defines the pins in a dictionary format. The key is the package name, the value can either be a version string or a list of two version strings. In the latter case, the first version string represents the build dependency, the second sets the run dependency.

Examples
--------

~~~
 "fontconfig":"2.12.*",
~~~

 Pin `fontconfig` to version `2.12.*` in both the build and the run dependency section.

 ~~~
 "freetype": ["2.7", "2.7|2.7.*"]
 ~~~

 Depend on `freetype 2.7` in the build dependency section; pin the run dependency to an arbitrary patch version of `freetype 2.7`.
