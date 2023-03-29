# Project Algorithms :computer:

Whiteboard problems (algorithmic challenges). This project presents solutions to six algorithmic challenges developed to demonstrate proficiency in techniques such as algorithmic complexity analysis, sorting algorithms, searching algorithms, recursion, and iterative solutions. Each challenge includes a detailed problem description, and solutions have been provided to showcase mastery of these skills.

## :hammer_and_wrench: Habilities

:green_circle: Python

:large_blue_circle: Algorithmic complexity
<br>

:large_blue_circle: Search algorithms
<br>

:large_blue_circle: Sorting algorithms
<br>

:large_blue_circle: Recursion
<br>

:large_blue_circle: Iteration
<br>

:large_blue_circle: Logic and problem solving
<br>

## Requirements

`venv`
> `Venv` is a built-in module in Python used to isolate project environments. In practice, we use `venv` so that each project has its own libraries with the desired version. If `venv` is not installed, use the command `sudo apt install python3-venv`.

## :wrench:  Setup

Clone the repository:

```
git clone git@github.com:crisnabto/Algorithms.git
```

Create the virtual environment for the project

```
python3 -m venv .venv && source .venv/bin/activate
```

Install the dependencies

```
python3 -m pip install -r dev-requirements.txt
```

> To run the files, use `python3 -i challenges/name_of_the_challenge.py`

## Challenges

<details>
  <summary>1. Number of students studying at the same time (Search algorithm)</summary><br />
  
  File `challenges/challenge_study_schedule.py`
  
  You work at the largest education company in Brazil. One day, the Product Manager `(PM)` wants to know which time has the highest number of students accessing the platform's content. With this data in hand, the PM will know the best time to make study materials available for maximum engagement.

The system's entry and exit times are recorded in the database every time a student enters and exits the system. This data will be contained in a list of tuples (`permanence_period`) where each tuple represents a student's period of stay in the system with their entry and exit times.

Your task is to discover the best time to make study materials available. To do this, use the problem-solving strategy called `brute force`, in which the function developed by you will be called several times with different values for the `target_time` variable, and the function returns will be analyzed.

:eyes: _Tip:_ The best time will be the one where the counter returned by the function is the highest.

<details>
 <summary>
   <b>Click here to see an example.</b>
 </summary>

```md
# In the arrays there are 6 students

# studant             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # output: 3, because the fourth, fifth, and sixth students were still studying during that time.
target_time = 4  # output: 3, because the fifth and sixth students started studying during that time, and the fourth was still studying.
target_time = 3  # output: 2, because the third and fourth students were still studying during that time.
target_time = 2  # output: 4, because the first, second, third, and fourth students were studying during that time.
target_time = 1  # output: 2, because the second and fourth students were studying during that time.

For this example, after running the function for all of these target times, we determined that the best time is 2, since it returned 4, meaning that 4 students were present during that time!
```
</details>

- The algorithm should use an iterative solution;
- If the target_time passed is null, the function should return None (consider 0 as a valid time);
- Return the number of present students for a specific input;
- Return None if there is any invalid input in permanence_period;
- Return None if target_time receives an empty value;
- The function should, through empirical analysis, behave with a maximum of O(n) complexity, that is, with linear asymptotic complexity.

</details>

<details>
  <summary>2. Cryptography of inversions (Test)</summary><br />
  
  File `tests/encrypt/test_encrypt.py`
  
  During a group dynamics activity in a hiring process, the hiring company defined a challenge in pairs, and each person will have a role. The first person must create a encryption function, and the second person must implement tests for the function implemented by the first person.

You will play the role of the second person in this dynamics, that is: you must implement the tests for an encryption function.

This test should be called `test_encrypt_message`, and it must ensure that the encryption function `encrypt_message` follows a specific logic.

<details>
  <summary>
    <b>🧠 Understanding the logic of the encryption function</b>
  </summary>

- Receives a string message and an integer key as parameters
- If `key` and `message` don't have the correct types, an exception should be raised
- If `key` is not a valid positive index of `message`, return the reversed string `message`
- If `key` is odd:
  - split `message` at index `key`, reverse the characters of each part, and return the union of the parts with `"_"` between them
- If `key` is even:
  - split `message` at index `key`, reverse the position of the parts, reverse the characters of each part, and return the union of the parts with `"_"` between them

</details>

</details>

<details>
  <summary>3. Palindromes (Recursion)</summary><br />
  
  File `challenges/challenge_palindromes_recursive.py`
  
  Write a function that will determine whether a word is a palindrome or not. The function will receive a string as a parameter and the return value will be a _boolean_, `True` or `False`.

