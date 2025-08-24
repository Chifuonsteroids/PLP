def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Discount is applied only if discount_percent >= 20.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    # Clear output message
    if discount >= 20:
        print(f"Discount applied! Final Price: {final_price:.2f}")
    else:
        print(f"No discount applied. Final Price: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
