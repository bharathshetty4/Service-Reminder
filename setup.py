from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'reminder/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()


setup(
    name='reminder',
    version=version,
    description='A Service to keep track of vehicle service date',
    long_description=open('README.md').read(),
    author='Bharath Kumar',
    author_email="shettybharath4@gmail.com",
    maintainer='Bharath Kumar',
    maintainer_email='shettybharath4@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['service-reminder=reminder.commands.launch:execute']
    },
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
    ],
)
