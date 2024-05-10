import shopping_cart as shopping_cart


def main():
    shop = shopping_cart.ShoppingCart()
    while True:
        print('1) Добавить продукт в корзину')
        print('2) Удалить продукт из корзины')
        print('3) Посмотреть стоимость корзины')
        print('4) Сохранить корзину в файл')
        print('5) Узнать страну производителя')
        print('6) Выйти')
        print()

        choice = input('Введите номер: ')

        if choice == '1':
            name = input('Введите название продукта: ')
            price = float(input('Введите цену продукта: '))
            barcode = int(input('Введите код продукта: '))

            product = shopping_cart.Product(barcode, name, price)
            shop.add_product(product)

        elif choice == '2':
            barcode = int(input('Введите код продукта, который хотите удалить: '))
            shop.remove_product(barcode)

        elif choice == '3':
            print(f'Текущая стоимость: {shop.get_total_cost()} руб.')

        elif choice == '4':
            shop.save_file('shop_basket.txt')

        elif choice == '5':
            barcode = int(input('Введите код продукта: '))
            print(shopping_cart.Product.country(barcode))

        elif choice == '6':
            break


if __name__ == main():
    main()