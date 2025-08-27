# 📈 Max Subarray Sum and Length — Kadane’s Algorithm

This Python script implements an enhanced version of **Kadane’s Algorithm** to find the **maximum sum** of a contiguous subarray and the **length** of that subarray. It’s a classic problem in dynamic programming and greedy algorithms, often asked in coding interviews and used in real-world applications like signal processing and financial analysis.

---

## 🚀 Features

- ✅ Efficient **O(n)** time complexity
- ✅ Tracks both **maximum sum** and **subarray length**
- ✅ Handles negative numbers gracefully
- ✅ Easy to integrate into larger projects

---

## 🧠 Algorithm Explanation
This function is based on Kadane’s Algorithm, which uses a greedy approach to solve the maximum subarray problem in linear time.

### 🧠 Step-by-Step Logic:

#### 1. Initialize:
- **max_sum = -∞** to store the best sum found so far
- **current_sum = 0** to track the running sum
- **start, end, temp_start** to track subarray indices

#### 2. Iterate through the array:
- If **current_sum is ≤ 0**, reset it to the current element
- Else, add the current element to **current_sum**

#### 3. Update max_sum:
- If **current_sum** exceeds **max_sum**, update **max_sum** and record the subarray boundaries

#### 4. Compute length:
- **length = end - start + 1**

---

## 🧪 Example

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, 11, 22, -25]
max_sum, length = max_subarray_sum_and_length(arr)
print("Max subarray sum:", max_sum)
print("Number of elements in max subarray:", length)

---

## Output:
Max subarray sum: 47
Number of elements in max subarray: 9

---

## 📊 Time and Space Complexity
Time Complexity : O(n)
Space Complexity : O(1)

---

## 🛠️ Author
Dinesh Kumar Mandal
Passionate about software engineering, web development, and building intelligent apps.
Skilled in Python, Flask, API integration, and algorithmic problem solving.

---

## 📌 License
This project is open-source and free to use under the MIT License.

---

## 📦 Function Signature

```python
def max_subarray_sum_and_length(arr: List[int]) -> Tuple[int, int]
 

