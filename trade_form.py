import entry
import reset_target
import exit_trade
import settings
from tkinter import *
from tkinter import ttk

# 画面作成
tkTrade = Tk()
tkTrade.geometry('300x300')  # 画面サイズの設定
tkTrade.title('scal')  # 画面タイトルの設定

frame0 = ttk.Frame(tkTrade, padding=(10, 20, 10, 10))
frame0.grid()

label0 = ttk.Label(frame0, text='建玉数', padding=(5, 10, 5, 0))
label0.grid(row=0, column=0, sticky=E)

# 建玉数入力
positions = IntVar()
positions.set(settings.qty)
positions_entry = ttk.Entry(
    frame0,
    textvariable=positions,
    width=5,
    justify=RIGHT)
positions_entry.grid(row=0, column=1, sticky=W)

tkTrade.resizable(False, False)
frame1 = ttk.Frame(tkTrade, padding=(10, 0, 10, 0))
frame1.grid()

label1 = ttk.Label(frame1, text='買いTakeProfit', padding=(5, 10, 5, 10))
label1.grid(row=0, column=0, sticky=E)

# 買い利食い幅入力
buy_take_profit = IntVar()
buy_take_profit.set(settings.buy_take_profit_margin)
buy_take_profit_entry = ttk.Entry(
    frame1,
    textvariable=buy_take_profit,
    width=5,
    justify=RIGHT)
buy_take_profit_entry.grid(row=0, column=1, sticky=W)

label3 = ttk.Label(frame1, text='売りTakeProfit', padding=(20, 10, 5, 10))
label3.grid(row=0, column=3, sticky=E)

# 売り利食い幅入力
sell_take_profit = IntVar()
sell_take_profit.set(settings.buy_take_profit_margin)
sell_take_profit_entry = ttk.Entry(
    frame1,
    textvariable=sell_take_profit,
    width=5,
    justify=RIGHT)
sell_take_profit_entry.grid(row=0, column=4, sticky=W)


# click時のイベント
def btn_buy_click():
    entry.entry('2', positions.get(), buy_take_profit.get())


def btn_sell_click():
    entry.entry('1', positions.get(), sell_take_profit.get())


# ボタン
frame2 = ttk.Frame(tkTrade, padding=(10, 5, 10, 0))
frame2.grid()
btnBuy = ttk.Button(
    frame2, text='買い',
    command=btn_buy_click)
btnBuy.grid(row=0, column=0, columnspan=2, sticky=E)
frame2.grid_columnconfigure(3, minsize=50)
btnSell = ttk.Button(
    frame2, text='売り',
    command=btn_sell_click)
btnSell.grid(row=0, column=5, columnspan=2, sticky=E)

frame4 = ttk.Frame(tkTrade, padding=(10, 30, 10, 0))
frame4.grid()

label0 = ttk.Label(frame4, text='再指定指値', padding=(5, 10, 5, 10))
label0.grid(row=0, column=0, sticky=E)

# 再指定指値入力
target_value = IntVar()
target_value.set(0)
target_value_entry = ttk.Entry(
    frame4,
    textvariable=target_value,
    width=10,
    justify=RIGHT)
target_value_entry.grid(row=0, column=1, sticky=W)


def btn_reset_target_click():
    reset_target.reset_target(positions.get(), target_value.get())


frame5 = ttk.Frame(tkTrade, padding=(10, 5, 10, 0))
frame5.grid()
btnRestTarget = ttk.Button(
    frame5, text='返済指値再設定',
    command=btn_reset_target_click)
btnRestTarget.grid(row=0, column=0, sticky=E)


def btn_exit_click():
    exit_trade.exit_trade(positions.get())


frame3 = ttk.Frame(tkTrade, padding=32)
frame3.grid()
btnExit = ttk.Button(
    frame3, text='成行返済',
    command=btn_exit_click)
btnExit.grid(row=0, column=0, sticky=E)

# 画面をそのまま表示
tkTrade.mainloop()
