import numpy as np
import numpy_financial as nf


# future value
'''
# rate => rate of interest in decimal
# nper => time period in years
# pmt  => amount already paid
# pv   => preset value (principle amount) (should be negative)
'''
nf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)


# present value
'''
# rate => rate of interest in decinal
# nper => time period in years
# pmt  => amount already paid
# fv   => future value 
'''
nf.pv(rate=0.08, nper=5, pmt=0, pv=-1000)

# payment per year
'''
# rate => rate of interest in decimal
# nper => number of years
# pv   => present value
# fv   => final value
'''
nf.pmt(rate=0.07/12, nper=5*12, pv=100000, fv=0) 

# Internal Rate of Return (IRR)
'''
# value_list => list contaning the cashflow
'''
l = [-1000, 100, 100, 100, 100, 300, 200]
nf.irr(l)