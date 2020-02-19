import os
from setuptools import setup, find_packages


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


README = local_file('README.rst')

setup(
    name="src",
    version='0.0.1',
    description='Library for building grafana dashboards',
    long_description=open(README).read(),
    url='https://github.com/filipve1994/grafanabuilddashboardswithpython',
    author='FVE',
    author_email='help@fve.com',
    license='Apache',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
    ],
    install_requires=[
        'attrs==19.2',
    ],
    extras_require={
        'dev': [
            'flake8',
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'generate-dashboard=src._gen:generate_dashboard_script',
            'generate-dashboards=src._gen:generate_dashboards_script',
        ],
    },
)
