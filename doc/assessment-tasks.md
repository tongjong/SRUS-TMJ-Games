# Overview

This assessment evaluates your ability to perform the following tasks in accordance with ICTPRG547 Apply advanced programming skills in another language:

## 1. Performance elements

- 1.4 Code sorting algorithm using programming techniques
- 3.2 Detect and resolve errors of syntactical, logical and design origin
- 3.3 Design and document required tests
- 4.1 Develop and document solution according to debugging test results

You will demonstrate your performance by providing evidence that you can code at least one sorting algorithm, and test and debug the code to resolve errors of a syntactical, logical, or design origin.

To succeed you must use a systematic, analytical processes in complex, non-routine situations, setting goals, gathering relevant information, and identifying, and evaluating, options against the agreed criteria

## 2. General instructions

> CRITICAL: Failure to follow these instructions will lead to an NYC

- Copy this file into a `docs` folder in your assessment repo
- Add and commit this file to your repository and associate the tag `por3-start` :
  - Copy and `add` this file to your repository under the `docs` folder
  - `git commit -m "chore: add task overview to my repo"
  - `git tag por3-start`
  - `git push origin main --tags`
  - Optional: you may want to complete this work in a branch
  - On your last commit, add the tag `por3-finish`
- Commit changes after you complete each task
- Push changes to your GitHub repository
- Ensure you submit your git repo (`.git/`) along with your assessment submission

## 3. Players have scores now

### 3.1. Task: Add scores to players

Add a private instance variable to the Player class that will hold the score (a positive integer value).

Provide a getter (property) and a setter method for this value.

#### 3.1.1. Success criteria

- [ ] Correct use of private instance variable
- [ ] Use of properties to create a getter and setter
- [ ] Raising ValueError if someone attempts to set a non-positive value

## 4. Sorting players

### 4.1. Task: Add unit tests for sorting players

Add the following unit tests to the `test_player.py` file:

```python
def test_sort_players(self):
    players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5), Player("Charlie", uid='03', score=15)]
    # note: ensure initialization code is valid for **your** implementation

    # do **not** change the following code:
    sorted_players = sorted(players)

    # players must be sorted by score as shown here:
    manually_sorted_players = [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10), Player("Charlie", uid='03', score=15)]

   self.assertListEqual(sorted_players, manually_sorted_players)

```

> **Note:** f you have made other changes to the initializer of your player update the above code to reflect this change - you must not make any other changes to the test code above.

### 4.2. Task: Interpret unit tests

What was the outcome of running the above unit test, copy paste the output **for just this particular test** below:

```text
FAILED                      [100%]
player_test.py:12 (TestPlayer.test_sort_player)
self = <player_test.TestPlayer testMethod=test_sort_player>

    def test_sort_player(self):
        player_1 = Player('01', "Alice", 10)
        player_2 = Player('02', "Bob", 5)
        player_3 = Player('03', "Charlie", 15)
        players = [player_1, player_2, player_3]
    
>       sorted_players = sorted(players)
E       TypeError: '<' not supported between instances of 'Player' and 'Player'

player_test.py:19: TypeError
```

### 4.3. Success criteria

- [ ] Unit test added to `test_player.py`
- [ ] Unit test output provided
- [ ] Unit test output reflects the error in `sorted(players)` (if you are getting another error read the instructions CAREFULLY)

#### 4.3.1. Question

The tests checks that calling sorted on a list of players will sort them by score, what is the **only** magic method that must be implemented in the player class for the `sorted` function to succeed?
The magic method that must be implemented is __lt__ 
> Answer Here

#### 4.3.2. Task: Implement the magic method in the Player class

Add a test case to test_player to test the comparison operator you are about to add - ensure you do not test a dunder method directly!

```python
def test_players_can_be_compared_by_score(self):
    # note: ensure initialization code is valid for **your** implementation
    alice = Player("Alice", uid='01', score=10)
    bob = Player("Bob", uid='02', score=5)

    # Add the appropriate expression to the following assert test
    self.assertTrue(...)
```

Run the test and confirm that your error resembles the previous error

```text
FAILED [100%]
player_test.py:26 (TestPlayer.test_players_can_be_compared_by_score)
self = <player_test.TestPlayer testMethod=test_players_can_be_compared_by_score>

    def test_players_can_be_compared_by_score(self):
>       self.assertTrue(self.alice < self.bob)
E       TypeError: '<' not supported between instances of 'Player' and 'Player'

