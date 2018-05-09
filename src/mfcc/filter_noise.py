
from moduleCsound import *
addTag(startSyn,startOpt,stopOpt,startIns)
header(nch=2)

# *** Instrument Strings ***
WhiteNoiseString="""
asig rand 0.6
out asig, asig
"""

LowPassString="""
asig rand 0.6
alp  butterlp asig, 1000 ;passing frequencies below 1 KHz
out alp, alp
"""

HighPassString="""
asig rand 0.6
ahp  butterhp asig, 500 ;passing frequencies above 500 Hz
out ahp, ahp
"""

BandPassString="""
asig rand 0.6
abp  butterbp asig, 1000, 100 ;passing band from 950 to 1050 Hz
out abp, abp
"""

BandRejectString="""
asig rand 0.6
abr  butterbr asig, 10000, 10000 ;rejecting band from 5 kHz to 15 kHz
out abr, abr
"""

instrument('White Noise',1,WhiteNoiseString)
instrument('Low Pass',2,LowPassString)
instrument('High Pass',3,HighPassString)
instrument('Band Pass',4,BandPassString)
instrument('Band Reject',5,BandRejectString)

addTag(stopIns,startSco)

# *** Table ***
table('1. Sine wave',1,0,8192,10,1)

# *** Score ***
rem('Noise Filtering Score')
for i in range(5): score(i+1,2*i,2)

addTag(stopSco,stopSyn)
writeRun('Tut25')