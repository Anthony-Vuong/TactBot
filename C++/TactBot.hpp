#ifndef TACTBOT_H
#define TACTBOT_H

#include "Turret.hpp"
#include "Rover.hpp"


class TactBot
{
    
private:

    char* alert_status;
    
    
public:
    TactBot(Rover r, Turret t);
    ~TactBot();

};

#endif // TACTBOT_H
