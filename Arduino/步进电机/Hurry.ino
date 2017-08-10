# include <Stepper.h>
# define STEPS 8966//转2.189圈需要的步数
int sensor = A0;
int val = 0;
double cir = 1.81, pace = 0;  //周长
Stepper stepper (STEPS, 8, 9, 10, 11);
void setup ()
{
  pinMode(sensor, INPUT);
  stepper.setSpeed(4);
  Serial.begin(9600);
}

void loop ()
{
  pace = velocity();
  delay(50);
  Serial.println(val);
  switch (val)
  {
    case 0: if (pace > 0.56)
        plus();
      break;

    case 1: if (pace > 1.12)
        plus();
      else if (pace < 0.56)
        sub();
      break;

    case 2: if (pace > 1.68)
        plus();
      else if (pace < 1.12)
        sub();
      break;

    case 3: if (pace > 2.24)
        plus();
      else if (pace < 1.68)
        sub();
      break;

    case 4: if (pace > 2.80)
        plus();
      else if (pace < 2.24)
        sub();
      break;

    case 5: if (pace > 3.36)
        plus();
      else if (pace < 2.80)
        sub();
      break;

    case 6: if (pace > 3.92)
        plus();
      else if (pace < 3.36)
        sub();
      break;

    case 7: if (pace < 3.92)
        sub();
      break;
    default: sub();
    break;
  }


}


double velocity()
{
  long count = 0, beginTime = 0, endTime = 0;
  long start = millis();
  while (1)
  {
    if (analogRead(sensor) < 100 && count == 0)
    {
      beginTime =  millis();//单位毫秒
      count = 1;
    }
    else if (analogRead(sensor) < 100 && count == 1)
    {
      endTime = millis();
      return (cir / (endTime - beginTime)) * 1000;
    }
    if(millis() - start > 2000) return 0;
  }
}

void plus()
{
  stepper.step(STEPS);
  val++;
}

void sub()
{
  stepper.step(-STEPS);
  val--;
}
