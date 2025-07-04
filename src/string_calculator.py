def add(numbers: str) -> int:
    if numbers== "":
        return 0
    
    delim = ","
    # check for custom delimiter syntax 
    if numbers.startswith("//"):
        # split into header and the rest
        header, numbers = numbers.split("\n", 1)
        delim = header[2:]      

    # normalize newlines to the chosen delimiter
    numbers = numbers.replace("\n", delim)

    parts = numbers.split(delim)

    if any(part == "" for part in parts):
        raise ValueError("invalid input")
    # convert to ints and sum
    return sum(int(n) for n in parts)
    
