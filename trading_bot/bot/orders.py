from bot.client import BinanceClient
import logging

class OrderManager:
    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(f"Placing order: {symbol}, {side}, {order_type}, {quantity}, {price}")

            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce='GTC'
                )
            else:
                raise ValueError("Invalid order type")

            logging.info(f"Order Response: {order}")
            return order

        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return {"error": str(e)}