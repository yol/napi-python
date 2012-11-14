from distutils.core import setup

setup(
    name='MaluubaNAPI',
    version='0.0.3',
    author='Maluuba',
    author_email='napi@maluuba.com',
    packages=['maluuba_napi'],
    url='http://developer.maluuba.com',
    license='LICENSE',
    description='A simple wrapper for consuming the Maluuba NLP API',
    long_description=open('README.md').read(),
    install_requires=[
        'requests >= 0.14.1'
    ]
)
