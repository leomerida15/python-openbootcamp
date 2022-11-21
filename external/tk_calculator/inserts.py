from tkinter import END, Entry, Tk


class Insert:

    _I = 0

    _Display: Entry = {}

    def _upI(self, n: int):
        self._I += n

    def __init__(self, display: Entry) -> None:
        self._Display = display

    def addItem(self, item: int) -> None:
        n = len(item)
        self._Display.insert(self._I, item)
        self._upI(n)

    def clear(self):
        self._Display.delete(0, END)
