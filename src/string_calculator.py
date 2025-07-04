
import re
class StringCalculator:
    def __init__(self):
        self._call_count = 0


    def add(self,numbers: str) -> int:
        self._call_count += 1
        if numbers== "":
            return 0
        
        delimiters = [","]  

        # Check for multiple delimiters: 
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiter_section = header[2:]

            if delimiter_section.startswith("[") and "]" in delimiter_section:
                # Only handle single-character delimiters in brackets
                delimiters = []
                i = 0
                while i < len(delimiter_section):
                    if delimiter_section[i] == "[" and delimiter_section[i+2] == "]":
                        delimiters.append(delimiter_section[i+1])
                        i += 3  
                    else:
                        i += 1
            else:
                # Single-character delimiter: //;\n1;2
                delimiters = [delimiter_section]

        # Normalize newlines to any delimiter (we can pick the first one)
        numbers = numbers.replace("\n", delimiters[0])

        # Manual split 
        parts = [numbers]
        for delim in delimiters:
            temp = []
            for part in parts:
                temp.extend(part.split(delim))
            parts = temp

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
