from ANNarchy import *

my_STDP = Synapse(
    parameters = """
        tau_pre = 20.0 : projection
        tau_post = 20.0 : projection
        cApre = 0.01 : projection
        cApost = 0.01 : projection
        wmin = -30 : projection
        wmax = 30 : projection
    """,
    pre_spike = """
        g_target += w
        w = clip(w - cApost * exp((t_post - t)/tau_post) , wmin , wmax)

    """,
    post_spike = """
        w = clip(w + cApre * exp((t_pre - t)/tau_pre) , wmin , wmax)
    """
)
