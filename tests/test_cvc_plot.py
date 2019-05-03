from rollen.profile import plot_shfts_crns
from rollen.profile import plot_shft_crn_optimized
from rollen.profile import plot_cvc_profs


def test_plot_shft_crn():
    line = 1580
    std = 3
    plot_shfts_crns(line, std, [890, 1250, 1400], [40, -40, -110, -140])


def test_plot_shft_crn_optimized():
    line = 1580
    std = 3
    wid = 1250
    new_max_crn = 0.3
    new_min_crn = -0.7
    plot_shft_crn_optimized(line, std, wid, new_max_crn, new_min_crn)


def test_plot_cvc_profs():
    line = 1580
    std = 3
    wid = 1250
    shfts = [40, -110]
    linestyles = ["k", "r--"]
    plot_cvc_profs(line, std, wid, shfts, linestyles)
