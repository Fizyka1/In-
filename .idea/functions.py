# coding=utf-8
from math import exp
from numpy import zeros

def calc_probability(sim_settings):
    probability = zeros(2)
    probability[0] = exp(sim_settings.field/2)
    probability[1] = exp(-sim_settings.field/2)

    return probability

