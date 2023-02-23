import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


class FileAtFreq:
    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name: str = "PDMS TEST balayage en frequence"
        self.skiprows: list = [0, 1, 2, 3, 4, 5, 6, 8, 9]
        self.df: DataFrame = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        return pd.read_excel(self.file_path, skiprows=self.skiprows,
                             usecols=['Fréquence Angulaire', 'Module de Stockage', 'Module de Perte', 'Couple'])

    def show_graph(self):
        x = self.df["Fréquence Angulaire"]
        y1 = self.df["Module de Stockage"]
        y2 = self.df["Module de Perte"]
        y3 = self.df["Couple"]

        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        twin1 = ax.twinx()
        twin2 = ax.twinx()

        # Offset the right spine of twin2.  The ticks and label have already been
        # placed on the right by twinx above.
        twin2.spines.right.set_position(("axes", 1.2))

        p1, = ax.semilogx(x, y1, "C0", label="Module de Stockage")
        p2, = twin1.semilogx(x, y2, "C1", label="Module de Perte")
        p3, = twin2.semilogx(x, y3, "C2", label="Couple")

        ax.set(xlabel="Fréquence Angulaire", ylabel="Module de Stockage")
        twin1.set(xlabel="Fréquence Angulaire", ylabel="Module de Perte")
        twin2.set(xlabel="Fréquence Angulaire", ylabel="Couple")

        ax.yaxis.label.set_color(p1.get_color())
        twin1.yaxis.label.set_color(p2.get_color())
        twin2.yaxis.label.set_color(p3.get_color())

        ax.tick_params(axis='y', colors=p1.get_color())
        twin1.tick_params(axis='y', colors=p2.get_color())
        twin2.tick_params(axis='y', colors=p3.get_color())

        ax.legend(handles=[p1, p2, p3])
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()


class FileAtEcoul:
    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name: str = "test silicone courbe d'ecouleme"
        self.skiprows: list = [0, 1, 2, 3, 4, 5, 6, 8, 9]
        self.df: DataFrame = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        return pd.read_excel(self.file_path, skiprows=self.skiprows,
                             usecols=['Gradient de Cisaillement', 'Contrainte de Cisaillement', 'Viscosité', 'Couple'])

    def show_graph(self):
        x = self.df["Gradient de Cisaillement"]
        y1 = self.df["Contrainte de Cisaillement"]
        y2 = self.df["Viscosité"]
        y3 = self.df["Couple"]


        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        twin1 = ax.twinx()
        twin2 = ax.twinx()

        # Offset the right spine of twin2.  The ticks and label have already been
        # placed on the right by twinx above.
        twin2.spines.right.set_position(("axes", 1.2))

        p1, = ax.plot(x, y1, "C0", label="Contrainte de Cisaillement")
        p2, = twin1.plot(x, y2, "C1", label="Viscosité")
        p3, = twin2.plot(x, y3, "C2", label="Couple")

        ax.set(xlabel="Gradient de Cisaillement", ylabel="Contrainte de Cisaillement")
        twin1.set(xlabel="Gradient de Cisaillement", ylabel="Viscosité")
        twin2.set(xlabel="Gradient de Cisaillement", ylabel="Couple")

        ax.yaxis.label.set_color(p1.get_color())
        twin1.yaxis.label.set_color(p2.get_color())
        twin2.yaxis.label.set_color(p3.get_color())

        ax.tick_params(axis='y', colors=p1.get_color())
        twin1.tick_params(axis='y', colors=p2.get_color())
        twin2.tick_params(axis='y', colors=p3.get_color())

        ax.legend(handles=[p1, p2, p3])
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()
