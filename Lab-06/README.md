# Python Lab 06: Dictionary Data Structures and Operations

## Student Details
- **Name:** Jay Rathore
- **Roll Number:** IC2K24-40
- **Course:** Master of Computer Applications (MCA)
- **Subject:** Python Programming Laboratory

---

## Overview

Lab 06 focuses on mastering Python dictionaries (`dict`), hash-based key-value lookups, nested data structures, dictionary comprehensions, and data inversion. The laboratory is divided into three distinct components:

1. **Practical Programming Tasks (Q1 - Q5):** Menu-driven console applications demonstrating CRUD operations, data aggregation, validation, filtering, and reporting using dictionary architectures.
2. **Section B (Code Tracing & Output Analysis):** Tracing edge cases involving dictionary reference assignment, shallow copying, falsy key filtering, hash collisions (`1 == 1.0 == True`), dictionary mutation during iteration, and dictionary comprehensions.
3. **Section C (Conceptual & Theoretical Analysis):** Comprehensive explanations regarding memory references, deep versus shallow copying, hashability constraints, lookup time complexity, and safe dictionary mutation patterns.

---

## File Structure

```text
Lab-06/
├── pythonLabQ1.py    # Question 1: Student Record and Grade Management System
├── pythonLabQ2.py    # Question 2: Employee Database and Payroll Analytics
├── pythonLabQ3.py    # Question 3: Library Record and Book Lending System
├── pythonLabQ4.py    # Question 4: Word Frequency Counter and Text Analyzer
├── pythonLabQ5.py    # Question 5: Contact Book with Reverse Phone Lookup
├── SectionB.txt      # Output analysis and explanations for 8 code snippets
├── SectionC.txt      # Theoretical answers on dictionary concepts and complexities
└── README.md        # Documentation for Lab 06
```

---

## Practical Programming Tasks

### 1. Student Record and Grade Management System

- **File:** `pythonLabQ1.py`
- **Objective:** Design an interactive, menu-driven student management system using nested dictionaries to track student details and marks across multiple subjects.
- **Data Structure:**
  ```python
  records = {
      "roll_no": {
          "name": str,
          "marks": {
              "math": int,
              "phy": int,
              "chem": int
          }
      }
  }
  ```
- **Key Functionalities:**
  - **Add Student:** Validates marks between 0 and 100 before creating records; prevents duplicate roll numbers.
  - **Update Subject Marks:** Modifies marks for a specific subject within the nested marks dictionary.
  - **Delete Student:** Safely removes a student record using `.pop()`.
  - **View Record:** Displays details and subject marks for a given roll number.
  - **Comprehensive Reports:**
    - Calculates average marks per student using dictionary comprehensions.
    - Identifies the overall topper using `max()` with key extraction.
    - Determines highest scorer in each subject dynamically.
    - Filters students scoring below 40 in any subject.
    - Groups students into letter grades (`A`: >=90, `B`: >=75, `C`: >=60, `D`: >=40, `F`: <40).

---

### 2. Employee Database and Payroll Analytics

- **File:** `pythonLabQ2.py`
- **Objective:** Implement an employee record system supporting department-level aggregation, payroll calculations, and non-destructive transformations.
- **Data Structure:**
  ```python
  employees = {
      "emp_id": {
          "name": str,
          "dept": str,
          "salary": float
      }
  }
  ```
- **Key Functionalities:**
  - **Add Employee:** Enforces non-negative salary validation and unique employee IDs.
  - **Update Salary:** Updates compensation with input validation.
  - **Delete Employee:** Removes employee records safely without program termination if ID is absent.
  - **Search Employee:** Retrieves complete details by employee ID.
  - **Analytical Reports:**
    - Computes department-wise total payroll and headcount using `dict.setdefault()`.
    - Identifies the highest-paid employee per department.
    - Generates a salary-sorted roster in descending order using `sorted()` with a custom lambda key.
    - Generates a non-mutating 10% raise simulation for employees earning below 50,000 using dictionary comprehensions.
    - Identifies the department with the highest average salary.

