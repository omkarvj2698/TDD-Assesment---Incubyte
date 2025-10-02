# TDD Assessment – Calculator

This project is my solution for the **Incubyte TDD Assessment**.  
The task was to build a small calculator function using **Test Driven Development (TDD)** in Python.

## Problem Statement
- **Input**: a string of numbers separated by delimiters  
- **Output**: the sum of the numbers as an integer  

### Requirements
1. Empty string should return `0`  
2. Single number should return the number itself  
3. Two numbers separated by a comma should return their sum  
4. The method should handle any amount of numbers  
5. New lines between numbers are allowed as separators  
   - Example: `"1\n2,3"` → `6`  
6. A custom delimiter can be defined in the format:  
   `//[delimiter]\n[numbers]`  
   - Example: `"//;\n1;2"` → `3`  
7. Negative numbers should throw an exception with the message:  
   `"negative numbers not allowed <numbers>"`  
   - If there are multiple negatives, list all of them separated by commas  

## How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/omkarvj2698/TDD-Assesment---Incubyte.git
   cd TDD-Assesment---Incubyte
   pip install -r requirements.txt
   pytest
