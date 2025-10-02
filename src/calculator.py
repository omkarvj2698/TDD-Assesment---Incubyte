class Calculator:
    DEFAULT_DELIMITERS = [",", "\n"]

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiters = list(self.DEFAULT_DELIMITERS)
        payload = numbers

        # header like: //;\n1;2
        if numbers.startswith("//"):
            header, payload = numbers.split("\n", 1)
            custom = header[2:]
            delimiters.append(custom)

        if all(d not in payload for d in delimiters):
            return int(payload)

        parts = self._split(payload, delimiters)
        return sum(int(p) for p in parts if p != "")

    def _split(self, s: str, delims):
        primary = delims[0]
        temp = s
        for d in delims[1:]:
            temp = temp.replace(d, primary)
        return temp.split(primary)
