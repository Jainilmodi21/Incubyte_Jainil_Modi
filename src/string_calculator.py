
class StringCalculator:
    def __init__(self):
        self._call_count = 0


    def add(self,numbers: str) -> int:
        self._call_count += 1
        if numbers== "":
            return 0
        
        delimiter = ","
        # custom delimiter of any length in format //[...]\n
        if numbers.startswith("//[") and "]\n" in numbers:
            header, numbers = numbers.split("\n", 1)
            delimiter = header[3:-1]  
        elif numbers.startswith("//"):
            # single-char delimiter 
            header, numbers = numbers.split("\n", 1)
            delimiter = header[2:]      

        # normalize newlines to the chosen delimiter
        numbers = numbers.replace("\n", delimiter)

        parts = numbers.split(delimiter)

        
        negatives = []
        valid_numbers = [] 
        for part in parts:
            if not part:
                continue

            number = int(part)

            # if it’s negative, store it
            if number < 0:
                negatives.append(number)
            elif number <= 1000:  
                valid_numbers.append(number)


        if negatives:
            # list all negatives in the message
            negative_str = ", ".join(str(n) for n in negatives)
            raise ValueError(f"negatives not allowed: {negative_str}")

        if any(part == "" for part in parts):
            raise ValueError("invalid input")
        # convert to ints and sum
        return sum(valid_numbers)
        

    def get_called_count(self) -> int:
        return self._call_count
