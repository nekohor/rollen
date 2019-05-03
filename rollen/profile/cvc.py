import numpy as np
from .std import Stand
from .roll import Roll


class ContinuouslyVariableCrown():

    def __init__(self, line):
        self.line = line

        self.stand = Stand()
        self.roll = Roll(line)

        self.abs_max_strock = 150

        self.edge_drop = 40

    def get_max_strock(self):
        return self.abs_max_strock

    def get_min_strock(self):
        return - self.abs_max_strock

    def get_shft_array(self):
        return np.arange(
            self.get_min_strock,
            self.get_max_strock + 1)

    def get_default_max_crn(self, std):
        if std in self.stand.upstreams:
            return 0.3
        elif std in self.stand.downstreams:
            return 0.3
        else:
            raise Exception("wrong std not in Stand.stds")

    def get_default_min_crn(self, std):
        if std in self.stand.upstreams:
            return -0.9
        elif std in self.stand.downstreams:
            return -0.5
        else:
            raise Exception("wrong std not in Stand.stds")

    def get_default_wid(self):
        if self.line == 1580:
            return 1275
        elif self.line == 2250:
            return 1650
        else:
            raise Exception("wrong line")

    def get_default_half_wid(self):
        return self.get_default_wid() / 2

    def get_half_wid(self, wid):
        return (wid - 2 * self.edge_drop) / 2

    def get_prof_coefs(self,
                       max_crn=None, min_crn=None,
                       side_diam_diff=None,
                       central_diam_diff=None
                       ):
        L = self.roll.get_half_len()

        Smax = self.get_max_strock()
        Smin = self.get_min_strock()

        if max_crn:
            Cmax = max_crn
        else:
            Cmax = self.get_default_max_crn()

        if min_crn:
            Cmin = min_crn
        else:
            Cmin = self.get_default_min_crn()

        # delta_s = -Sm * (Cmin + Cmax) / (Cmin - Cmax)
        a3 = (Cmin - Cmax) / (6 * L * L * (Smin - Smax))
        a2 = - (Cmin / (2 * L * L)) + 3 * a3 * (Smin - L)

        if side_diam_diff:
            diff = side_diam_diff
            a1 = (diff - 8 * a2 * L * L - 4 * a3 * L) / (4 * L)
        elif central_diam_diff:
            diff = central_diam_diff
            a1 = a2 * a2 / a3 / 3 - 3 / 4 * pow(diff, 2 / 3) * pow(a3, 1 / 3)
        else:
            b = self.get_default_half_wid()
            a1 = - 2 * a2 * L - 3 * a3 * L * L - a3 * b * b

        return [0, a1, a2, a3]

    def get_crn(self, wid, pos_shft, coefs):

        Lwr = self.roll.get_len()
        L = self.get_half_len()
        b = self.get_half_wid(wid)

        Ps = L - pos_shft
        Psb = L + pos_shft

        p = np.poly1d(coefs[::-1])
        D = p(Lwr)

        Hc = D - p(Lwr - Psb) - p(Ps)
        Hd = D - p(Lwr - (Psb + b)) - p(Ps + b)
        Ho = D - p(Lwr - (Psb - b)) - p(Ps - b)

        # crown negative value and with um
        # Note that the crown is roll crown, not the strip crown
        crn = -1 * (Hc - 0.5 * (Hd + Ho)) * 1000

        return crn

    def get_crn_array(self, wid, coefs):
        crn_array = np.array([])
        for shft in self.get_shft_array():
            crn_array = np.append(crn_array, self.get_crn(shft, wid, coefs))

    def get_curve(self, wid, max_crn=None, min_crn=None):
