from solution_2 import *

basket = ShoppingCart('shopping_cart.txt')
basket.add_product(Product(123456789012,10.99,"USA"))
basket.add_product(Product(234567890123,15.49,"UK"))
basket.add_product(Product(345678901234,9.99,"GER"))
basket.add_product(Product(456789012345,12.75,"FR"))
basket.add_product(Product(567890123456,8.49,"ITA"))
basket.add_product(Product(678901234567,14.25,"ESP"))
basket.add_product(Product(789012345678,11.99,"CAN"))
basket.add_product(Product(890123456789,13.50,"AUS"))
basket.add_product(Product(901234567890,19.99,"JPN"))
basket.add_product(Product(112345678901,7.99,"CHN"))
print(basket.get_total_price())  
basket.remove_product(1234567890123)
print(basket.get_total_price())
if __name__ == "__main__":
    main()