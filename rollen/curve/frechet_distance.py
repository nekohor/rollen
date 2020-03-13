import numpy as np


class FrechetDistance():

    def __init__(self):

        pass

    def eucl_distance(self, x, y):
        """
        L2-norm between point x and y
        param x: numpy_array
        param y: numpy_array

        return : dist float L2-norm between x and y
        """
        dist = np.linalg.norm(x - y)
        return dist

    def _c(self, ca, i, j, P, Q):

        if ca[i, j] > -1:
            return ca[i, j]
        elif i == 0 and j == 0:
            ca[i, j] = self.eucl_distance(P[0], Q[0])
        elif i > 0 and j == 0:
            ca[i, j] = max(self._c(ca, i - 1, 0, P, Q),
                           self.eucl_distance(P[i], Q[0]))
        elif i == 0 and j > 0:
            ca[i, j] = max(self._c(ca, 0, j - 1, P, Q),
                           self.eucl_distance(P[0], Q[j]))
        elif i > 0 and j > 0:
            ca[i, j] = max(
                min(
                    self._c(ca, i - 1, j, P, Q),
                    self._c(ca, i - 1, j - 1, P, Q),
                    self._c(ca, i, j - 1, P, Q)
                ),
                self.eucl_distance(P[i], Q[j])
            )
        else:
            ca[i, j] = float("inf")

        return ca[i, j]

    def frechet_distance(self, P, Q):
        """
        Compute the discret frechet distance between trajectory P and Q
        param P :px2 numpy_array, trajectory P
        param Q :px2 numpy_array, trajectory Q

        return float, the discret frechet distance between trajectory P and Q

        """
        ca = np.ones((len(P), len(Q)))
        ca = np.multiply(ca, -1)
        return self._c(ca, len(P) - 1, len(Q) - 1, P, Q)


if __name__ == '__main__':
    fs = FrechetDistance()

    dist = fs.frechet_distance([3, 4, 3], [0, 1, 0])
    print(dist)
