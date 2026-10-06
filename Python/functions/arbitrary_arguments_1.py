def address_line(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    for val in kwargs.values():
        print(val)
address_line("Dr.", "Drake", "Ramoray", end = " ", 
            Room = 1244, 
            Hostel = 'F Block',
            Uni = 'VIT University', 
            City = 'Chennai', 
            State = 'Tamil Nadu', 
            Country = 'India')