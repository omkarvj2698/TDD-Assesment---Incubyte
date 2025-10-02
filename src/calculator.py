class Calculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if "," not in numbers and "\n" not in numbers:
            return int(numbers)

        # general: split on comma, sum all
        parts = numbers.split(",")
        return sum(int(p) for p in parts)