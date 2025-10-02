class Calculator:
    DEFAULT_DELIMITERS = [",", "\n"]

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiters = list(self.DEFAULT_DELIMITERS)
        payload = numbers

        # if headers like: //;\n1;2 or //[%]\n1%2
        if numbers.startswith("//"):
            header, payload = numbers.split("\n", 1)
            custom = header[2:]  # fetch text after //

            # accept either //;\n  OR  //[;]\n
            if custom.startswith("[") and custom.endswith("]"):
                custom = custom[1:-1]  # strip the surrounding brackets
            delimiters.append(custom)

        parts = self._split(payload, delimiters)
        ints = [int(p) for p in parts if p != ""]

        negatives = [n for n in ints if n < 0]
        if negatives:
            raise ValueError("negative numbers not allowed " + ",".join(str(n) for n in negatives))

        return sum(ints)

    def _split(self, s: str, delims):
        primary = delims[0]
        temp = s
        for d in delims[1:]:
            temp = temp.replace(d, primary)
        return temp.split(primary)
