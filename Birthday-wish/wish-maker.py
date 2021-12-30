import Bday_wapp_char as wish
def main():
    name=input("Enter the name: ")
    name=name.replace(" ","")
    name= name.upper()
    l=len(name)
    if l<14:
        name+='#'*(25-l)
    ch=int(input("1. new year\n2. B'day\nenter choice: "))

    if ch==1:
        k=int(input("enter w: "))
        nyr(name,k)
        
    else:
        bday(name,l)



def bday(name,l):
    if l<10:
        wish.happy(name)
        wish.wishort(name)
    if l>=10:
        wish.happy(name)
        wish.wilong(name)

def nyr(name,k):
    wish.happy(name)
    if k==1:
        wish.ny1(name)
    else:
        wish.ny2(name)
    wish.y22(name)

if __name__=='__main__':
    main()


'''
    Currently it can generate blocks of "HAPPY BIRTHDAY !'" 
    in monospace font for whatsapp
    and it is custom made to fit many whatsapp screen which can accomadate
    ```ABCDEFGHIJKLMNOPQRSTUV``` 22 characters in a single line
    Don't forget the ```monospace code of whatapp```: ```msg here``` 
    which is generated along with it...

    I will update it with other blocks, when I get time, feel free to use and wish your friends& family
    Run this program with Bday_wapp_char.
    #####################
    ABCDEFGHIJKLMNOPQRSTUV
'''