player_test.py:28: TypeError
```

Implement the appropriate magic method in the Player class and ensure you pass this test (and only this test!).

#### 4.3.3. Success criteria

- [ ] Unit test added to `test_player.py`
- [ ] Magic method implemented in `Player` class
- [ ] Initial Failed Unit test output provided
- [ ] Unit test runs successfully with submited code
- [ ] Dunder method not employed directly

#### 4.3.4. Task: Are we sorted yet?

Rerun `test_sort_players` does the test pass? If not, include the output below:

```text
FAILED                      [100%]
player_test.py:17 (TestPlayer.test_sort_player)
self = <player_test.TestPlayer testMethod=test_sort_player>

    def test_sort_player(self):
    
        players = [self.alice, self.bob, self.charlie]
        manually_sorted_players = [self.bob, self.alice, self.charlie]
    
        sorted_players = sorted(players)
    
>       self.assertListEqual(sorted_players, manually_sorted_players)
E       AssertionError: Lists differ: [<app[33 chars]8F007D5A90>, <app.player.Player object at 0x00[61 chars]5D0>] != [<app[33 chars]8F00772710>, <app.player.Player object at 0x00[61 chars]5D0>]
E       
E       First differing element 0:
E       <app.player.Player object at 0x0000028F007D5A90>
E       <app.player.Player object at 0x0000028F00772710>
E       
E       - [<app.player.Player object at 0x0000028F007D5A90>,
E       -  <app.player.Player object at 0x0000028F00772710>,
E       ? ^
E       
E       + [<app.player.Player object at 0x0000028F00772710>,
E       ? ^
E       
E       +  <app.player.Player object at 0x0000028F007D5A90>,
E          <app.player.Player object at 0x0000028F007725D0>]

player_test.py:25: AssertionError
```

Why did the test fail (note: if it doesn't fail, it means there is something you have already done before you were asked to - you need to figure out what that is!)?

> When objects are compared for equality, They are implemented to compare the objects by its reference in memory rather than the object content. Since the two objects compared 
> are stored in different place in memory, the test fails. Therefore, the magic method which implements the objects comparison by default needs to be overridden for the test to pass.git  

Add the necessary code to the Player class to ensure that the `test_sort_players` test passes.

#### 4.3.5. Success criteria

- [ ] Correct explanation of why `test_sort_players` failed/passed
- [ ] Correct implementation of the magic method in the `Player` class
- [ ] `test_sort_players` passes when run against the submitted code

## 5. Implement a custom sorting algorithm

The senior developer on your team believes that a custom sorting algorithm would be more efficient than the built-in `sorted` function (you grit your teeth, sigh, and realize you need this job!). They have asked you to implement a custom sorting algorithm that will sort a list of players by score.

To help you get started they have provided you with some example code that they wrote in their undergraduate days:

```python
def sort_quickly(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort_quickly(left) + [pivot] + sort_quickly(right)
```

### 5.1. Question: complexity

What is the expected time and space complexity of the above algorithm? You can answer using big O or in plain English but in both cases you MUST justify your answer.

> The example code has big O(nlogn) time complexity and big O(n^2) in worst case scenarios where the selected pivot is less than or greater than 
  all the other elements in the array. As there are more elements in the array, it requires to step through the list x amount of the elements till the array is sorted.
  so the put through the array will go up exponentially while the time goes up linearly. As we partition the array in to two each time, it will take a linear time till the 
  array is sorted, therefore n times logn.

### 5.2. Task: Implement the custom sorting algorithm

#### 5.2.1. Create a new method in the Player class

Use the sample above (and its algorithm) as a starting point to implement a `classmethod` in the Player class that takes a list of players and returns a list of players sorted by score in **descending** order. Top scores come first!

#### 5.2.2. Create a test cases

Add a separate test case to `test_player.py` to test your custom sorting algorithm

Include your code below:

```python
@classmethod
def sort(cls, arr: list["Player"]):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x.score < pivot.score:
            left.append(x)
        else:
            right.append(x)

    return cls.sort(left) + [pivot] + cls.sort(right)

def test_sort(self):
    sorted_players = Player.sort([self.alice, self.bob, self.charlie])
    manually_sorted_players = [self.alice, self.bob, self.charlie]

    self.assertListEqual(sorted_players, manually_sorted_players)
```

#### 5.2.3. Success criteria

- [ ] Custom sorting algorithm implemented in the `Player` class as `classmethod`
- [ ] Custom sorting algorithm sorts in descending order
- [ ] Custom sorting algorithm compares players using their score (via the rich comparison operators)
- [ ] Custom sorting algorithm tested in `test_player.py` and tests passed

### 5.3. Test your custom sorting algorithm at scale

The senior developer is impressed with your work and asks you to test your custom sorting algorithm with a list of 1000 players. They provide you with a script that will generate a list of 1000 players with random scores.

```python
import random
from player import Player


players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
```

#### 5.3.1. Task: Create a test case to sort 1000 players

Using the code above as a starting point, create a test case to test your custom sort algorithm - you can test it against the `sorted` function to ensure it is working correctly.

Include your test case below:

```python
  def test_sort_with_1000_players(self):
        players = [Player(f"{i:03}", f"Player {i}", score=random.randint(0, 1000)) for i in range(1000)]

        sorted_players_using_custom_alg = Player.sort(players, descend=False)
        sorted_players_using_built_in_alg = sorted(players)

        self.assertListEqual(sorted_players_using_built_in_alg, sorted_players_using_custom_alg)
```

#### 5.3.2. Success criteria

- [ ] Test case added to `test_player.py`
- [ ] Test case sorts 1000 players correctly when compared to `sorted` function
- [ ] Test case passes when run against the submitted code

#### 5.3.3. Task: Testing sorting sorted players

You had a scary thought - and decided to test your custom sorting algorithm against a list of players that are already sorted by score. You are worried that your algorithm might not be efficient in this case.

#### 5.3.4. Task: Create a test case to sort 1000 sorted players

Create a test case that tries to sort 1000 players that are already sorted.

If you get a failure, include the failure below:

```text
FAILED (errors=1)

Error
Traceback (most recent call last):
  File "C:\Users\Tong\Desktop\python-2025\assignments\SRUS-TMJ-Games\test\player_test.py", line 50, in test_sort_with_sorted_list_with_1000_players
    sorted_players_using_custom_alg = Player.sort(players)
                                      ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tong\Desktop\python-2025\assignments\SRUS-TMJ-Games\app\player.py", line 71, in sort
    return cls.sort(left, descend) + [pivot] + cls.sort(right, descend)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tong\Desktop\python-2025\assignments\SRUS-TMJ-Games\app\player.py", line 71, in sort
    return cls.sort(left, descend) + [pivot] + cls.sort(right, descend)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tong\Desktop\python-2025\assignments\SRUS-TMJ-Games\app\player.py", line 71, in sort
    return cls.sort(left, descend) + [pivot] + cls.sort(right, descend)
           ^^^^^^^^^^^^^^^^^^^^^^^
  [Previous line repeated 983 more times]
  File "C:\Users\Tong\Desktop\python-2025\assignments\SRUS-TMJ-Games\app\player.py", line 66, in sort
    if x.score > pivot.score:
       ^^^^^^^
RecursionError: maximum recursion depth exceeded
```

Provide a reason why this test failed (if you got recursion errors, you need to explain **why** they occurred).

If your implementation did not fail, you must explain what changes you made to the original algorithm given by the senior developer to ensure that it did not fail.

> The error is due to the sort function recursively calls itself too many times exceeding the stack flow. Currently, there is no check to determine if the list is already sorted, resulting in returning the very same array over and over, causing the stack overflow.
Propose a fix to your sorting algorithm that fixes this issue.

```python
list_sorted = False
        index = 0

        while index < len(arr) - 1:
            if descend:
                if arr[index] > arr[index + 1]:
                    list_sorted = True
                else:
                    list_sorted = False
                    break
            else:
                if arr[index] < arr[index + 1]:
                    list_sorted = True
                else:
                    list_sorted = False
                    break
            index += 1

        if list_sorted or len(arr) <= 1:
            return arr
```

#### 5.3.5. Success criteria

- [ ] Test case added to `test_player.py`
- [ ] Test case passes only when changes above are added

## 6. Task: Authenticity of in class work

Complete the following snippet before you submit:

```text
I, <Tong Jong and J155917>, partially completed this work in class 306,under the supervision of Rafael Avigad, and partially completed it at home on 1/4/25.

I understand that until I meet my assessor to confirm that this work is a valid and true representation of my abilities to write and debug a sorting algorithm in Python, this submission cannot be considered complete.

```

## 7. Submit your work

- [ ] Ensure all tasks are complete and tests pass
- [ ] Answer all questions in your own words
- [ ] Complete the statement of authenticity
- [ ] Include `.git` showing each task committed (you must show at least 5 commits)
- [ ] Tag your last commit as `por3-finish`
- [ ] Push your changes to your GitHub repository
- [ ] Submit a zip of your repository to the LMS (ensure you do not add the `.venv` or `__pycache__` folders)

---
End of assessment task