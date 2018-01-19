from libs.os import read_args
from libs.algorithms import KMeans
from libs.gui import Scatter


args = read_args()
X = [[1, 2],
     [1.5, 1.8],
     [1, 0.6],
     [5, 8],
     [8, 8],
     [9, 11]]

C = [[1.5, 1.8],
     [8, 8],
     [7, 7]]

alg = KMeans(k=args["k"], max_iter=args["m"], tol=args["p"])
res = alg.cluster(X, C, args["d"])
plot = Scatter(['r.', 'g.', 'b.', 'y.', 'c.', 'm.', 'firebrick', 'lime', 'white', 'black'], "teal")
plot.show(res)