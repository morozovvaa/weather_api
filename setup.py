from setuptools import setup, find_packages

setup(
    name='weather-api',
    version='0.1.0',
    description='Простой API для получения данных о погоде от OpenWeatherMap',
    author='Diana',
    author_email='diamorozov@gmail.com',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

