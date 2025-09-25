# Toy Store with Stock Management 🏪
toyss = {
    "🚗car": {"price": 300, "stock": 5},
    "🧸doll": {"price": 200, "stock": 3},
    "⚽ball": {"price": 500, "stock": 10},
    "🤖robot": {"price": 2000, "stock": 2},
    "🧩puzzle": {"price": 100, "stock": 4},
    "🔫gun": {"price": 700, "stock": 9}
}

toys = {
    "car": {"price": 300, "stock": 5},
    "doll": {"price": 200, "stock": 3},
    "ball": {"price": 500, "stock": 10},
    "robot": {"price": 2000, "stock": 2},
    "puzzle": {"price": 100, "stock": 4},
    "gun": {"price": 700, "stock": 9}
}

print("🎉 Welcome to Jalil's Toy Store 🎉")

while True:
    if not toys:
        print("😅 All toys sold out! Store is empty now.")
        break

    print("\n Available Toys:")
    for name, info in toyss.items():
        print(f"- {name.title()} : ₹{info['price']} ({info['stock']} in stock)")

    toy_name = input("\n👉 Enter the toy you want to buy (or 'exit' to leave): ").lower()
    if toy_name == 'exit':
        print("👋 Thanks for visiting! Come again!")
        break

    if toy_name not in toys:
        print("❌ Toy not found. Try again.")
        continue

    try:
        money = int(input("💰 How much money do you have? ₹"))
        qty = int(input("🔢 How many do you want to buy? "))
        toy = toys[toy_name]

        if qty > toy["stock"]:
            print(f"⚠️ Sorry! Only {toy['stock']} {toy_name}(s) left.")
            continue

        total = qty * toy["price"]

        if money >= total:
            change = money - total
            toy["stock"] -= qty
            print(f"\n✅ You bought {qty} {toy_name}(s) for ₹{total}")
            print(f"💵 Change left: ₹{change}")

            # Remove toy if stock is now 0
            if toy["stock"] == 0:
                print(f"📦 {toy_name.title()} is now out of stock and removed from the store.")
                del toys[toy_name]

        else:
            print(f"🚫 Not enough money. You need ₹{total}, but you only have ₹{money}.")

    except ValueError:
        print("⚠️ Invalid input. Please enter numbers only.")
