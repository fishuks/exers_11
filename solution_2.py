class Product:
    """
    Class representing a product.

    Attributes:
        _barcode (str): The product's barcode.
        _price (float): The price of the product.
        _country_code (str): The country code of the manufacturer.
    """
    def __init__(self, barcode, price, country_code):
        """
        Initializes an instance of the Product class.

        Args:
            barcode (str): The product's barcode.
            price (float): The price of the product.
            country_code (str): The country code of the manufacturer.
        """
        self._barcode = barcode
        self._price = price
        self._country_code = country_code
    
    @property
    def barcode(self):
        """
        Get the barcode of the product.

        Returns:
            int: The barcode of the product.
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """
        Set a new barcode for the product.

        Args:
            barcode (int): The new barcode to set for the product.
        """
        self._barcode = barcode

    @property
    def price(self):
        """
        Get the price of the product.

        Returns:
            float: The price of the product.
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Set a new price for the product.

        Args:
            price (float): The new price to set for the product.
        """
        self._price = price

    @property
    def country_code(self):
        """
        Get the country_code of the product.

        Returns:
            str: The country_code of the product.
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Set a new country_code for the product.

        Args:
            country_code (str): The new price to set for the product.
        """
        self._country_code = country_code

class ShoppingCart:
    """
    Class representing a shopping cart.

    Attributes:
        _file_name (str): The file name for saving cart data.
        _products (list): List of products in the cart.
    """
    def __init__(self, file_name):
        """
        Initializes an instance of the ShoppingCart class.

        Args:
            file_name (str): The file name for saving cart data.
        """
        self._file_name = file_name
        self._products = []

    def load_data(self):
        """
        Load data to the shopping cart.

        Returns :
                None
        """
        with open(self._file_name, 'r') as file:
            for line in file:
                barcode, price, country_code = line.strip().split(',')
                self._products.append(Product(barcode, float(price), country_code))
        

    def save_data(self):
        """
        Save data to the shopping cart.

        Returns :
                None
        """
        with open(self._file_name, 'w') as file:
            for product in self._products:
                file.write(f"{product.barcode},{product.price},{product.country_code}\n")

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        Args:
            product (Product): The product to add to the cart.
        """
        self._products.append(product)

    def remove_product(self, barcode):
        """
        Remove a product to the shopping cart.

        Args:
            barcode (int): The product to remove to the cart.
        """
        for product in self._products:
            if product.barcode == barcode:
                self._products.remove(product)
                return

    def get_total_price(self):
        """
        Calculate the total price of all products in the cart.

        Returns:
            float: The total price of all products in the cart.
        """
        return sum(product.price for product in self._products)
    
def main():
    """
    Main program function for managing the shopping cart.
    """
    cart = ShoppingCart('shopping_cart.txt')

    while True:
        print("1. Загрузить данные")
        print("2. Сохранить данные")
        print("3. Добавить товар")
        print("4. Удалить товар")
        print("5. Вывести общую стоимость")
        print("6. Выход")

        choice = input("Выберите действие: ")
        if choice == '1':
            cart.load_data()
            print('Данные загружены')
        elif choice == '2':
            cart.save_data()
            print('Данные сохранены')
        elif choice == '3':
            barcode = input("Введите штрих-код: ")
            price = float(input("Введите цену: "))
            country_code = input("Введите код страны производителя: ")
            cart.add_product(Product(barcode, price, country_code))
        elif choice == '4':
            barcode = input("Введите штрих-код товара для удаления: ")
            cart.remove_product(barcode)
        elif choice == '5':
            print(f"Общая стоимость: {cart.get_total_price()}")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
