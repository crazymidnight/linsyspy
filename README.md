# linsyspy
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
- [ ] Quality indicators: transient time, overshoot, static error
- [ ] Noise filter in X and Y