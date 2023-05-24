def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    element_calls = []
    for call in planeteer_calls:
        element_calls.append(call.capitalize() + "!")
    return element_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]

    for string in strings:
        if string in cheeses:
            return string
    return None