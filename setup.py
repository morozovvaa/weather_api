from setuptools import setup

setup(
    name='weather_api',
    version='0.1.0',
    description='Простой API для получения данных о погоде от OpenWeatherMap',
    author='Diana',
    author_email='diamorozov@gmail.com',
    packages=['weather_api'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

