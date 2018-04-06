# linsyspy ![contributions welcome](https://img.shields.io/badge/Laboratory-awesome-brightgreen.svg?style=flat) [![Build Status](https://travis-ci.org/crazymidnight/linsyspy.svg?branch=master)](https://travis-ci.org/crazymidnight/linsyspy)
### Dynamic linear system modeling project
Python interpreter version 3.6 or higher and packages from *requirements.txt* are required.
 
### Instruction to run:
1. Install packages: 
    ```bash
     pip install -r requirements.txt
    ``` 
2. Enter initial conditions and number of simulation steps in *input.txt*

3. Run model:
    ```bash
    python model.py
    ``` 
### TODO list:
- [X] Estimation of stability - algebraic methods
- [X] Quality indicators: transient time, overshoot, settled value
- [X] Noise filter in X and Y
