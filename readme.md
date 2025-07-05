# String Calculator -

## Features Implemented

Each feature was developed using the **Red-Green-Refactor** TDD cycle:

### 1.  Empty String
- Input: `""`
- Output: `0`

### 2. Support for 1 and 2 Numbers
- Input: `"1"` → Output: `1`  
- Input: `"1,2"` → Output: `3`

### 3. Newline as Delimiter
- Input: `"1\n2,3"` → Output: `6`

### 4.  Invalid Input Handling
- Input: `"1,\n"` → Raises: `ValueError("invalid input")`

### 5.  Custom Delimiter
- Input: `"//;\n1;2"` → Output: `3`

### 6.  Negative Numbers Not Allowed
- Input: `"1,-2"` → Raises: `ValueError("negatives not allowed: -2")`

### 7.  Count `add()` Calls
- Method: `get_called_count()` → Returns: Number of times `add()` was invoked

### 8.  Ignore Numbers > 1000
- Input: `"2,1001"` → Output: `2`

### 9.  Delimiters of Any Length
- Input: `"//[***]\n1***2***3"` → Output: `6`

### 10.  Multiple Delimiters
- Input: `"//[*][%]\n1*2%3"` → Output: `6`

### 11.  Multiple Delimiters with Length > 1
- Input: `"//[**][%%]\n1**2%%3"` → Output: `6`

### 12.  Non-Numeric Characters in Input
- Input: `"2,a"` → Raises: `ValueError("Invalid input")`

### 13.  Floating Point Numbers
- Input: `"2,5.5"` → Raises: `ValueError("Invalid input")`

### 14.  Using "[]" as Delimiter or empty delimiter
- Input: `"//[]\n1[]2[]3"` → Output: `Empty delimiter or `[]` delimiter is not allowed`

### 15.  Very Large Numbers
- Input: `"1234567891011"` → Output: `0` (Ignored due to >1000 rule)



