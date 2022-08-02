import time

import board
import send_order_entry
import order_info
import send_order_profit
import variables


def entry(side, qty, take_profit_margin):
    # 初期化
    variables.take_profit_order_id = ''
    variables.exit_side = ''
    variables.margin_trade_type = 0

    cur_price = board.get_current_price()

    entry_price = 0
    exit_price = 0
    if side == "2":
        # 買いエントリ
        # 金利がかからない一般(デイトレ)
        variables.margin_trade_type = 3
        entry_price = cur_price + 1000

        variables.exit_side = "1"

    else:
        # 売りエントリ
        trade_side = "1"
        # 売りエントリの場合はプレミアム料を取られるので制度信用
        variables.margin_trade_type = 1
        entry_price = cur_price - 1000

        variables.exit_side = "2"

    # エントリ
    entry_order_id = send_order_entry.send_order_entry(side, qty, variables.margin_trade_type, entry_price)

    order_price = 0
    while True:
        # 全約定するまで待つ
        order_price = order_info.orders_info(entry_order_id)
        if order_price is not None:
            break
        time.sleep(0.2)

    if side == "2":
        # 買いエントリ
        exit_price = order_price + take_profit_margin

    else:
        # 売りエントリ
        exit_price = order_price - take_profit_margin

    # 利食い注文
    variables.take_profit_order_id = \
        send_order_profit.sendorder_takeprofit(variables.exit_side, qty, variables.margin_trade_type, exit_price)
