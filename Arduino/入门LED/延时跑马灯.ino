byte ledPin[]={4,5,6,7,8,9,10,11,12,13};
int ledDelay(65);
int direction = 1;
int currentLED = 0;
unsigned long changeTime;
int potPin = 2;
void setup() {
  // put your setup code here, to run once:
  for(int x=0;x<10;x++){
    pinMode(ledPin[x],OUTPUT);
  }
  changeTime = millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  ledDelay = analogRead(potPin);
  if((millis() - changeTime > ledDelay)){
    changeLED();
    changeTime = millis();
  }
}

void changeLED(){
  for(int x=0;x<10;x++){
    digitalWrite(ledPin[x],LOW);
  }
  digitalWrite(ledPin[currentLED],HIGH);
  currentLED += direction;
  if(currentLED == 9){direction = -1;}
  if(currentLED == 0){direction = 1;}
}

