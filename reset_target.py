import time

import cansel_order
import send_order_profit
import variables
import order_info_cansel


def reset_target(qty, exit_price):
    # 利食い指値注文をキャンセル
    cansel_order_id = cansel_order.cancelorder(variables.take_profit_order_id)

    # キャンセル完了するまで待つ
    while True:
        if order_info_cansel.orders_info_cansel(cansel_order_id):
            break
        time.sleep(0.15)

    # 指値返済再注文
    variables.take_profit_order_id = \
        send_order_profit.sendorder_takeprofit(variables.exit_side, qty, variables.margin_trade_type, exit_price)
