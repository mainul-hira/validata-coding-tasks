from decimal import Decimal, InvalidOperation


class ShoppingCart:
    def __init__(self):
        """
        cart_items will store items in this format:
        {
            "item_id": {
                "name": name,
                "price": price,
                "quantity": quantity
            }
        }
        """
        self.cart_items: dict[int, dict[str, str | Decimal | int]] = {}

    @staticmethod
    def _validate_amount_decimal(amount: float) -> (bool, Decimal):
        try:
            amount_str = str(amount)
            amount_decimal = Decimal(amount_str)
            if "." not in amount_str:
                return True, amount_decimal
            if len(amount_str.split(".")[1]) > 2:
                return False, amount_decimal
            return True, amount_decimal
        except InvalidOperation:
            return False, Decimal(0)

    def add_item(self, item_id: int, item_name: str, price: float, quantity: int = 1) -> None:
        is_valid, price_decimal = self._validate_amount_decimal(price)
        if not is_valid:
            raise ValueError("Price must be a decimal number with at most two decimal places.")
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError("Quantity must be a positive integer.")

        if item_id in self.cart_items:
            self.cart_items[item_id]["quantity"] += quantity
        else:
            self.cart_items[item_id] = {"name": item_name, "price": price_decimal, "quantity": quantity}
        
        print(f"Added {quantity} x {item_name} to the cart.")

    def remove_item(self, item_id: int, quantity: int = 1) -> None:
        if item_id not in self.cart_items:
            print(f"{item_id} is not in the cart.")
            return

        if quantity >= self.cart_items[item_id]["quantity"]:
            # Remove the item completely
            del self.cart_items[item_id]
            print(f"Removed {item_id} from the cart.")
        else:
            # Reduce only the specified quantity
            self.cart_items[item_id]["quantity"] -= quantity
            print(f"Removed {quantity} x {self.cart_items[item_id]['name']} from the cart.")

    def calculate_total_cost(self) -> Decimal:
        total = 0
        for item_data in self.cart_items.values():
            total += item_data["price"] * item_data["quantity"]
        return total

    def display_cart(self) -> None:
        if not self.cart_items:
            print("Cart is empty.")
            return
        
        print("\n----- Shopping Cart -----")
        for item_id, data in self.cart_items.items():
            print(f"{item_id}: {data['name']} - {data['quantity']} x {data['price']} = {data['quantity'] * data['price']}")
        
        print(f"Total Cost: ${self.calculate_total_cost()}")
        print("-------------------------\n")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(1, "Item 1", 20.50, 2)
    cart.add_item(2, "Item 2", 20.00, 1)
    cart.display_cart()
    cart.remove_item(1, 1)
    cart.display_cart()
    print(f"Total Cost: ${cart.calculate_total_cost()}")