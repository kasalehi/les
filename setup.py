from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as f:
        line=f.readline()
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        if line!='-e .':
            requirements.remove('-e .')
    return requirements
                    
                    
                    
setup(
    name='ml projects',
    version='0.0.1',
    author='keyvan salehi',
    author_email='ksalehi@yahoo.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)                   