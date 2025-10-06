from pyscript import display 
#Restaurant Ordering System using Python Data types 

#String Data Type 
restaurant_name = "Cafe Paradise"
owner_name = "Sittie Dida-agun"

#Integer Data Type
year_since = 2025 

#Float Data Type 
tax_rate = 0.08 

#Boolean Data Type 
has_delivery = True
is_dine_in = True 
is_takeaway = False

#List Data Type 
product_names = ["ice cream", "cookie", "cake"]
beverages = ["coffee", "oreo frappe"]

#Tuple Data Type 
business_hours = ("10:00 AM", "9:00 PM")

#Dictionary Data Types 
menu = {
    "ice cream": 100.00,
    "cookie": 65.00,
    "cake": 150.00,
    "coffee": 50.00,
    "oreo frappe": 90.00
}

#Set Data Types 
common_allergens = {"nuts", "dairy", "gluten"}

#Displaying restaurant Information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist:", target="heading1") 


#Display Menu Items
display(product_names[0], target="prod1")
display(f"₱{menu['ice cream']: .2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['cookie']: .2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['cake']: .2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['coffee']: .2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['oreo frappe']: .2f}", target="price5")

#Display additional info 
display(f"Open: {business_hours[0]} - {business_hours[1]}", target= "openingHours")

#display order type
display(f"Dine-in Available", target="orderType")