---

### 3. Library Record and Book Lending System

- **File:** `pythonLabQ3.py`
- **Objective:** Create a multi-copy library catalog tracking book availability, borrowing privileges, and borrower relationships.
- **Data Structure:**
  ```python
  books = {
      "isbn": {
          "title": str,
          "author": str,
          "copies": int,
          "issued_to": list,      # List of member IDs
          "ever_issued": bool
      }
  }
  ```
- **Key Functionalities:**
  - **Add Book / Restock:** Adds a new book or increments copy count if the ISBN already exists.
  - **Issue Book:**
    - Checks copy availability (copies > 0).
    - Prevents duplicate issuance of the same title to the same member.
    - Enforces a maximum borrowing limit of 2 books per member across the library.
    - Decrements available copies and marks `ever_issued` as True.
  - **Return Book:** Restores stock and removes member ID from the active borrowers list.
  - **Search:** Case-insensitive search by ISBN or partial title.
  - **Reports:**
    - Filters titles by a specific author.
    - Inverts book-to-member relationships to identify members holding multiple books.
    - Lists out-of-stock titles (0 available copies).
    - Lists titles that have never been checked out.

---

### 4. Word Frequency Counter and Text Analyzer

- **File:** `pythonLabQ4.py`
- **Objective:** Process raw textual input, clean non-alphanumeric noise, calculate word occurrences, and produce inverted frequency indexes.
- **Key Functionalities:**
  - **Text Normalization:** Converts text to lowercase and strips punctuation using character-level checks (`isalnum()`).
  - **Frequency Mapping:** Counts occurrences using `dict.get(word, 0) + 1`.
  - **Top N Words:** Sorts by frequency descending, breaking ties alphabetically via `sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))`.
  - **Hapax Legomena:** Extracts and displays words occurring exactly once.
  - **Inverted Frequency Dictionary:** Groups words by frequency: `{frequency: [list_of_words]}`.
  - **Length-wise Indexing:** Groups unique words by their character count: `{length: [list_of_words]}`.
  - **Word Search:** Instant O(1) frequency lookup for user-queried words.

---

### 5. Contact Book with Reverse Phone Lookup

- **File:** `pythonLabQ5.py`
- **Objective:** Build a contact directory supporting multi-number contacts, strict 10-digit validation, global phone uniqueness, and reverse lookup indexing.
- **Data Structure:**
  ```python
  directory = {
      "name": {
          "phones": list,    # List of 10-digit string phone numbers
          "email": str,
          "city": str
      }
  }
  ```
- **Key Functionalities:**
  - **Add Contact:** Validates phone number length (10 digits, numeric) and ensures global uniqueness across all contacts before insertion.
  - **Add Secondary Number:** Allows adding multiple distinct contact numbers to an existing person while maintaining global uniqueness.
  - **Update Details:** Allows modifying email or city independently.
  - **Safe Deletion:** Deletes records using `.pop(name, None)` to prevent KeyError exceptions.
  - **Partial Name Search:** Substring search across all contact names.
  - **Reports and Utilities:**
    - **Reverse Lookup Dictionary:** Dynamically generates `{phone_number: owner_name}` via comprehension for instant O(1) phone-to-name resolution.
    - **City Grouping:** Groups contact names by city using `setdefault()`.
    - **Multi-number Flag:** Lists all contacts possessing more than one phone number.
    - **Sorted Directory:** Displays all records in alphabetical order of contact names.

---

## Section B: Code Tracing and Output Analysis Summary

The file `SectionB.txt` documents the step-by-step tracing and expected outputs for eight dictionary code snippets:

