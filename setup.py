from setuptools import setup, find_packages


install_requires = [
    'aiohttp',
    'aiohttp_jinja2',
    'jinja2'
]

setup(
    name='tomscalculator',
    author='george',
    description='test task',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    data_files=[('templates', ['tomscalculator/templates/index.html'])],
    install_requires=install_requires,
    entry_points={"console_scripts": ['tomscalc = tomscalculator.main:main']}
)