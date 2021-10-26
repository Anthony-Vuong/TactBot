#ifndef MOTOR_H
#define MOTOR_H



class Motor
{
    
private:
    int enable_pin;
    int pin1_input;
    int pin2_input;
    int signalA_encoder;
    int signalB_encoder;
    bool inMotion{false};
    
    
public:
    Motor(int enable, int in1, int in2, int sig1_enc, int sig2_enc);
    ~Motor();
    void clockwise_turn(short int duty);
    void counter_clockwise_turn(short int duty);
    void hold();
    void spin(short int direction, short int duty);
    void enable_motor();
    void disable_motor();

    

};

#endif // MOTOR_H
