stocks = {
    "laptop": {
        "hp": 20000,
        "dell": 40000,
        "asus": 32000,
        "macbook": 150000
    },
    "mobile": {
        "iphone": 80000,
        "oneplus": 40000,
        "mi": 20000 
    }
}

def show_products(products, range):
    total_items = {}
    for x, y in products.items():
        if(y < range):
            total_items[x] = y

    if(len(total_items)):
        print(f"Available items in this range: {total_items}")
        order_products(total_items, products)
    else:
        print(f"No {product} found in this range {range}...")


def order_products(available_products, products):
    isOrderOkay = input('Do you want to Order yes or no: ').lower()
    if(isOrderOkay == 'yes'):
        order_item = input(f'Which {product} do you want: ')
        if(order_item in available_products):
            print(f"{product} Name is: {order_item} \nPrice is: {stocks[product][order_item]} \nThanks for your Visit!") 
        else:
            print(f"Please enter available {products} product")



product = input("Enter your item name ex:(laptop or mobile) : ").lower()


range = int(input('Enter your max price range: '))
show_products(stocks[product], range)
