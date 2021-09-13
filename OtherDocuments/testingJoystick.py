#java
if(percentY < 0)  {
    
    tempPercent = Math.abs(percentY)
    if(tempPercent > 0 && tempPercent < 20){
        write message = 11
    }
    elif(tempPercent > 20 && tempPercent < 40){
        write message = 12
    }
    elif(tempPercent > 40 && tempPercent < 60){
        write message = 13
    }
    elif(tempPercent > 60 && tempPercent < 80){
        write message = 14
    }
    else{
        write message = 15
    }
}
else{
    if(percentY > 0 && percentY < 20){
        write message = 31
    }
    elif(percentY > 20 && percentY < 40){
        write message = 32
    }
    elif(percentY > 40 && percentY < 60){
        write message = 33
    }
    elif(percentY > 60 && percentY < 80){
        write message = 34
    }
    else{
        write message = 35
    }
}

#python
def decipherMessage(self, msg):
    
    direction = msg[0]
    speed = msg[1]
    
    
    
    
    if direction == 1:
        forward(1, speed)
    else:
        backward(-1, speed)
    
    
    
        
        



