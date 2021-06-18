//Week 2:
//Basic setup
//Make the rover drive

#include <Servo.h> //this includes the Servo library so that your code is easier to write

//Name your servos
Servo leftServo; 
Servo rightServo;

void setup() {
  // put your setup code here, to run once:

  //Attach your servos to the pin that you have them wired to
  leftServo.attach(10);
  rightServo.attach(11);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //Set both servos to stopped (90)
  leftServo.write(90); 
  rightServo.write(90);

  //wait for one second
  delay(1000);

  //Set both servos to drive forward
  //they have opposite numbers because they are mounted in opposite directions
  leftServo.write(120);
  rightServo.write(20);

  //let the rover drive for a second
  delay(1000);

}
