**Agenda**

1. Interview Practice Pitfalls & How to Avoid Them
2. Binary Search

---

* It's a separate skill
* different types of interviews --> whiteboarding, role specific, emotional
* data structures and algorithm interviews have a steep learning curve, but once you crack it then you will be able to ace a *good* amount of interviews.

---

**How You Practice Matters**

* How you practice has a huge impact on your performance
* Very few people practive effectively for interviews

---

**What do you think are the most common mistakes people make when practicing for interviews**

Common Mistakes

1. Mindlessly doing as many problems as you can
2. Forgetting about problems/patterns already seen
3. Not being emotionally prepared
4. Getting demotivated
5. Not preparing for other types of interview

*Practice being able to write it down without an ide and no compiler*

---

**Mindlessly doing as many problems as you can**

* Amount of Leetcode questions != Amount of your understanding of the material
* Brute-Memorizing solutions are not efficient
* Add deliberate practice to your regimen
* "... a special type of practice that is purposeful and systematic"

[practice](!practice.png)(!practice.png)

---

**Forgetting about problems/patterns already seen**

* *Acing interviews is largely on recognizing a pattern/solution you've previously used and applying it to the problem at hand
* Fast recall is important during interviews
* Add ***spaced repition*** to your regimen to retain as much information as possible

  * Use *Anki* to create custom flashcards with built-in spaced repition

[Forgetting Curve](!forgetting_curve.png)

---

**Not being emotionally prepared**

* The emoitonal and physical (pre-Covid) environment during interviews are different
* Simulate conditions similar to an actual interview:
* time

---

**Getting Demotivaated**

* Doing all hard problems is a recipe for demotivation, and ultimately failure
* Interleave easy-medium-hard problems together to gain confidence and challenge yourself
* Stuck in a problem? Look at the solution, then redo it later.

"A competitor needs to be process-oriented, always looking for stronger opponents to spur growth, but it's also important to keep on winning enough to maintain confidence" - *The Art of Learning: A Journey in the Pursuit of Excellence*"A competitor needs to be process-oriented, always looking for stronger opponents to spur growth, but it's also important to keep on winning enough to maintain confidence" - *The Art of Learning: A Journey in the Pursuit of Excellence*

---

**Binary Search**

* Halve the search space on each iteration for sorted collections/ranges for O(logn) performance
* Take the middle elements o the current search space
  * If that's the target then you're done
  * If it's greater than the target, go left
  * Else it's less thatn the target, so go right

[binary search](!binary_search.png)(!binary_search.png)

---

**When to Use Binary Search**

* Very useful for sorted collections (arrays, strings) but also ranges (range of values)
* Can be implemented iteratively/recursively
* **Keywords**: sorted, ranges
* **This should be muscle memory**

---

**Square Root Problem**

* Implement squareRoot(_x:Int) -> Int
* Find the square root of the a number x, where x>0
* Since the return type is an integer, the decimal digits will be truncated

[Example](!sample_problem.png)

---

**Square Root Brute Force**

* try every value [0, target]
* O(n) performance

```
def sqrt(x):
    # try every number from 0 to x
    # if current number is square root then output it
    for i in range (x+1):
        squared = i * i
        if squared == x:
            return i
        elif squared > x:
            return i - 1
    return -1

sqrt(8) # 2.82
```

---

Square Root Binary Search

* Use binary search to keep halving the search space
* Key idea: binary search also works for ranges of values, not just sorted arrays/strings
* O(logn) performance

---

Given a non-negative integer, x, compute and returen the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

```
"""
input: 16
output: 4

input: 8
output: 2

input: 1
output: 1

Plan:
use binary search to keep halving the search range
keep track of the nearest solution we've found
return nearest soltion found.
"""

class Solution:
    def mySqrt(self, x:int) -> int:
        min, max = 0, x  # starting from 0 to the x value
        res = 0
        while min <= max:
            mid = int((min + max)/2)
            squared = mid * mid
            if squared == x:
                return mid
            elif squared > x:
                max = mid - 1
            else:
                min = mid + 1
                res = mid
        return res
```
