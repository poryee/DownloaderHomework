from setuptools import find_packages, setup

setup(
    name='PyDownloader',
    version='1.0.0',
    description='program to download data from multiple sources and protocols to local disk',
    author='Por Yee',
    author_email='poryee1@hotmail.com',
    license='UNLICENSE',

    keywords='cli',
    python_requires='>=3.5',
    test_suite="tests",
    packages=find_packages(exclude=['docs', 'tests1*']),

    install_requires=['requests', 'tqdm', 'paramiko'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-mock'],
    entry_points={
        'console_scripts': [
            'downloader=downloader.cli:main',
        ],
    }
)
