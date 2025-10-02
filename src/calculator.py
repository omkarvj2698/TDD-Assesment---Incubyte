class Calculator:
    DEFAULT_DELIMITERS = [",", "\n"]

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if all(d not in numbers for d in self.DEFAULT_DELIMITERS):
            return int(numbers)

        parts = self._split(numbers, self.DEFAULT_DELIMITERS)
        return sum(int(p) for p in parts if p != "")

    def _split(self, s: str, delims):
        primary = delims[0]
        temp = s
        for d in delims[1:]:
            temp = temp.replace(d, primary)
        return temp.split(primary)
