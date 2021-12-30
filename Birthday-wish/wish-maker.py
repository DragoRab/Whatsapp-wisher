import Bday_wapp_char as wish
name=input("Enter the name: ")
name=name.replace(" ","")
name= name.upper()
l=len(name)
if l<14:
        name+='#'*(25-l)
if l<10:
    wish.happy(name)
    wish.wishort(name)
if l>=10:
    wish.happy(name)
    wish.wilong(name)
    '''
    Currently it can generate blocks of "HAPPY BIRTHDAY !'" 
    in monospace font for whatsapp
    and it is custom made to fit many whatsapp screen which can accomadate
    ```ABCDEFGHIJKLMNOPQRSTUV``` 22 characters in a single line
    Don't forget the ```monospace code of whatapp```: ```msg here``` 
    which is generated along with it...

    I will update it with other blocks, when I get time, feel free to use and wish your friends& family
    Run this program with Bday_wapp_char.

````
|#####|        |#####|
 |###|          |###| 
 |###|          |###| 
 |###|  ______  |###| 
 |###|  /####\  |###| 
 |###| /######\ |###| 
 |###|/###/\###\|###| 
 |#######/  \###\###| 
 |######/    \######| 
 |#####/      \#####|

```
    '''
