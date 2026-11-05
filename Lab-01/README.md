# Python Lab - 01 
## By Jay Rathore
## IC2K24-40


## 1. Variable and Identifier Practice
**File:** `VariableandIdentifierPractice.py`

**Aim:** Demonstrate declaring variables of different data types and checking their types.

**Logic:**
Four variables are created to hold a name (string), age (integer), height (float), and student status (boolean). Each is printed alongside the result of `type()` to confirm Python's automatic type assignment.

**Sample Input / Output:**
```
(No input required)

Name :  Jay Rathore <class 'str'>
Age :  24 <class 'int'>
Height :  170 <class 'int'>
Whether Student :  True <class 'bool'>

---

## 2. Greeting Program
**File:** `GreetingProgram.py`

**Aim:** Take basic user details as input and greet the user with a personalized message.

**Logic:**
Three inputs (name, age, city) are collected using `input()`. Since `input()` always returns a string, no type conversion is needed as the values are only used for display. An f-string combines all three into one sentence.

**Sample Input / Output:**
```
Please Enter your name : Rahul
Enter your Age Please : 21
Enter your City Please : Bhopal
Greetings to Mr.Rahul. You entered your age 21 years old and you belong to Bhopal.  Greetings! Nice to Meet you.
```

---

## 3. Arithmetic Operations
**File:** `ArithmeticOperations.py`

**Aim:** Take two numbers as input and perform basic arithmetic operations on them.

**Logic:**
Two numbers are read using `input()` and converted to `float` using `float()`. All five operations (sum, difference, product, quotient, remainder) are computed using standard operators and printed with clear labels.

**Sample Input / Output:**
```
Enter the First Number : 12
Enter the Second Number : 4
Sum =  16.0
Diffrence =  8.0
Product =  48.0
Quotient =  3.0
Remainder =  0.0
```

---

## 4. Celsius to Fahrenheit
**File:** `CelsiustoFahrenheit.py`

**Aim:** Convert a temperature value from Celsius to Fahrenheit.

**Logic:**
The Celsius value is taken as input and converted to `float`. The formula `F = (C * 9/5) + 32` is applied, and the result is displayed using an f-string.

**Sample Input / Output:**
```
Enter the temperature please : 30
The temperature in Fahrenheit is :  86.0
```

---

## 5. String Manipulation
**File:** `StringManipulation.py`

**Aim:** Take a full name as input and demonstrate common string operations on it.

**Logic:**
The name is stored as a string, and its uppercase and lowercase forms are obtained using the `.upper()` and `.lower()` methods. It is reversed using slicing (`[::-1]`), and its length is found using `len()`.

**Sample Input / Output:**
```
Enter your full name : Jay Rathore
In Upper case :  AISHWARYA KUMAR SINGH
In Lower case :  aishwarya kumar singh
Reversed :  hgniS ramuK ayrawhsiA
Total Length :  21
```

---

## 6. Escape Sequence Practice
**File:** `EscapeSequence.py`

**Aim:** Print a small, neatly aligned receipt using escape sequences.

**Logic:**
Tab characters (`\t`) are used to align item names and prices into columns, while each `print()` call naturally moves to a new line. Extra tabs are added after short item names so all prices line up under one column.

**Sample Input / Output:**
```
(No input required)
Item Name	MRP	    Billing Price

#Keyboard	899		    749

#Mouse		499		    449

#Monitor   10,000		9,499

## 7. Bonus Question
**File:** `BonusCalculator.py `

**Sample Input / Output:**
```
--- Calculator Menu ---
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Select an option (1-5): 1
Enter first number: 2
Enter second number: 3
Result: 5.0

--- Calculator Menu ---
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Select an option (1-5): 5
Exiting calculator. Goodbye!
