#include <Servo.h>
#define LEDpin 3

Servo myservo;
byte i=0,fade=1;

void setup() {
 Serial.begin(9600);
 myservo.attach(9);
 myservo.write(0);
}

void loop() {
  myservo.write(i);
  readSerial();
  i = i + fade;
  fade=(i<=0||i>=180)?-fade:fade;
  delay(30);
}

void readSerial(){
    if(Serial.available()>0){
    char reading = Serial.read();
    switch(reading){
      case '0': analogWrite(LEDpin,0);break;
      case '1': analogWrite(LEDpin,1);break;
      case '2': analogWrite(LEDpin,3);break;
      case '3': analogWrite(LEDpin,10);break;
      case '4': analogWrite(LEDpin,255);break;
    }
  }
}
