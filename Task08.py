def time_convertor(time):
    hour = time // 60
    minutes = (time % 60)

    if hour <= 1:
        print(f" {str(hour)} hour , {str(minutes)} minutes ")
    else:
        print(f" {str(hour)} hours , {str(minutes)} minutes ")    

time_convertor(67)  
time_convertor(280)
     
