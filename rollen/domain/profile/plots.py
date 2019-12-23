import seaborn as sns
import matplotlib.pyplot as plt
import logging

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
        cvc.plot_shft_crn("{}$mm$".format(wid))

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
        plt.text(shft + 10, cvc.calc_crns(shft), "{}mm".format(shft))

    plt.legend()

    plt.title("{}产线 F{}机架 $Cmax$={}$mm$ $Cmin$={}$mm$".format(
        line, std, cvc.max_crn, cvc.min_crn))
    plt.xlabel("窜辊位置($mm$)")
    plt.ylabel("辊缝凸度( $\mu m$)")

    plt.savefig("plot_shfts_crns.png")
    plt.close("all")


def plot_shft_crn_optimized(line, std, wid, max_crn, min_crn):
    plt.figure()

    old_cvc = ContinuouslyVariableCrown(line, std, wid)
    new_cvc = ContinuouslyVariableCrown(line, std, wid, max_crn, min_crn)

    old_cvc.plot_shft_crn(label="改进前窜辊-凸度对应关系")
    new_cvc.plot_shft_crn(label="改进后窜辊-凸度对应关系")
    logging.info(new_cvc.max_crn)
    logging.info(new_cvc.min_crn)

    old_coefs = [round(x, 16) for x in old_cvc.get_prof_coefs()]
    new_coefs = [round(x, 16) for x in new_cvc.get_prof_coefs()]
    logging.info(new_coefs)

    plt.text(-150, -50, "原a1={}\n原a2={}\n原a3={}\n".format(
        old_coefs[1], old_coefs[2], old_coefs[3]))
    plt.text(50, -200, "新a1={}\n新a2={}\n新a3={}\n".format(
        new_coefs[1], new_coefs[2], new_coefs[3]))

    plt.legend()

    plt.title("{}产线 F{}机架 宽度{}$mm$ 新$Cmax$={}$mm$ 新$Cmin$={}$mm$".format(
        line, std, wid, max_crn, min_crn))

    plt.xlabel("窜辊位置($mm$)")
    plt.ylabel("辊缝凸度( $\mu m$)")
    plt.savefig("plot_shft_crn_optimized.png")
    plt.close("all")


def plot_cvc_profs(line, std, wid,
                   shfts, linestyles,
                   max_crn=None, min_crn=None):
    plt.figure()

    cvc = ContinuouslyVariableCrown(line, std, wid, max_crn, min_crn)

    cvc.plot_profs(shfts, linestyles)

    plt.legend()

    plt.title("{}产线 F{}机架 宽度{}$mm$ $Cmax$={}$mm$ $Cmin$={}$mm$".format(
        line, std, wid, cvc.max_crn, cvc.min_crn))

    plt.xlabel("辊身长度($mm$)")
    plt.ylabel("CVC辊缝形状相对位置($mm$)")

    plt.savefig("plot_cvc_profs.png")
    plt.close("all")
