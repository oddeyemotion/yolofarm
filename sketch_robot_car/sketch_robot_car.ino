#include <AFMotor.h>

AF_DCMotor motor1(1);   // M1 on Motor Shield
AF_DCMotor motor2(2);   // M2
AF_DCMotor motor3(3);   // M3
AF_DCMotor motor4(4);   // M4

char bluetoothInput='S';  // Input from Bluetooth HC-05

void setup()
{
  Serial.begin(9600); // Connect to Bluetooth HC-05
 
  motor1.setSpeed(255); // Initialise Motor Speed
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255);
  stopCar();          // Initialise Car Position
}


void loop() {

bluetoothInput=Serial.read(); // Read Bluetooth HC-05

switch (bluetoothInput) {
  case 'F':
  goForward();
  break; 
  case 'B':
  goBackward(); 
  break;
  case 'L':
  turnLeft(); 
  break;
  case 'R':
  turnRight();   
  break;
  case 'S':
  stopCar();
  break;
} // end switch

} // end loop()

void goForward()
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}
void goBackward()
{
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}
void turnLeft()
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}
void turnRight()
{
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}
void stopCar()
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}
