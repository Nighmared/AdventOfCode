class InputReader:
    fname: str
    lines: list[str]
    content: str

    def __init__(self, fpath) -> None:
        self.fname = fpath
        with open(fpath, "r", encoding="utf-8") as f:
            self.content = f.read().strip()
            self.lines = self.content.split("\n")
            if self.lines[-1].strip() == "":
                self.lines.pop()
