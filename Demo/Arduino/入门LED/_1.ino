#include <Servo.h>
Servo myServo;
const int piezo = A0;
const int switchPin = 2;
const int speakerPin = 9;
const int greenLed = 4;
const int redLed = 5;

int knockVal;
int switchVal;
int pinKnock = 3;//设定的敲击数
int count = 0;
const int quietKnock = 10;
const int loudKnock = 100;
boolean locked = false;
int numberOfKnocks = 0;

void setup() {
  myServo.attach(9);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(switchPin, INPUT);
  Serial.begin(9600);
  digitalWrite(greenLed, HIGH);
  myServo.write(0);
}

void loop() {
  if (locked == false) {
    switchVal = digitalRead(switchPin);
    if(switchVal == HIGH)
    {
      switchVal = 0;
      switchVal = digitalRead(switchPin);
      delay 3000;//3秒检测
      if (switchVal == HIGH) {
      locked = true;
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
      myServo.write(90);
      delay(1000);
      }
      else
        {
            int sensorReading = analogRead(A0);
            int thisPitch = map(sensorReading, 400, 1000, 120, 1500);
            tone(9, thisPitch, 10);
            delay(1); 
        }
    }
   
  }

  if (locked == true) {
    knockVal = analogRead(piezo);
    if (numberOfKnocks < pinKnock && knockVal > 0) {
      if (checkForKnock(knockVal) == true) {
        numberOfKnocks++;
      }
    }

    if (numberOfKnocks >= pinKnock) {
      locked = false;
      myServo.write(0);
      delay(20);
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
      numberOfKnocks = 0;
    }
  }
}

boolean checkForKnock(int value) {
  if (value > quietKnock && value < loudKnock) {
    digitalWrite(yellowLed, HIGH);
    delay(50);
    digitalWrite(yellowLed, LOW);
    return true;
  }
  else {
    return false;
  }
}

