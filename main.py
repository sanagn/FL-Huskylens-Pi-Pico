import machine
from huskylensPythonLibrary import HuskyLensLibrary
import utime
import time
import uos

husky = HuskyLensLibrary("I2C") ## SERIAL OR I2C
#φροντιζουμε η καμερα να είναι σε κατασταση  akoloyuhgse th grammh

# Ορίζουμε τους ακροδέκτες GPIO για τους κινητήρες του ρομπότ
M1A = machine.PWM(machine.Pin(10)) 
M1B = machine.PWM(machine.Pin(11)) 
M1A.freq(50) 
M1B.freq(50) 
M2A = machine.PWM(machine.Pin(20)) 
M2B = machine.PWM(machine.Pin(21)) 
M2A.freq(50) 
M2B.freq(50)

# Ορίζουμε τη λειτουργία των κινητήρων του ρομπότ
def move__forword(speed): # Ο κύκλος λειτουργίας πρέπει να είναι μεταξύ 0 και 65535
    #print("Fspeed"+str(speed))
    M1A.duty_u16(0) 
    M1B.duty_u16(speed)
    M2A.duty_u16(0)
    M2B.duty_u16(speed)  
def move__backword(speed): # Ο κύκλος λειτουργίας πρέπει να είναι μεταξύ 0 και 65535
    M1A.duty_u16(speed)
    M1B.duty_u16(0)
    M2A.duty_u16(speed)
    M2B.duty_u16(0)      
def move_left(speed): # Ο κύκλος λειτουργίας πρέπει να είναι μεταξύ 0 και 65535
    #print("Lspeed"+str(speed))
    M1A.duty_u16(0) 
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(speed)
def move_right(speed):# Ο κύκλος λειτουργίας πρέπει να είναι μεταξύ 0 και 65535
    #print("Rspeed"+str(speed))
    M1A.duty_u16(0) 
    M1B.duty_u16(speed)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
def stop_robot(speed):
    M1A.duty_u16(0) 
    M1B.duty_u16(speed)
    M2A.duty_u16(0)
    M2B.duty_u16(0)


# Main loop
utime.sleep_ms(1000)
while True:
    data = husky.command_request_arrows()
    #print(type(data))
    #print(data)
    #r = data[0] stack if data is empty!
    #print(f"[ Head:(x:{r[0]}, y:{r[1]}), Tail:(x:{r[2]}, y:{r[3]})")
    #print ("δεδομένα:")
    for i in data:
        XTail = int(i[0])
        YTail= i[1]
        XHead = int(i[2])
        YHead  = i[3]
        #print ("Χ-αρχής="+ str(XTail) +", Υ-αρχής="+ str(YTail)+",Χ-τελους="+str(XHead)+", Υ-τέλους="+str(YHead))
    Rten = XHead - 160 #160 είναι το μέσο Χ της κάμερας
    Rdir = XHead
    #print ("Rten="+str(Rten)+", Rdir="+ str(Rdir)) 
    #error = (int32_t)result.xTarget;
    # Analyze data and determine the position of the line
    # Example: Parse data to extract line position information

    # Control motors based on line position
    # Example: If line is more to the left, turn left. If more to the right, turn right.
    if Rdir > 180:
        move_right(abs(Rten)*400)
        utime.sleep_ms(abs(Rten))
    elif Rdir < 130:
        move_left(abs(Rten)*400)
        utime.sleep_ms(abs(Rten))
    elif (Rdir > 130) &(Rdir < 180):
        move__forword(40000)
    else:
        stop_robot(0)
    utime.sleep_ms(10)  # Adjust as needed for control frequency
    

# Ορίζουμε τις λειτουργίες των κινητήρων για να κινούν το ρομπότ μπροστά

# Ορίζουμε τις λειτουργίες των κινητήρων για να σταματήσουν το ρομπότ




