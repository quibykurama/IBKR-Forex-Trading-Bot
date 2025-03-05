from setuptools import setup, find_packages

setup(
    name='trading_bot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'numpy',
        'psycopg2-binary',
        'ib_insync',
        'matplotlib',
        'scipy',
        'pytest',
        'jupyter',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'run_bot=run_bot:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Automated trading bot with customizable strategies',
    url='https://github.com/yourgithubusername/trading-bot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
