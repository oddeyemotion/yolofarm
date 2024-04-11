#include <Wire.h>

const int line_sensor = 11;
int line_val = 0;
int car_on = 0;

const int in1A = 7;
const int in2A = 8;
const int in3A = 9;
const int in4A = 10;

const int in1B = 3;
const int in2B = 4;
const int in3B = 5;
const int in4B = 6;

void setup() {
  Wire.begin(0x8);
  Serial.begin(9600);

  pinMode(line_sensor, INPUT);

  pinMode(in1A, OUTPUT);
  pinMode(in2A, OUTPUT);
  pinMode(in3A, OUTPUT);
  pinMode(in4A, OUTPUT);

  pinMode(in1B, OUTPUT);
  pinMode(in2B, OUTPUT);
  pinMode(in3B, OUTPUT);
  pinMode(in4B, OUTPUT);
}

void receiveEvent (int howMany){
  while (Wire.available()){
    car_on = Wire.read();
  }
}

void sendEvent(){
  //Wire.write(line_val);
  Wire.write(car_on);
}

void Forward(){
  digitalWrite(in1A, HIGH);
  digitalWrite(in2A, LOW);
  digitalWrite(in3A, HIGH);
  digitalWrite(in4A, LOW);

  digitalWrite(in1B, HIGH);
  digitalWrite(in2B, LOW);
  digitalWrite(in3B, HIGH);
  digitalWrite(in4B, LOW);
}

void Backward(){
  digitalWrite(in1A, LOW);
  digitalWrite(in2A, HIGH);
  digitalWrite(in3A, LOW);
  digitalWrite(in4A, HIGH);

  digitalWrite(in1B, LOW);
  digitalWrite(in2B, HIGH);
  digitalWrite(in3B, LOW);
  digitalWrite(in4B, HIGH);
}

void loop() {
  Wire.onReceive(receiveEvent);
  line_val = digitalRead(line_sensor);
  if (car_on == 1){
    Forward();
  }
  else {
    digitalWrite(in1A, LOW);
    digitalWrite(in2A, LOW);
    digitalWrite(in3A, LOW);
    digitalWrite(in4A, LOW);

    digitalWrite(in1B, LOW);
    digitalWrite(in2B, LOW);
    digitalWrite(in3B, LOW);
    digitalWrite(in4B, LOW);
  }

  Wire.onRequest(sendEvent);

  Serial.print(line_val);
  Serial.print("\t");
  Serial.print(car_on);
  Serial.print("\n");
  delay (500);
}