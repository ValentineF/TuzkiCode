int  ledPin = 11;
float sinVal;
int ledVal;
void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int x=0;x<180;x++){
  sinVal = (sin(x*(3.14/180)));
  ledVal = int (sinVal*255);
  analogWrite(ledPin,ledVal);
  delay(25);
  }
}
