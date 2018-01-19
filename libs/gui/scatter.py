import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


class Scatter:
    """Used to generate 2D scatter from KMeans result
    """

    def __init__(self, clr, cent_clr):
        self.clr = clr
        self.cent_clr = cent_clr

    def show(self, res):
        """Visualises data in 2D

        Args:
            res ({'pts': {'p': float[m], 'c': int}[m], 'cts': float[k][m]}): Data result from KMeans cluster
        """
        style.use('ggplot')
        C = np.array(res["cts"])
        i = 0
        pt_len = len(res["pts"])
        while i < pt_len:
            clstr_id = res["pts"][i]["c"]
            plt.plot(res["pts"][i]["p"][0], res["pts"][i]["p"]
                     [1], self.clr[clstr_id], markersize=10)
            i += 1

        plt.scatter(C[:, 0], C[:, 1], marker="*", c=self.cent_clr, s=150)
        plt.show()
