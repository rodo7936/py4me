from setuptools import setup, find_packages

setup(
    name='py4me',
    version='0.0.1a',
    license='MIT',
    url='https://github.com/rodo7936/py4me',
    description='Python SDK for 4me API',
    keywords=['4me', 'api', 'py4me', 'sdk', '4me api', 'python 4me', '4me python', '4me sdk'],
    python_required='>=3.7',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    long_description='Python SDK for 4me API',
    author='rodo7936 - Patryk Szczepański',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
    ],

)
