from setuptools import setup

setup(
    name='Heimdall_v0.1',
    version='0.1',
    packages=['Heimdall', 'Heimdall.plugins'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        Heimdall=Heimdall.main:main
    ''',
)
