from rollen.profile import ContinuouslyVariableCrown
from rollen.profile import plot_shfts_crns


def test_plot_shft_crn():
    line = 1580
    std = 3
    plot_shfts_crns(line, std, [890, 1250, 1400], [40, -40, -110, -140])
