import os
import argparse

def read_args():
    # define argument types 
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--k_val', type=int, metavar='', required = False, help="K - Number of clusters. Default: 2")
    parser.add_argument('-d', '--dist_method', type=int, metavar='', required = False, help="Method used to calculated distance between points. Default: 0")
    parser.add_argument('-m', '--max_iter', type=int, metavar='', required = False, help="Maximun number of iterations. Default: 100")
    parser.add_argument('-t', '--test_file', type=str, metavar='', required = False, help="File that contains test data. Default: test.txt")
    parser.add_argument('-c', '--centr_file', type=str, metavar='', required = False, help="File that contains centroid data. Default: centroids.txt")
    parser.add_argument('-p', '--precision', type=float, metavar='', required = False, help="Tolerance precision. Default: 0.001")
    
    # set default values
    p_args = { "k": 2, "d": 0, "m": 100, "t": "test.txt", "c": "centroids.txt", "p": 0.001 }

    # parse arguments if any
    args = parser.parse_args()
    if args.k_val:
        p_args["k"] = int(args.k_val)
    if args.dist_method:
        p_args["d"] = int(args.dist_method)
    if args.max_iter:
        p_args["m"] = int(args.max_iter)
    if args.test_file:
        p_args["t"] = str(args.test_file)
    if args.centr_file:
        p_args["c"] = str(args.centr_file)
    if args.precision:
        p_args["p"] = float(args.precision)

    return p_args