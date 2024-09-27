###### 1. What is the correct way to create an empty list in Python?

- A: empty_list = []
- B: empty_list = {}
- C: empty_list = list[]
- D: empty_list = new_list()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer ->  A: empty_list = []

</p>
</details>

###### 2. What is the output of the following Python code that calculates the square root of 25 and performs trigonometric functions on an angle of 45 degrees?

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for x in numbers:
    squared.append(x**2)
result = sum(squared)

```

- A: 55
- B: 30
- C: 15
- D: 25

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: 55

</p>
</details>

###### 3. Which method is used to add an element to the beginning of a list?

- A: my_list.prepend()
- B: my_list.insert(0, element)
- C: my_list.add_first(element)
- D: my_list.insert_first(element)

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: my_list.insert(0, element)

</p>
</details>

###### 4. What is the result of len([1, 2, 3] + [4, 5])

- A: 2
- B: 15
- C: Error
- D: 5

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 5

</p>
</details>

###### 5. What is the output of the following code snippet?

```python
my_list = ['a', 'b', 'c']
result = my_list * 2
print(result)
```

- A: ['a', 'b', 'c', 'a', 'b', 'c']
- B: ['a', 'a', 'b', 'b', 'c', 'c']
- C: ['a', 'b', 'c', 2]
- D: ['a', 'b', 'c', '2']

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: ['a', 'b', 'c', 'a', 'b', 'c']

</p>
</details>

###### 6. How do you check if a specific value exists in a list?

- A: if my_list.contains(value):
- B: if my_list.has(value):
- C: if value in my_list:
- D: if my_list.index(value):

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: if value in my_list:

</p>
</details>

###### 7. Which method is used to insert an element at a specific index in a list?

- A: my_list.insert(index, element)
- B: my_list.add(index, element)
- C: my_list.insert_at(index, element)
- D: my_list.put(index, element)

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: my_list.insert(index, element)

</p>
</details>

###### 8. How do you create a list of numbers from 0 to 9 using a single line of code?

- A: number_list = [0:9]
- B: number_list = range(10).to_list()
- C: number_list = list(range(10))
- D: number_list = [range(10)]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: number_list = list(range(10))

</p>
</details>

###### 9. How do you check if a list is empty?

- A: if my_list.empty():
- B: if len(my_list) == 0:
- C: if not my_list:
- D: if my_list.is_empty():

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: if not my_list:

</p>
</details>

###### 10. What is the output of the following code?

```python
my_list = [1, 2, 3, 4, 5]
my_list.pop(2)
print(my_list)
```

- A: [1, 2, 4, 5]
- B: [1, 2, 3, 4, 5]
- C: [1, 3, 4, 5]
- D: [2, 3, 4, 5]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: [1, 2, 4, 5]
</p>
</details>


###### 11. BONUS QUESTION -> What is the output of the following Python code?

```python
words = ['apple', 'banana', 'cherry', 'date']
result = []
for word in words:
    if len(word) > 5:
        result.append(word[::-1])

print(result)

```

- A: ['ananab', 'yrrehc']
- B: ['elppa', 'ananab', 'yrrehc', 'etad']
- C: ['banana', 'cherry', 'date']
- D: ['elppa', 'ananab', 'yrrehc']

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What is the output of the following Python code?

```python
original_list = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, original_list)
result = list(doubled)

```

- A: [2, 4, 6, 8, 10]
- B: [1, 2, 3, 4, 5, 2, 4, 6, 8, 10]
- C: [1, 2, 4, 8, 16]
- D: [2, 4, 8, 16, 32]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 13. 😈 DEVIL QUESTION 😈

```python
original_list = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, original_list)
result = list(doubled)

```

- A: ['powerful', 'python', 'language']
- B: ['language', 'powerful', 'python']
- C: ['powerful', 'language', 'python']
- D: ['powerful', 'language', 'python', 'is', 'a']

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 14. 😈 DEVIL QUESTION 😈

```python
numbers = [2, 4, 6, 8, 10]
result = [i for i in numbers if all(i % j != 0 for j in range(2, i))]

```

- A: [2, 4, 6, 8, 10]
- B: []
- C: [2]
- D: [10]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 15. 😈 INSANE DIFFICULTY QUESTION 😈

```python
my_list = [2, 4, [6, 8, [10, 12, [14, 16]]]]
result = my_list[2][2][2][1]
my_list[2][2].append(18)
flattened = sum([i if isinstance(i, list) else [i] for i in my_list[2][2]], [])
final_result = flattened[-2]
print(result, final_result)
```

- A: 16 18
- B: 16 14
- C: 14 18
- D: 16 16

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me, explain the code :)) 

</p>
</details>
