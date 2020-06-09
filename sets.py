# nums = [1,2,3,4,7,9]
# sorted(nums)

# # kalo set gak seesuai abjad tapi ngehilangin yang dobel

# ninjas = {"ryu": "black", "yoshi": "red"}
# ninjas.values()
# set(ninjas.values())

def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts): 
        num = belts.count(belt)
        print(f"There are {num} {belt} belts")

#def ninja_intro(dictionary):
#    for key,val in dictionary.items():
#        print(f"I am {key} and I am a {val} belt")
ninja_belts = {}

while True: 
    ninja_name = input("Enter a ninja name: ")
    ninja_belt = input("Enter a ninja belt: ")
    ninja_belts[ninja_name] = ninja_belt #ninja_name = key, belt = val

    another = input("Add another? (y/n)")
    if another == "y":
        continue
    else: 
        break 

#ninja_intro(ninja_belts)
belt_count(ninja_belts)