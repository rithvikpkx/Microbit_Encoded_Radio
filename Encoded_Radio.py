#13.2
#Import microbit module
from microbit import *

#13.2
#Import radio module
import radio

#13.2
#Enable radio hardware on the microbit
radio.on()

#13.2
#Configure radio channel to channel 16
radio.config(channel=16)

#13.6
#Define custom function called encode() with parameters text and shift
def encode(text, shift):
    
    #13.6
    #Set variable encoded to empty string
    encoded = ""
    
    #13.6
    #This for loop, loops the indented code “c” number of times
    #c is the number of characters in text
    for c in text: # ← New
        
        #13.6
        #Translate variable c into numbers and add shift
        #Assign this new value to variable val
        val = ord(c) + shift # ← New
        
        #13.6
        #Translate value of val into normal string and add encoded
        #Assigns this new value to encoded
        encoded = encoded + chr(val) # ← New
        
    #13.6
    #Return value of encoded to caller code
    return encoded
    
#13.6
#Create variable msg with string value Cats
msg = "Cats"

#13.6
#Call encode function with parameters msg for text and 3 for shift
#Set returned value equal to variable code_msg
code_msg = encode(msg, 3)

#13.7
#Send value of code_msg through radio
radio.send(code_msg)

#13.2
#Infinitely loop indented code block
while True:
    
    #13.2
    #Check radio for incoming messages
    #Store incoming messages in variable msg
    msg = radio.receive()
    
    #13.6
    #Conditional if statement to check if msg is blank or not
    #If msg is not blank, run indented code
    if msg:
        
        #13.7
        #Decode value of msg and set this value to clear_msg
        clear_msg = encode(msg, -3)
        
        #13.7
        #Scroll value of clear_msg across screen
        #Don't wait for code to stop and scoll infinitely
        display.scroll(clear_msg, wait=False, loop=True)
