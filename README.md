# PID_Sim
PID Controller sim


## To install:
[Make sure you have python installed on your computer](https://www.python.org/downloads/)


## Install dependencies
```
pip3 install pygame
pip3 install pygame_widgets
```
## To Run:
```
git clone https://github.com/ravenstudios/PID_Sim.git
cd PID_Sim
python3 main.py

```
## To use:
There are sliders for the set poit, p term, i term, d term and a switch to turn the system on and off.
Turn on PID Controller
Set the set point slider
Set the P term slider, to much P term will case instability and oscillating
Set The I term slider, this will smooth out oscillations, to much will casuse slow reactions and delays
For this system, D term isnt needed and causes instability. Future systems will use this term.
