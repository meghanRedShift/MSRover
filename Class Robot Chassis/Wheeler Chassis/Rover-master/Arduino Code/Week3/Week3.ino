//Week 3:
//Create functions for forward, backward, left, right, and stop
//Use functions in the loop to drive the robot

//Week 4:
//Create inputs for functions to have variable drive times
//Begin designing maze

#include <Servo.h> //this includes the Servo library so that your code is easier to write

//Name your servos
Servo leftServo; 
Servo rightServo;

void setup() {
  // put your setup code here, to run once:

  //Attach your servos to the pin that you have them wired to
  leftServo.attach(10);
  rightServo.attach(3);
  
}

void loop() {
  // put your main code here, to run repeatedly:
 forward();
 left();
 forward();
}

//write functions for forward, backward, left, right, and stop
//Remember: motors are mounted in opposite directions!
void forward(){
  leftServo.write(120);
  rightServo.write(60);
}

void backward(){
  leftServo.write(60);
  rightServo.write(120);
}

void left(){
  leftServo.write(120);
  rightServo.write(120);
}

void right(){
  leftServo.write(60);
  rightServo.write(60);
}

//stop is a reserved word - use a different name like hold instead
void hold(){
  leftServo.write(90);
  rightServo.write(90);
}

