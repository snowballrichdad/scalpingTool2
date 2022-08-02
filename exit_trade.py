import time

import cansel_order
import variables
import order_info_cansel
import send_order_exit_market


def exit_trade(qty):
    # 利食い指値注文をキャンセル
    cansel_order_id = cansel_order.cancelorder(variables.take_profit_order_id)

    # キャンセル完了するまで待つ
    while True:
        if order_info_cansel.orders_info_cansel(cansel_order_id):
            break
        time.sleep(0.15)

    # 成行返済注文
    send_order_exit_market.send_order_exit_market(variables.exit_side, variables.margin_trade_type, qty)
