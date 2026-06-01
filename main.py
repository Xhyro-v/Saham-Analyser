from api.API import get_stock_data


data = get_stock_data(
    symbol="IDX:CUAN",
    start_date="2026-05-18",
    end_date="2026-05-29"
)

if __name__ == "__main__":
  for d in data:
    print("")
    print(f"{d['datetime']} | O: {d['open']:<8} H: {d['high']:<8} L: {d['low']:<8} C: {d['close']:<8} Vol: {d['volume']}")
    print("")