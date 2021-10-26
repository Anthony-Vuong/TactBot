#include "Motor.hpp"
#include <pigpio.h>


//Overloaded Constructor
Motor::Motor(int en_pin_val, int in1_pin_val, int in2_pin_val, int sig1_enc, int sig2_enc)
    :enable_pin{en_pin_val}, pin1_input{in1_pin_val}, pin2_input{in2_pin_val}, signalA_encoder{sig1_enc}, signalB_encoder{sig2_enc}{
        
        //Setting up DC motor pins, NOTE: Check for invalid flags
        gpioSetMode(enable_pin, PI_OUTPUT);
        gpioSetMode(pin1_input, PI_OUTPUT);
        gpioSetMode(pin2_input, PI_OUTPUT);
        gpioSetMode(signalA_encoder, PI_INPUT);
        gpioSetMode(signalB_encoder, PI_INPUT);

}

//Destructor
Motor::~Motor(){}

void Motor::enable_motor(){
    gpioWrite(enable_pin, 1);
}

void Motor::disable_motor(){
    gpioWrite(enable_pin, 0);
}

void Motor::clockwise_turn(short int duty){
    if(!inMotion){
        gpioWrite(enable_pin, 1);
        gpioWrite(pin1_input, 0);
        gpioWrite(pin2_input, 1);
        inMotion = true;
    }
    
    gpioPWM(enable_pin, duty);
    
}

void Motor::counter_clockwise_turn(short int duty){
    if(!inMotion){
        gpioWrite(enable_pin, 1);
        gpioWrite(pin1_input, 1);
        gpioWrite(pin2_input, 0);
        inMotion = true;
    }
    
    gpioPWM(enable_pin, duty);
    
    
}

void Motor::hold(){
    gpioWrite(enable_pin, 0);
    gpioWrite(pin1_input, 0);
    gpioWrite(pin2_input, 0);
    inMotion = false;

}

void Motor::spin(short int direction, short int duty){
    if(direction == 1){
        clockwise_turn(duty);
    }else if(direction == -1){
        counter_clockwise_turn(duty);
    }else{
        hold();
    }
    
}

