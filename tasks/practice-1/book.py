book_inventory = {}

def book_add():
    title = input("title: ")
    
    if title in book_inventory:
        print('Book already exists, incrementing the value..')
        book_inventory[title]['Quantity'] +=1
        print(f'Book {title} added successfully')
        
        ch = int(input("Press 3 to display inventory\n 0 to exit"))
        if ch:
            view_inventory()
        else:
            exit()
            
        
    else:
        author = input("author: ")
        genre = input("genre: ")
        qty = int(input("quantity: "))
        price = int(input("price: "))
    book_inventory.update({title: {'Author': author, 'Genre': genre, 'Quantity': qty, 'Price': price}})
    print(f'Book {title} added successfully')
    
    ch = int(input("Press 3 to display inventory\n 0 to exit"))
    if ch:
        view_inventory()
    else:
        exit()


def book_sell():
    title = input('title: ')
    
    if title in book_inventory:
        print(f'available quantity of {title} is {book_inventory[title]['Quantity']}\n')
        available = book_inventory[title]['Quantity']
        
        if(available > 0):
            units = int(input("How many units you wish to sell? "))
                
            if(units <=available):
                book_inventory[title]['Quantity'] -= units
                print(f'{units} of {title} sold successfully!')
                
                if(book_inventory[title]['Quantity'] == 0):
                    del book_inventory[title]
                    print(f'{units} of {title} sold successfully!')
        
        else:
            if(units>available):
                print('Quantity to be sold is greater than available units, Please try again!')
            else:
                print('Quantity to be sold is lesser than available units, Please try again!')
    else:
        print(f'{title} not found, please ensure you typed the title correctly')
    
    ch = int(input("Press 3 to display inventory\n 0 to exit"))
    if ch:
        view_inventory()
    else:
        exit()  


def view_inventory():
    print('=' * (len('INVENTORY')+2) + '\n' 
      "INVENTORY\n" +
      '=' * (len('INVENTORY')+2))
    print('\n')
    print(book_inventory)
    
    
def search_book():
    title = input("title: ")
    
    if title in book_inventory:
        print(f"Book information for {title}:\n{book_inventory[title]}")
    else:
        print(f"Book with the title '{title}' not found in the inventory.")
        
    
def total():
    sum = 0
    
    for title, details in book_inventory.items():
        quantity = details.get('Quantity', 0)
        price = details.get('Price', 0)
        total_value += quantity * price

    print(f'Total value of all books: ${total_value:.2f}')



print('=' * (len('BOOK-STORE INVENTORY SYSTEM')+2) + '\n' 
      "BOOK-STORE INVENTORY SYSTEM\n" +
      '=' * (len('BOOK-STORE INVENTORY SYSTEM')+2))

choice = int(input( "1. Add Book\n"
      + "2. Sell Book\n"
      + "3. Display Inventory\n"
      + "4. Search Book\n"
      + "5. Calculate total value\n"
      + "Choose your option: "))

if choice == 1:
    book_add()

elif choice == 2:
    book_sell()

elif choice == 3:
    view_inventory()

elif choice == 4: 
    search_book()

elif choice == 5:
    total()

    