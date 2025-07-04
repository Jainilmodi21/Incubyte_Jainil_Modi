def add(numbers: str) -> int:
    if numbers== "":
        return 0
    
    #replace \n to "," for delimeter
    numbers = numbers.replace("\n", ",")
    #split string in numbers using "," delimeter
    parts = numbers.split(",")

    if any(part == "" for part in parts):
        raise ValueError("invalid input")
    # convert to ints and sum
    return sum(int(n) for n in parts)
    
