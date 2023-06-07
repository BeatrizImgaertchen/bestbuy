import store
import products


def start(store_obj):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\nAll Products in Store:")
            all_products = store_obj.get_all_products()
            for product in all_products:
                print(product.show())

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal Amount in Store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                if product_name == "done":
                    break

                product = None
                for prod in store_obj.get_all_products():
                    if prod.name.lower() == product_name.lower():
                        product = prod
                        break

                if product is None:
                    print("Invalid product name. Please try again.")
                    continue

                quantity = int(input("Enter quantity: "))
                shopping_list.append((product, quantity))

            total_price = store_obj.order(shopping_list)
            print(f"Order cost: {total_price} dollars.")

        elif choice == "4":
            print("Thank you for using the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
