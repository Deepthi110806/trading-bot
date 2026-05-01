import argparse
from bot.orders import OrderManager
from bot.validators import validate_input
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\n📌 Order Request Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        manager = OrderManager()
        response = manager.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n📊 Order Response")
        print(response)

        if "orderId" in response:
            print("\n✅ Order Placed Successfully")
        else:
            print("\n❌ Order Failed")

    except Exception as e:
        print(f"\n⚠ Error: {e}")

if __name__ == "__main__":
    main()