#def greet(name = "john",time = "afternoon"):
#    print(f'Good {time} {name}')

#greet(name="susi")

def area(radius): 
    area = 3.142 * radius * radius
    return area

def vol(area,length):
    vol = area*length
    print (vol)

radius = int(input("Enter a radius : "))
length = int(input("Enter a length : "))

area(radius)
vol(area(radius),length)

