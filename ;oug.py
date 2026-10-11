def graph():
    h = 10
    start_row = 20
    start_column = 25

    for x in range(-h, h + 1):
        y = x**2
        row = start_row - y // 2
        column = start_column + x * 2

        print(f"\033[{row};{column}H*", end="", flush=True)

    print("\033[22;1H")


graph()