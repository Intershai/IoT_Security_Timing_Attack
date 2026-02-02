# IoT Security Project: Timing Attack on Authentication

## Project Overview
This project demonstrates a **Timing Attack** (side-channel attack) on an IoT device's PIN verification process. [cite_start]It fulfills the requirements for Project Topic #15[cite: 68, 69, 70].

### Contents
* [cite_start]`vulnerable_device.py`: Simulation of an IoT device with a character-by-character comparison vulnerability[cite: 69].
* [cite_start]`attacker.py`: Script that deduces the PIN by measuring response times.
* [cite_start]`secure_device.py`: Refactored code using constant-time comparison to prevent the attack.

## Vulnerability Analysis
[cite_start]The vulnerability exists because the verification function returns `False` immediately upon finding the first incorrect character (early exit)[cite: 61, 69]. [cite_start]This creates a measurable difference in execution time, allowing an attacker to guess the PIN digit by digit.

## How to Run
1. Run the attack simulation:
   ```bash
   python attacker.py
2. Observe how each digit is identified based on the response time delay.

Mitigation
The secure_device.py implements a constant-time comparison. It processes all characters of the PIN regardless of whether they match, ensuring the response time is always identical.
