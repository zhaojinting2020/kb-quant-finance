#
# Python Script to Simulate a
# Financial Tick Data Server
#
# Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
import zmq
import math
import time
import random
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://0.0.0.0:5555')


class InstrumentPrice(object):
    def __init__(self):
        self.symbol = 'SYMBOL'
        self.t = time.time()
        self.value = 100.
        self.sigma = 0.4
        self.r = 0.01

    def simulate_value(self):
        ''' Generates a new, random stock price.
        '''
        t = time.time()
        seconds_per_trading_year = 252 * 8 * 60 * 60
        dt_scale = 500  # arbitrary factor to amplify price moves for the demo
        dt = (t - self.t) / seconds_per_trading_year
        dt *= dt_scale
        self.t = t
        self.value *= math.exp((self.r - 0.5 * self.sigma ** 2) * dt +
                               self.sigma * math.sqrt(dt) * random.gauss(0, 1))
        return self.value


ip = InstrumentPrice()

while True:
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    msg = '{} {} {:.2f}'.format(ts, ip.symbol, ip.simulate_value())
    print(msg)
    socket.send_string(msg)
    time.sleep(random.random() * 2)
