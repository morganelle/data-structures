"""Setup for data structures."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov', 'tox']
}

setup(
    name='Data structures',
    description='Python implementation of various data structures.',
    version='0.1',
    author='Sean Beseler, Morgan Nomura',
    author_email='seanwbeseler@gmail.com, morganelle@gmail.com',
    license='MIT',
    py_modules=['bst'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)
