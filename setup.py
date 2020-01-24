import os

from setuptools import setup

readme_path = os.path.join(os.path.dirname(__file__), "README.rst")
with open(readme_path) as fp:
    long_description = fp.read()

setup(
    name='timeoutthreadpoolexecutor',
    version='1.0.0',
    url='https://github.com/JohnDoee/timeoutthreadpoolexecutor',
    author='Anders Jensen',
    author_email='andersandjensen@gmail.com',
    description='A backported ThreadPoolExecutor with thread TTL',
    long_description=long_description,
    license='MIT',
    py_modules=['timeoutthreadpoolexecutor'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
