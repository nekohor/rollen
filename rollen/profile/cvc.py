import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from .std import Stand
from .roll import Roll


sns.set(color_codes=True)
sns.set(rc={'font.family': [u'Microsoft YaHei']})
sns.set(rc={'font.sans-serif': [u'Microsoft YaHei', u'Arial',
                                u'Liberation Sans', u'Bitstream Vera Sans',
                                u'sans-serif']})
# mpl.style.use('ggplot')


class ContinuouslyVariableCrown():

    def __init__(self, line, std, wid,
                 max_crn=None, min_crn=None,
                 side_diam_diff=None,
                 central_diam_diff=None
                 ):

        self.line = line
        self.std = std
        self.wid = wid

        self.stand = Stand()
        self.roll = Roll(line)

        self.abs_max_strock = 150

        self.edge_drop = 40

        self.max_crn = self.get_max_crn(max_crn)
        self.min_crn = self.get_min_crn(min_crn)

        self.side_diam_diff = side_diam_diff
        self.central_diam_diff = central_diam_diff

    def get_max_strock(self):
        return self.abs_max_strock

    def get_min_strock(self):
        return - self.abs_max_strock

    def get_shft_array(self):
        return np.arange(
            self.get_min_strock(),
            self.get_max_strock() + 1)

    def get_default_max_crn(self, std):
        if std in self.stand.upstreams:
            return 0.3
        elif std in self.stand.downstreams:
            return 0.3
        else:
            raise Exception("wrong std not in Stand.stds")

    def get_max_crn(self, max_crn):
        if max_crn:
            return max_crn
        else:
            return self.get_default_max_crn(self.std)

    def get_default_min_crn(self, std):
        if std in self.stand.upstreams:
            return -0.9
        elif std in self.stand.downstreams:
            return -0.5
        else:
            raise Exception("wrong std not in Stand.stds")

    def get_min_crn(self, min_crn):
        if min_crn:
            return min_crn
        else:
            return self.get_default_min_crn(self.std)

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

    def get_prof_coefs(self):

        L = self.roll.get_half_len()

        Smax = self.get_max_strock()
        Smin = self.get_min_strock()

        Cmax = self.max_crn
        Cmin = self.min_crn

        # delta_s = -Sm * (Cmin + Cmax) / (Cmin - Cmax)
        a3 = (Cmin - Cmax) / (6 * L * L * (Smin - Smax))
        a2 = - (Cmin / (2 * L * L)) + 3 * a3 * (Smin - L)

        if self.side_diam_diff:
            diff = self.side_diam_diff
            a1 = (diff - 8 * a2 * L * L - 4 * a3 * L) / (4 * L)
        elif self.central_diam_diff:
            diff = self.central_diam_diff
            a1 = a2 * a2 / a3 / 3 - 3 / 4 * pow(diff, 2 / 3) * pow(a3, 1 / 3)
        else:
            b = self.get_default_half_wid()
            a1 = - 2 * a2 * L - 3 * a3 * L * L - a3 * b * b

        return [0, a1, a2, a3]

    def get_prof_fit(self):
        return np.poly1d(self.get_prof_coefs()[::-1])

    def get_crn(self, pos_shft):

        Lwr = self.roll.get_len()
        L = self.roll.get_half_len()
        b = self.get_half_wid(self.wid)

        Ps = L - pos_shft
        Psb = L + pos_shft

        p = self.get_prof_fit()
        D = p(Lwr)

        Hc = D - p(Lwr - Psb) - p(Ps)
        Hd = D - p(Lwr - (Psb + b)) - p(Ps + b)
        Ho = D - p(Lwr - (Psb - b)) - p(Ps - b)

        # crown negative value and with um
        # Note that the crown is roll crown, not the strip crown
        crn = -1 * (Hc - 0.5 * (Hd + Ho)) * 1000

        return crn

    def get_crn_array(self):
        crn_array = np.array([])
        for shft in self.get_shft_array():
            crn_array = np.append(crn_array, self.get_crn(shft))
        return crn_array

    def get_curve_shft_crn(self):
        p = np.polyfit(self.get_shft_array(),
                       self.get_crn_array(), 1)
        return p

    def get_curve_crn_shft(self):
        p = np.polyfit(self.get_crn_array(),
                       self.get_shft_array(), 1)
        return p

    def calc_shfts(self, crns):
        return np.polyval(self.get_curve_crn_shft(), crns)

    def calc_crns(self, shfts):
        return np.polyval(self.get_curve_shft_crn(), shfts)

    def plot_shft_crn(self, label):
        plt.plot(self.get_shft_array(),
                 self.calc_crns(self.get_shft_array()),
                 label=label)

    def plot_profs(self, shfts, linestyles):
        roll_len_array = np.arange(self.roll.get_len())

        p = self.get_prof_fit()

        i = 0
        for shft in shfts:
            plt.plot(roll_len_array, p(roll_len_array + shft) + 0.2,
                     linestyles[i], label="窜辊位置{}$mm$".format(shft))
            plt.plot(roll_len_array, p(roll_len_array - shft) - 0.2,
                     linestyles[i], label=None)
            i = i + 1