1. **Object Reference Assignment:** Demonstrates that `d2 = d` assigns a shared reference rather than creating a copy, causing mutations via `d2` to alter `d`.
2. **Shallow Copy (`.copy()`):** Illustrates that shallow copying duplicates the top-level dictionary but retains shared references to nested mutable objects (e.g., lists).
3. **Dictionary Comprehension with Truthiness Filtering:** Traces filtering during zip iteration where falsy values (like `0`) are dropped.
4. **`setdefault()` Behavior:** Confirms that `setdefault()` returns existing values without overwriting, while inserting default values only for absent keys.
5. **Key Equality and Hash Collisions:** Explains why `{1: "a", 1.0: "b", True: "c"}` resolves to length 1 due to `1 == 1.0 == True` and matching hash values in Python.
6. **Dictionary Mutation During Iteration:** Traces why using `del d[k]` while looping directly over `d` triggers a `RuntimeError: dictionary changed size during iteration`.
7. **Safe Extraction (`.pop()` and `.popitem()`):** Demonstrates safe retrieval with fallbacks (`d.pop("z", None)`) and removal of the most recently inserted item (`d.popitem()`).
8. **Key-Value Inversion Overwrite:** Demonstrates that inverting a dictionary with duplicate values results in key collisions where later entries overwrite earlier ones.

---

## Section C: Conceptual and Theoretical Analysis Summary

The file `SectionC.txt` addresses foundational theoretical concepts in Python dictionary mechanics:

- **Reference vs. Shallow Copy vs. Deep Copy:**
  - Reference assignment creates an alias pointing to the same memory block.
  - `d.copy()` clones top-level keys but references identical nested structures.
  - `copy.deepcopy()` recursively duplicates all levels, making it the required approach for nested databases (such as student marks) to prevent unintended side effects.
- **Key Hashability and Access Strategies:**
  - Keys must be hashable and immutable (e.g., `tuple`, `str`, `int`) so their hash value remains constant across the lifetime of the hash table. Mutable types (`list`, `set`) are unhashable.
  - `d[key]` is used when a key is guaranteed to exist.
  - `d.get(key)` is used for optional lookups where missing keys should return `None`.
  - `d.get(key, default)` is used for aggregations and counters where missing keys need an initial baseline value (e.g., `0`).
- **Batch Updates vs. Iterative Assignment:**
  - `d.update()` efficiently merges another dictionary or iterable of key-value pairs in a single internal C-level operation, offering cleaner syntax and better performance than manual loops.
- **Data Immutability via Comprehensions:**
  - Generating new dictionaries through comprehensions avoids mutating source datasets, maintaining an audit trail and preventing race conditions in analytical pipelines.
- **Safe Deletion During Iteration:**
  - Modifying dictionary topology while iterating over it causes iterator desynchronization.
  - Safe methods include iterating over a static snapshot using `list(d.keys())` or constructing a filtered dictionary using comprehension syntax.
- **Time Complexity and Reverse Indexing:**
  - Dictionary key lookups run in average **O(1)** constant time due to hash tables, compared to **O(N)** linear searches over lists.
  - Creating inverted lookup dictionaries (such as phone-to-name mappings) is essential for scaling query operations efficiently.

---

## How to Run the Programs

All programs are written in Python 3 and require no third-party libraries. Run each program from the terminal:

```bash
# Navigate to the Lab-06 directory
cd Desktop/IC2K24-40-PythonLab-JayRathore/Lab-06

# Run Question 1: Student Management System
python3 pythonLabQ1.py

# Run Question 2: Employee Payroll System
python3 pythonLabQ2.py

# Run Question 3: Library Management System
python3 pythonLabQ3.py

# Run Question 4: Word Frequency Counter
python3 pythonLabQ4.py

# Run Question 5: Contact Book with Reverse Lookup
python3 pythonLabQ5.py
```

---

## Conclusion

This laboratory work demonstrates the practical and theoretical mastery of Python dictionaries. By leveraging average O(1) lookups, nested schemas, dictionary comprehensions, and safe data handling patterns, these implementations provide robust, error-tolerant, and performant solutions to standard record-keeping and data processing problems.
