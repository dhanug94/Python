"""def myfunc(**kwargs):
    if 'movie' in kwargs:
        print("My favorite movie is {}".format(kwargs['movie']))
    else:
        print("Not interested")
myfunc(movie = 'abcd', fvrt = 'agneepath')"""        



def myfunction(mystring):
    result = ""
    for letter, value in enumerate(mystring):
        if letter % 2==0:
          result = result + value.upper()    
        else:
           result = result + value.lower()   
    return result
print(myfunction('Pranav'))  



mystring = 'Pranav'
result = mystring + 'd'
print(result)