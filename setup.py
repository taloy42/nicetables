from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='NiceTable',
    url='https://github.com/jladan/package_demo',
    author='Tal Levi',
    author_email='anukhehpus@gmail.com',
    # Needed to actually package something
    packages=['Ntable','build_table_help'],
## Needed for dependencies
#install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='taloy42',
    description='makes tables readable by a human',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
