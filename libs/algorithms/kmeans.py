from math import sqrt


class KMeans:
    """K Means algorithm that supports different distance calculation methods.
    This is a flat clustering form!
    """

    def __init__(self, k=2, max_iter=100, tol=0.001):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol

    # Main method
    def cluster(self, data, centroids, dist_method=0):
        """Groups the numeric N dimensional points to K clusters

        Args:
            data (float[n][m]): n x m dimensional matrix
            centroids (float[k][m]): k x m dimensional matrix
            dist_method (int, optional): method used to calculatede distace.
                values: 0 -> Euclidean,
                        1 -> Manhattan,
                        2 -> Squared Euclidean,
                        3 -> Chebyshev

        Raises:
            ValueError: If number of centroids is less then K value

        Returns:
            {'pts': {'p': float[m], 'c': int}[m], 'cts': float[k][m]}:
            returns the data with one additional column on the right that specifies the cluster
        """
        if len(centroids) < self.k:
            raise ValueError(
                'Number of centroids must be greater or equal than K.')
        elif len(centroids) > self.k:
            centroids = centroids[:self.k]  # reduce number of centroids

        # Init compare data
        if dist_method == 0:
            closure = self.euclidean
        elif dist_method == 1:
            closure = self.manhattan
        elif dist_method == 2:
            closure = self.squared_euclidean
        else:
            closure = self.chebyshev

        itr = 0
        data_len = len(data)
        attr_len = len(data[0])
        cent_len = len(centroids)
        res = data[0:]

        # Until max iteration is reached
        while itr < self.max_iter:
            i = 0
            # Compare each point with centroids and decide to which centroid the point belongs
            while i < data_len:
                res[i] = {"p": data[i], "c": 0}
                min_dist = closure(data[i], centroids[0])
                j = 1
                while j < cent_len:
                    dist = closure(data[i], centroids[j])
                    if min_dist > dist:
                        min_dist = dist
                        res[i]["c"] = j
                    j += 1
                i += 1

            # Find mean point of each cluster and make them as centroids.
            # This is calculated by finding avg of each dimension in each cluster
            # e.g cluster 0 => C0 = [1/n SUM(p[i][j])];
            #       i=0..n, j=0..m where n is no_points and m is no_dims
            # count of points in a cluster
            cnt_clstr_p = [0 for x in range(cent_len)]
            avg_pts = [[0 for x in range(attr_len)] for y in range(
                cent_len)]  # average distance of each cluster

            k = 0
            while k < data_len:
                clstr_id = res[k]["c"]
                cnt_clstr_p[clstr_id] += 1
                l = 0
                while l < attr_len:
                    avg_pts[clstr_id][l] += res[k]["p"][l]
                    l += 1
                k += 1

            k = 0
            while k < cent_len:
                l = 0
                while l < attr_len:
                    avg_pts[k][l] /= cnt_clstr_p[k]
                    l += 1
                k += 1

            # Test break condition: all dist(centroids, avg_pts) <= tol
            break_loop = True
            k = 0
            while k < cent_len:
                if closure(centroids[k], avg_pts[k]) > self.tol:
                    break_loop = False
                    break
                k += 1

            centroids = avg_pts
            if break_loop:
                break
            itr += 1

        return {"pts": res, "cts": centroids}

    # Methods for calculating the distance
    def euclidean(self, p1, p2):
        """Calculated the euclidean distance between two n dimensional points. 
        Euclidean distance: SQRT(SUM((ai - bi) ^ 2))

        Args:
            p1 (float[n]): n dimensional point 1
            p2 (float[n]): n dimensional point 2

        Returns:
            float: Distance between two points
        """
        return sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))

    def squared_euclidean(self, p1, p2):
        """Calculated the squared euclidean distance between two n dimensional points. 
        Squared Euclidean distance: SUM((ai - bi) ^ 2)

        Args:
            p1 (float[n]): n dimensional point 1
            p2 (float[n]): n dimensional point 2

        Returns:
            float: Distance between two points
        """
        return sum([(a - b) ** 2 for a, b in zip(p1, p2)])

    def manhattan(self, p1, p2):
        """Calculated the manhattan distance between two n dimensional points. 
        Manhattan distance: SUM(|ai - bi|)

        Args:
            p1 (float[n]): n dimensional point 1
            p2 (float[n]): n dimensional point 2

        Returns:
            float: Distance between two points
        """
        return sum([abs(a - b) for a, b in zip(p1, p2)])

    def chebyshev(self, p1, p2):
        """Calculated the chebyshev distance between two n dimensional points.
         Chebyshev distance: MAX(|ai - bi|)

        Args:
            p1 (float[n]): n dimensional point 1
            p2 (float[n]): n dimensional point 2

        Returns:
            float: Distance between two points
        """
        return max([abs(a - b) for a, b in zip(p1, p2)])
