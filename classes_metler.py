import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


class FileMetlerTempE:
    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name: str = "$DGEBA-D230 tpmd"
        self.skiprows: list = [1]
        self.df: DataFrame = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        return pd.read_excel(self.file_path, skiprows=self.skiprows)

    def show_graph(self):
        x = self.df["t"]
        y1 = self.df["E'"]
        y2 = self.df['E"']

        fig, ax = plt.subplots()

        twin1 = ax.twinx()

        p1, = ax.semilogy(x, y1, "C0", label="E'")
        p2, = twin1.semilogy(x, y2, "C1", label='E"')

        ax.set(xlabel="température", ylabel="E'")
        twin1.set(xlabel="température", ylabel='E"')

        ax.yaxis.label.set_color(p1.get_color())
        twin1.yaxis.label.set_color(p2.get_color())

        ax.tick_params(axis='y', colors=p1.get_color())
        twin1.tick_params(axis='y', colors=p2.get_color())

        ax.legend(handles=[p1, p2])
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()


class FileMetlerTempF:
    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name: str = "$DGEBA-D230 tpmd"
        self.skiprows: list = [1]
        self.df: DataFrame = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        return pd.read_excel(self.file_path, skiprows=self.skiprows)

    def show_graph(self):
        x = self.df["t"]
        y1 = self.df["F"]
        y2 = self.df['F0']

        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        twin1 = ax.twinx()

        p1, = ax.semilogy(x, y1, "C0", label="F")
        p2, = twin1.semilogy(x, y2, "C1", label='F0')

        ax.set(xlabel="température", ylabel="F")
        twin1.set(xlabel="température", ylabel='F0')

        ax.yaxis.label.set_color(p1.get_color())
        twin1.yaxis.label.set_color(p2.get_color())

        ax.tick_params(axis='y', colors=p1.get_color())
        twin1.tick_params(axis='y', colors=p2.get_color())

        ax.legend(handles=[p1, p2])
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()
