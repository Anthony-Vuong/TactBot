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
    void display_alert_status() const;
    const void rover_controls();
    const void turret_controls();

};

#endif // TACTBOT_H