But what is a palindrome?

> A palindrome is a word, phrase, or number that maintains its meaning even when read backward. For example, "ABCBA".

:warning: In this project we will focus only on palindromic words and not on phrases or numbers.

<details>
 <summary>
   <b>Click here to see an example.</b>
 </summary>

```md
word = "ANA"
# output: True

word = "SOCOS"
# output: True

word = "REVIVER"
# output: True

word = "COXINHA"
# output: False

word = "AGUA"
# output: False
```

</details>

- The algorithm must be implemented using a recursive solution;

- Do not worry about the complexity analysis of this algorithm;

- If an empty string is passed, return False.

</details>

</details>

<details>

  <summary>4. Anagrams (Sorting algorithm)</summary><br />
  
  File `challenges/challenge_anagrams.py`
  
  Create an algorithm that can compare two strings, sort them, and identify whether one is an anagram of the other. That is, your function will receive two string parameters and the function's return will be a `()` tuple with the first string sorted, the second string sorted, and a `True` or `False ` _boolean_ representing if they are anagrams.

The algorithm should consider uppercase and lowercase letters as equal during the input comparison, i.e., be case insensitive.

But what is an anagram?

> "An anagram is a kind of wordplay created by rearranging the letters of a word or expression to produce other words or expressions, using all the original letters exactly once."

<details>
 <summary>
   <b>Click here to see an example.</b>
 </summary>

```md
first_string = "amor"
second_string = "roma"
# output: ('amor', 'amor', True)
# Explanation: In this case, the sorted string of 'amor' remains 'amor', and the sorted string of 'roma' becomes 'amor'. Furthermore, the function returns True because the word "roma" is an anagram of "amor".


first_string = "pedra"
second_string = "perda"
# output: ('adepr', 'adepr', True)
# Explanation: In this case, the return value is also True. In the word "pedra", we swap the "d" with the "r" and form "perda", which is an anagram, and we have both strings sorted.


first_string = "pato"
second_string = "tapo"
# output: ('aopt', 'aopt', True)


first_string = "Amor"
second_string = "Roma"
# output: ('amor', 'amor', True)
# Explanation: In this case, the function returns True because the word "Roma" is an anagram of "Amor" regardless of the letters "R" and "A" being capitalized.


# Now check this example where there is no anagram
first_string = "coxinha"
second_string = "empada"
# output: ('achinox', 'aademp', False)
```

</details>

- Use sorting algorithms to perform this requirement.

- You can use any algorithm you want (Selection sort, Insertion sort, Bubble sort, Merge sort, Quick sort or TimSort), as long as it achieves a complexity of O(n log n).

:warning: Among the algorithms mentioned above, you must choose one that meets the desired complexity for the requirement and adapt it to the problem. The use of ready-made Python functions is not allowed.

Examples of not allowed ready-made Python functions: sort, sorted and Counter;

:warning: It is not allowed to perform any imports in this file!

- The function returns True if one string is an anagram of the other, regardless of whether the letters are uppercase or lowercase;

- The function returns False if one string is not an anagram of the other;

- The function should, through empirical analysis, behave at most as O(n log n), i.e., with linearithmic asymptotic complexity.


</details>

<details>
  <summary> 5. Finding repeated numbers (Search algorithm)</summary><br />
  
  File `challenge_find_the_duplicate.py`
  
  Given an array of integers nums containing n + 1 integers, where each integer is in the range [1, n].

  Return only one duplicated number in nums.
  
  <details>
 <summary>
   <b>Click here to see an example.</b>
 </summary>

```md
nums = [1, 3, 4, 2, 2]
# output: 2

nums = [3, 1, 3, 4, 2]
# output: 3

nums = [1, 1]
# output: 1

nums = [1, 1, 2]
# output: 1

nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# output: 7
```

</details>

- If no value is passed or a string is passed or there are no duplicate numbers, return False.
- The array must:

  - Have only positive integers greater than 1;

  - Have only one number repeating two or more times, all other numbers must appear only once;

  - Have at least two numbers.

- The function should, through empirical analysis, behave at most as O(n log n), i.e., with linearithmic asymptotic complexity.

</details>

<details>
  <summary>6. Palindromes (Iterativity)</summary><br />
  
  File `challenge_palindromes_iterative.py`
  
  Solve the same problem presented in requirement 2 - Palindromes, but this time using an iterative solution.
  
  - The function should, through empirical analysis, behave at most as O(n), i.e., with linear asymptotic complexity.
  
</details>

---


### :envelope_with_arrow: Contact

[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:crisnabto@gmail.com)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/crisna-bezerra/)












  
  
  
  
  
  
