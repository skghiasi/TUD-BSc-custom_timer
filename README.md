# Variable modulation of the liquid crystals
In this repository, there are files that help generating the Arduino code, which in turn, modulates (a batch) of liquid crystal(s).

## Usage
The python code "generate_arduino_code.py" has to be modified to contain proper values of the output pins, duration of each hi/lo level, and the initial signal level. 

The user has to change the parts marked by the "TODO" text in the comment, the function generate_code does not need to change. 

### An example

We have the case where the following pulse shape has to be made, and it has to appear on pins 38, 40, and 42 of Arduino (all pins show the same pulse, useful when multiple liquid crystals are used).

The TODO parts in the code have to be changed as follows: 

```python 
    voltage_pulse_durations_list = [10 , 20 , 30 , 40 , 50]
    output_pins_list = [38 , 40 , 42]
    voltage_initial_level = 0
```


