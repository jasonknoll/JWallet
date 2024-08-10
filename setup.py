from setuptools import setup, find_packages

setup(
    name='jwallet',
    version='0.1.13',
    packages=find_packages(),
    
    #entry_points={
     #   'console_scripts': [
      #      'jwallet=jwallet.jwallet',
     #   ],
    #},
    install_requires=[
        "web3",
        "argparse",
        "python-dotenv",
        "bitcoinlib",
        "eth-account"
    ],
    python_requires='>=3.8',  # Adjust based on your needs
    author='Jason Knoll',
    author_email='jknolldev@gmail.com',
    description='A CLI crypto wallet generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jasonknoll/jwallet',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
