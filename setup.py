from setuptools import setup

setup(
    name='Heimdall_v0.1',
    version='0.1',
    packages=['Heimdall', 'Heimdall.plugins', 'Heimdall.lib'],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        heimdall=Heimdall.main:main
    ''',
)
