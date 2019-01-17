import numpy
import talib

high = numpy.random.random(100)
low = numpy.random.random(100)
open = numpy.random.random(100)
close = numpy.random.random(100)
volume = numpy.random.random(100)

import numpy
import talib

from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)

output = talib.MOM(close, timeperiod=5)