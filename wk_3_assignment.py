# def calculate_discount(price, discount_percent):
#     """
#     Calculate the final price after applying a discount.

#     Args:
#         price (float): The original price.
#         discount_percent (float): The discount percentage.

#     Returns:
#         float: The final price after applying the discount.
#     """

#     if discount_percent >= 20:
#         # Calculate the discount amount
#         discount_amount = (discount_percent / 100) * price
#         # Calculate the final price
#         final_price = price - discount_amount
#         return final_price
#     else:
#         # Return the original price if the discount is less than 20%
#         return price


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

def main():
    # Prompt the user for input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the final price
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: ${price:.2f}")

if __name__ == "__main__":
    main()

