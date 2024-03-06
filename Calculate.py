import re
from typing import List

class StringCalculator:
    def Calculate(self, arg: str) -> int:
        if not arg:
            return 0

        # Check if custom delimiter is provided
        delimiter = ','
        if arg.startswith("//"):
            delimiter_end = arg.index("\n")
            delimiter = arg[2:delimiter_end]
            arg = arg[delimiter_end + 1:]

        # Split numbers based on delimiter
        numbers = self._split_numbers(arg, delimiter)

        # Handle negative numbers
        negatives = [int(num) for num in numbers if int(num) < 0]
        if negatives:
            raise ValueError("Negatives not allowed: " + ", ".join(map(str, negatives)))

        # Ignore numbers greater than 1000
        numbers = [int(num) for num in numbers if int(num) <= 1000]

        return sum(numbers)


    def _split_numbers(self, arg: str, delimiter: str) -> List[str]:
        # Handle multiple delimiters
        if "[" in delimiter and "]" in delimiter:
            delimiters = re.findall(r'\[(.*?)\]', delimiter)
            for d in delimiters:
                arg = arg.replace(d, delimiter)
                numbers = re.split(r'[' + re.escape(delimiter) + r'\n]', arg)
        else:
        # Handle default delimiters
            numbers = re.split(r'[' + re.escape(delimiter) + r'\n]', arg)

        # Filter out empty strings
        numbers = [num for num in numbers if num]
        return numbers
