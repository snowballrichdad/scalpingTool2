import sys
# import MySQLdb
from datetime import datetime as dt

port = "18080"


symbol = "1570"
qty = 10
buy_take_profit_margin = 10
buy_stop_loss_margin = 20
sell_take_profit_margin = 10
sell_stop_loss_margin = 20

now_time = dt.now()

exit_time = now_time.replace(hour=14, minute=59)
record_stop_time = now_time.replace(hour=10, minute=0)

# 標準出力をファイルに
tstr = now_time.strftime('%Y%m%d%H%M%S')


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("c:\\data\\" + tstr + ".log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


sys.stdout = Logger()
sys.stderr = Logger()
