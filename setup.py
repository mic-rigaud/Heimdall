from setuptools import setup

setup(
    name='Strawberry_v0.1',
    version='0.1',
    packages=['Strawberry', 'Strawberry.plugins', 'Strawberry.lib'],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        heimdall=Strawberry.main:main
    ''',
)
