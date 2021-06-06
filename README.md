# smart_gardening_system

Smart gardening system using Raspberry Pi

# Requirement

## Hardware

* Raspberry Pi Zero WH
* Grove Base HAT for Raspberry Pi
* Grove Temperature & Humidity Sensor
* Grove TDS Sensor

## Software

* grove 0.6
* ambient-python-lib
 
# Installation

* grove

```bash
$ curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
```

* ambient-python-lib

```bash
$ sudo pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```
 
# Usage
 
```bash
$ git clone https://github.com/tech-kind/smart_gardening_system.git
$ cd smart_gardening_system
$ python3 gardening_system.py
```
 
# Author
 
* tech-kind
 
# License
 
"smart_gardening_system" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License), see LICENSE.
 
# Reference

* https://wiki.seeedstudio.com/jp/Grove_Base_Hat_for_Raspberry_Pi
