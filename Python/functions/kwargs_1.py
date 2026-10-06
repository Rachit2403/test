def address(**kwargs):
    for key in kwargs.keys():
        print(key)
address(Room = 1244, 
        Name = 'Rachit Vyas', 
        Hostel = 'F Block',
        Uni = 'VIT University', 
        City = 'Chennai', 
        State = 'Tamil Nadu', 
        Country = 'India')
print("----------")
print("----------")
print("----------")
def address(**kwargs):
    for val in kwargs.values():
        print(val)
address(Room = 1244, 
        Name = 'Rachit Vyas', 
        Hostel = 'F Block',
        Uni = 'VIT University', 
        City = 'Chennai', 
        State = 'Tamil Nadu', 
        Country = 'India')
print("----------")
print("----------")
print("----------")
def address(**kwargs):
    for val, key in kwargs.items():
        print(f"{val}: {key}")
address(Room = 1244, 
        Name = 'Rachit Vyas', 
        Hostel = 'F Block',
        Uni = 'VIT University', 
        City = 'Chennai', 
        State = 'Tamil Nadu', 
        Country = 'India')