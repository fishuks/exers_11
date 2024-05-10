import EAN_13


class Product:
    """
    Class of product.

    Args:
        barcode (int): barcode product
        name (str): name product
        price (int): price product
    """

    def __init__(self, barcode, name, price):
        """
        The function initialises an instance of the molecule class.
        :param barcode (int): barcode product
        :param name (str): name product
        :param price (int): price product
        """
        self.__name = name
        self.__price = int(price)
        self.__barcode = int(barcode)

    @property
    def name(self):
        """
        Finction for getting name product.
        :return: name product
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Function for setting name product.
        :param new_name: new name for product
        :return: new name
        """
        self.__name = new_name

    @property
    def price(self):
        """
        Function for getting price product.
        :return: price
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Function for setting price product.
        :param new_price: new price
        """
        self.__price = new_price

    @property
    def barcode(self):
        """
        Function for getting barcode product.
        :return: barcode product
        """
        return self.__barcode

    @barcode.setter
    def barcode(self, new_barcode):
        """
        Function for setting barcode product.
        :param new_barcode: new barcode
        """
        self.__barcode = new_barcode

    @staticmethod
    def country(barcode):
        """
        Function for getting country of priduct.
        :param barcode: barcode of product
        :return: country
        """
        if len(str(barcode)) == 13:
            code_country = str(barcode // 10_000_000_000)
            country = EAN_13.encode_EAN_13[code_country]
            return country
        else:
            return f'Вы ввели неправильный штрих-код'

    def __repr__(self):
        return f'{self.__name}'


class ShoppingCart:
    """
    Class of shopping cart.

    Args:
        __products (list): list of products
        __total_cost (float): value of total cost
    """

    def __init__(self):
        """
        The function initialises an instance of the molecule class.
        """
        self.__products = []
        self.__total_cost = 0

    def get_products(self):
        """
        Function for getting list of products.
        :return: list of products
        """
        return self.__products

    def get_total_cost(self):
        """
        Function for getting total cost of shopping cart.
        :return: total cost
        """
        return self.__total_cost

    def add_product(self, product):
        """
        Function for adding product.
        :param product (Product): product
        """
        self.__products.append(product)
        self.__total_cost += product.price

    def remove_product(self, barcode):
        """
        Function for removing product from shopping cart.
        :param barcode: barcode
        """
        for product in self.__products:
            if product.barcode == barcode:
                self.__products.remove(product)
                self.__total_cost -= product.price

    def load_file(self, filename):
        """
        Function for loading shopping cart in file
        :param filename: filename
        """
        with open(filename, 'r', encoding='utf_8') as file:
            for line in file:
                line = line.split()
                product = Product(line[0], line[1], line[2])
                self.add_product(product)

    def save_file(self, filename):
        """
        Function for saving shopping cart in file.
        :param filename: filename
        """
        data = []
        for product in self.__products:
            data.append(f'{product.barcode} {product.name} {product.price}')

        with open(filename, 'w') as f_out:
            print(data, file=f_out)

    def __str__(self):
        return f'{self.__products}'

    def __repr__(self):
        return self.__str__()