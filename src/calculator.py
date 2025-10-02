class Calculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if "," not in numbers and "\n" not in numbers:
            return int(numbers)

        # allow both "," and "\n" as delimiters
        normalized = numbers.replace("\n", ",")
        parts = normalized.split(",")
        return sum(int(p) for p in parts if p != "")