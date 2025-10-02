class Calculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        # no delimiter present means single number
        if "," not in numbers and "\n" not in numbers:
            return int(numbers)
        raise NotImplementedError