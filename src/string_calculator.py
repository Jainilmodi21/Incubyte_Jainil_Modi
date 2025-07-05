
import re
class StringCalculator:
    def __init__(self):
        self._call_count = 0


    def add(self,numbers: str) -> int:
        self._call_count += 1
        if numbers== "":
            return 0
        
        delimiters = [",", "\n"]  

        # Custom delimiter 
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiter_section = header[2:]

            if delimiter_section.startswith("[") and "]" in delimiter_section:
                # Extract multiple delimiters of any length
                delimiters = []
                temp = ""
                inside_brackets = False
                for char in delimiter_section:
                    if char == "[":
                        inside_brackets = True
                        temp = ""
                    elif char == "]":
                        inside_brackets = False
                        if temp == "":
                            raise ValueError("Empty delimiter or `[]` delimiter is not allowed")
                        delimiters.append(temp)
                    elif inside_brackets:
                        temp += char
            else:
                # Single character delimiter
                delimiters = [delimiter_section, "\n"]
        # Split manually 
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

            #check string contains character that are not number
            try:
                 # check for floating point
                 if not part.isdigit() and not (part.startswith('-') and part[1:].isdigit()):
                        raise ValueError("Invalid input")
                    
                 number = int(part)
            except ValueError:
                raise ValueError("Invalid input")

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
