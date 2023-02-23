import pandas as pd
import matplotlib.pyplot as plt


from pathlib import Path


class FileAresDeform:
    """ x = Oscillation strain
        y1 = Storage modulus(log)
        y2 = Loss modulus"""

    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name: str = "Amplitude - 1"
        self.skiprows: list = [0, 2]
        self.df: DataFrame = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        return pd.read_excel(self.file_path, sheet_name=self.sheet_name, skiprows=self.skiprows)

    def show_graph(self):
        x = self.df["Oscillation strain"]
        y1 = self.df["Storage modulus"]
        y2 = self.df["Loss modulus"]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Oscillation strain')
        ax1.set_ylabel('Storage modulus', color='r')
        ax1.semilogy(x, y1, color='r', label="G'")
        ax1.legend(loc="center left")

        ax2 = ax1.twinx()
        ax2.set_ylabel('Loss modulus', color='b')
        ax2.plot(x, y2, color='b', label='G"')
        ax2.legend(loc="center right")
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()


class FileAresTempStd:
    """ x = Oscillation strain
        y1 = Storage modulus(log)
        y2 = Loss modulus"""

    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name: str = "Temperature Ramp - 1"
        self.skiprows: list = [0, 2]
        self.df: DataFrame = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        return pd.read_excel(self.file_path, sheet_name=self.sheet_name, skiprows=self.skiprows)

    def show_graph(self):
        x = self.df["Temperature"]
        y1 = self.df["Storage modulus"]
        y2 = self.df["Loss modulus"]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Temperature')
        ax1.set_ylabel('Storage modulus', color='r')
        ax1.semilogy(x, y1, color='r', label="G'")
        ax1.legend(loc="center left")

        ax2 = ax1.twinx()
        ax2.set_ylabel('Loss modulus', color='b')
        ax2.plot(x, y2, color='b', label='G"')
        ax2.legend(loc="center right")
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()


class FileAresTemp2climb:
    """ x = Oscillation strain
        y1 = Storage modulus(log)
        y2 = Loss modulus"""

    def __init__(self, file_path, title_graph):
        self.file_path: Path = file_path
        self.sheet_name1: str = "Temperature Ramp - 1"
        self.sheet_name2: str = "Temperature Ramp - 3"
        self.skiprows: list = [0, 2]
        self.dfs: list = self.load_xls()
        self.title_graph: str = title_graph

    def load_xls(self):
        dfs = []
        df1 = pd.read_excel(self.file_path, sheet_name=self.sheet_name1, skiprows=self.skiprows)
        dfs.append(df1)
        df2 = pd.read_excel(self.file_path, sheet_name=self.sheet_name2, skiprows=self.skiprows)
        dfs.append(df2)
        return dfs

    def show_graph(self):
        x1 = self.dfs[0]["Temperature"]
        y11 = self.dfs[0]["Storage modulus"]
        y12 = self.dfs[0]["Loss modulus"]
        y21 = self.dfs[1]["Storage modulus"]
        y22 = self.dfs[1]["Loss modulus"]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Temperature')
        ax1.set_ylabel('Storage modulus', color='r')
        ax1.semilogy(x1, y11, color='r', label="G' montée 1")
        ax1.semilogy(x1, y21, '--', color='#FF5733', label="G'montée 2")
        ax1.legend(loc="center left")

        ax2 = ax1.twinx()
        ax2.set_ylabel('Loss modulus', color='b')
        ax2.plot(x1, y12, color='b', label='G" montée 1')
        ax2.plot(x1, y22, '--', color='#5790EF', label='G" montée 2')
        ax2.legend(loc="center right")
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()


class FileAresTempMulti:
    """ x = Oscillation strain
        y1 = Storage modulus(log)
        y2 = Loss modulus"""

    def __init__(self, files_path, title_graph, f_name1, f_name2):
        self.files_path = files_path
        self.sheet_name: str = "Temperature Ramp - 1"
        self.skiprows: list = [0, 2]
        self.dfs: list = self.load_xls()
        self.title_graph = title_graph
        self.f_name1 = f_name1
        self.f_name2 = f_name2

    def load_xls(self):
        dfs = []
        for path_file in self.files_path:
            df = pd.read_excel(path_file, sheet_name=self.sheet_name, skiprows=self.skiprows)
            dfs.append(df)
        return dfs

    def show_graph(self):
        x1 = self.dfs[0]["Temperature"]
        y11 = self.dfs[0]["Storage modulus"]
        y12 = self.dfs[0]["Loss modulus"]
        y21 = self.dfs[1]["Storage modulus"]
        y22 = self.dfs[1]["Loss modulus"]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Temperature')
        ax1.set_ylabel('Storage modulus', color='r')
        ax1.semilogy(x1, y11, color='r', label=f"G' {self.f_name1}")
        ax1.semilogy(x1, y21, '--', color='#FF5733', label=f"G' {self.f_name2}")
        ax1.legend(loc="center left")

        ax2 = ax1.twinx()
        ax2.set_ylabel('Loss modulus', color='b')
        ax2.plot(x1, y12, color='b', label=f"G' {self.f_name1}")
        ax2.plot(x1, y22, '--', color='#5790EF', label=f"G' {self.f_name2}")
        ax2.legend(loc="center right")
        plt.title(f"ARESG2 - Déformation - {self.title_graph}")
        plt.show()
