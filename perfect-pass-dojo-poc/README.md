### Randori #3 - Perfect Pass

Entropy is central to the second law of thermodynamics, which states that the entropy of an isolated system left to spontaneous evolution cannot decrease with time. As a result, isolated systems evolve toward thermodynamic equilibrium, where the entropy is highest. A consequence of the second law of thermodynamics is that certain processes are irreversible. WAT? Keep reading...

Password entropy is important because it measures password randomness and unpredictability — the greater the entropy, the more effective the password is against all types of cyberattacks.
One of the most common types of targeted cyberattack is a brute force attack in which cybercriminals try all possible character combinations to discover your password. Sometimes they use dictionaries of common passwords (like “qwerty” or “123456”) to break into password-protected computers, accounts, and networks — this strategy is better known as a dictionary attack.

Passwords are complicated, the famous 123deoliveira4 is bad, we need to do better, we can and we will. But in order to do better we need to be creative sometimes.Our company decided to increase the security for endusers. We are tasked with project to create the perfect password validator. We need to be able to detect if the password is weak or strong, the cool kids dont call strong passwords anymore, they call perfect pass. We need to write a program that pass all 7 rules of perfect password, so our detector call tell if any password is perfect or not, rules:
```
Rule #1 - The length needs to be 32 chars.
Rule #2 - The character "!" is forbiden.
Rule #3 - The character "_" is forbiden.
Rule #4 - The password need to have at least 2 Capital letters
Rule #5 - The password need to have at least 2 numbers
Rule #6 - The password need to have at exact 2 special chars (#,*,-,$)
Rule #7 - The password need to have the longest substring without repeating chars == 26
```

### Usage

* Run unit tests

```shell
python3 -m unittest -v test_main.py
```