from ANNarchy import *

Izhikevich = Neuron(
    parameters = """
        noise = 0.0
        a = 0.2
        b = 0.2
        c = -65.0
        d = 2.0
        v_thresh = 30.0
        i_offset = 0.0
    """, 
    equations = """
        I = g_exc - g_inh + noise * Normal(0.0, 1.0) + i_offset
        dv/dt = 0.04 * v^2 + 5.0 * v + 140.0 - u + I : init = -65.0
        du/dt = a * (b*v - u) : init= -13.0
    """,
    spike = "v > v_thresh",
    reset = "v = c; u += d",
    refractory = 0.0
)
