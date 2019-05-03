import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from .cvc import ContinuouslyVariableCrown
sns.set(color_codes=True)
sns.set(rc={'font.family': [u'Microsoft YaHei']})
sns.set(rc={'font.sans-serif': [u'Microsoft YaHei', u'Arial',
                                u'Liberation Sans', u'Bitstream Vera Sans',
                                u'sans-serif']})


def plot_shfts_crns(line, std, wids, shfts, max_crn=None, min_crn=None):
    plt.figure()

    for wid in wids:
        cvc = ContinuouslyVariableCrown(line, std, wid, max_crn, min_crn)
        cvc.plot_shft_crn()

    cvc = ContinuouslyVariableCrown(line, std, wids[1], max_crn, min_crn)

    plt.scatter(
        shfts,
        cvc.calc_crns(shfts),
        marker="X",
        s=100,
        c="k",
        label="特定窜辊位置"
    )

    # text
    for shft in shfts:
        plt.text(shft, cvc.calc_crns(shft), "{}mm".format(shft))
    plt.legend()

    plt.title("{}产线 F{}机架 $Cmax={}mm$ $Cmin={}mm$".format(
        line, std, cvc.max_crn, cvc.min_crn))
    plt.xlabel("窜辊位置($mm$)")
    plt.ylabel("辊缝凸度( $\mu m$)")

    plt.savefig("plot_shft_crn.png")
    plt.close("all")
