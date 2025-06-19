from string import ascii_uppercase
class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = dict(zip(list(string.ascii_uppercase), [[0 for i in range(rows + 1)] for j in range(26)]))
        print(self.sheet)

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell[0]][int(cell[1:])] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell[0]][int(cell[1:])] = 0

    def getValue(self, formula: str) -> int:
        val1, val2 = formula[1:].split("+")
        if val1[0]
        val1 = self.sheet[val1[0]][int(val1[1:])] if val1[0].isalpha else int(val1)
        val2 = self.sheet[val2[0]][int(val2[1:])] if val2[0].isalpha else int(val2)
        return val1 + val2

        


Spreadsheet = Spreadsheet(3)
getValue