# two functions, that will calculate calories from menue orders from two dicts 

menue_dict = {
  "Hamburger": 250,
  "Cheese Burger": 300,
  "Big Mac": 540,
  "McChicken": 350,
  "French Fries": 230,
  "Salad": 15,
  "Coca Cola": 150,
  "Sprite": 150,
}

combo_dict = {
  "Happy Meal": ['Cheese Burger', 'French Fries', 'Coca Cola'],
  "Best Of Big Mac": ['Big Mac', 'French Fries', 'Coca Cola'],
  "Best Of McChicken": ['McChicken', 'Salad', 'Sprite']
}

def advanced_calories_counter(orders, calorie_sum = 0):#
    for ele in orders:
        if (ele not in combo_dict) & (ele not in menue_dict):
            return f'{ele} not found'
        else:
            if ele in combo_dict:
                print('to be searched in the combo_dict')
                for item in combo_dict[ele]:
                    print(item)
                    calorie_sum += menue_dict[item]
            if ele in menue_dict:
                print('so be searched in menue')
                calorie_sum += menue_dict[ele]
    return calorie_sum

def poor_calories_counter(meal1, meal2, meal3):
    if meal1 not in menue_dict:
        return f'{meal1} not found'
    if meal2 not in menue_dict:
        return f'{meal2} not found'
    if meal3 not in menue_dict:
        return f'{meal3} not found'
    else:
        return menue_dict[meal1]+menue_dict[meal2]+menue_dict[meal3]

print(poor_calories_counter("McChicken", "French Fries", "Sprite"))

print(advanced_calories_counter(["French Fries", "Happy Meal", "Sprite", "Best Of McChicken"]))