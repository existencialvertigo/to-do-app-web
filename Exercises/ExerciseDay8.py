while True:
    with open("coin-flip.txt", "r") as file:
        coin_flips = file.readlines()

    user_answer = input("Throw the coin and enter head or tail here: ?") + "\n"

    coin_flips.append(user_answer)

    with open("coin-flip.txt", "w") as file:
        file.writelines(coin_flips)

    heads = coin_flips.count("head\n")
    percentage = heads/len(coin_flips) * 100

    print(f"Heads: {percentage}%")



