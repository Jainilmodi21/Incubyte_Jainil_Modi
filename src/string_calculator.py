
class StringCalculator:
    def __init__(self):
        self._call_count = 0


    def add(self,numbers: str) -> int:
        self._call_count += 1
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

        
        negatives = []
        for part in parts:
            if not part:
                continue

            number = int(part)

            # if it’s negative, store it
            if number < 0:
                negatives.append(number)

        if negatives:
            # list all negatives in the message
            negative_str = ", ".join(str(n) for n in negatives)
            raise ValueError(f"negatives not allowed: {negative_str}")

        if any(part == "" for part in parts):
            raise ValueError("invalid input")
        # convert to ints and sum
        return sum(int(n) for n in parts)
        

    def get_called_count(self) -> int:
        return self._call_count
