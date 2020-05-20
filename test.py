
#mylist = [(1,3), (2,4), (5,7), (6,8), (9,10)]
#for (a,b) in mylist:
 #  print(a)
#   print(b) 


d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d.items():
    print (item)

x = 0
while x < 5:
    print(f'the current value of x is {x}')
    x += 1

word = 'pranav'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mydata= [1, 2, 3]
myname= ['Pranav', 'Dhanashri']

for item in (zip(mydata,myname)):
    print(item)

mystring = 'Dhanashri'
mylist1 = [letter for letter in mystring]
print (mylist1)

mynumber = [num**2 for num in range(0,5)]
print(mynumber)

mylist2= [x**2 for x in range(0,10) if x%2==0]
print(mylist2)


def myfunc(mystring):
    result = ""
    for letter, value in enumerate(mystring):
        if letter % 2==0:
          result = result + value.upper()    
        else:
           result = result + value.lower()   
    return result     

st = 'this is a test'
for letter in st.split():
    if letter[0] == 't':
        print(letter)


for num in range(1,101):
    if num%3==0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)  


st = 'hello world bye world'
for letter in st.split():
    print(letter[0])




def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b   
    elif a % 2 != 0 or b % 2 != 0:   
        if a > b:
            return a
        else:
            return b      
print(lesser_of_two_evens(2,5))         



def split_fun(string):
  my_strng = string.split()
  if my_strng[0][0] == my_strng[1][0]:
    return True
  else:
    return False
print(split_fun("Hello orld"))

def two_integers(a,b):
    if(a + b) == 20:
        print("Correct")
    elif a == 20 or b == 20:
        return True
    else:
        return False    
print(two_integers(20,10))           


def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
print(makes_twenty(10,20))




"""def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
print(old_macdonald('macdonald'))"""  


def old_macdonald(name):
    first_letter = name[0]
    middle_letters = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + middle_letters + fourth_letter.upper() + rest 
print(old_macdonald('macdonald')

)    
def master_yoda(text):
    word_list = text.split()
    reverse_word_list = word_list[::-1]
    return ' '.join(reverse_word_list)
print(master_yoda('Hello World'))    
   
def almost_there(n):
    if abs(100 - n) <= 10 or abs(200 - n)<= 10:
        return True
    else:
        return False
print(almost_there(100))            


def has_33(num):
    for digit in num:
        if num[digit]== 3 and num[digit + 1]== 3:
            return True
        else:
            return False
print(has_33([1,1,3,5]))                


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
print(paper_doll("Mississipi"))        


def black_jack(a,b,c):
    if sum([a,b,c]) == 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return "BUST"
print(black_jack(5,6,11))              


def spy_games(nums):

    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1
print(spy_games([1,2,0,0,0,7,5]))    