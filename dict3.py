# ninja_belts = {"crystal": "red", "ryu": "black"}
# ninja_belts["ryu"]
# "ryu" in ninja_belts
# list(ninja_belts.keys())
# vals = list(ninja_belts.valueS())
# vals.count("black")
# ninja_belts["yoshi"] = "red"
# person = dict(name = "shawn", age=27, height=170)
# person()

def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f"I am {key} and I am a {val} belt")
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

ninja_intro(ninja_belts)