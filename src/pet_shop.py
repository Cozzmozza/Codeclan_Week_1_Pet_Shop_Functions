# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, value):
    pet_shop['admin']['total_cash'] = pet_shop['admin']['total_cash'] + value

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, value):
    pet_shop['admin']['pets_sold'] = pet_shop['admin']['pets_sold'] + value

def get_stock_count(pet_shop):
     return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed_name):
    breed_list = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed_name:
            breed_list.append(breed_name)
    return breed_list

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop['pets']:
        if pet['name'] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
     for pet in pet_shop['pets']:
        if pet['name'] == pet_name:
           pet_shop['pets'].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, value):
    customer['cash'] = customer['cash'] - value

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'] = [new_pet]

def customer_can_afford_pet(customer, new_pet):
    if customer['cash'] >= new_pet['price']:
        return True
    else:
        return False
# Instead of this,c an use the condition, 
    return customer['cash'] >= new_pet['price']
# that'll return true


# Run find pet by name, which will return a dictionary of the pet name, price, etc
# If a pet is found:
#   If customer can afford pet, for this pet name
        # Remove customer cash equal to the pet price DONE
        # Add value to the shops total DONE
        # increase customer pet count by 1
        # increase pets sold by 1
def sell_pet_to_customer(pet_shop, pet, customer):
    if find_pet_by_name(pet_shop, pet) != pet and customer_can_afford_pet(customer, pet):
        # Don't need the == True. Assumes it is true. 
        find_pet_by_name(pet_shop, pet)
        cost = pet['price']
        remove_customer_cash(customer, cost)
        pet_shop['admin']['total_cash'] = pet_shop['admin']['total_cash'] + cost
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        # Missing Remove Pet By Name
        # Should have used add_or_remove_cash instead of total cash

# def sell_pet_to_customer(pet_shop, pet, customer):
#     if pet != None and customer_can_afford_pet(customer, pet):
#         # Mine overly complex? I used find_pet_by_name
#         remove_pet_by_name(pet_shop, pet["name"])
#         # add_pet_to_customer(customer, pet)
#         # remove_customer_cash(customer, pet["price"])
#             # Did this but via variable
#         # add_or_remove_cash(pet_shop, pet["price"])
#         # increase_pets_sold(pet_shop, 1)
