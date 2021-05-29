#include <stdio.h>
#include <wiringPi.h>
#define LED1 21
#define LED2 16

void main()
{
   printf("라즈베리파이 C로 구동해보기\n");
   wiringPiSetupGpio();
   pinMode(LED1, OUTPUT);
   pinMode(LED2, OUTPUT);

   while(1)
   {
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, LOW);
      delay(500);
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, HIGH);
      delay(500);
   }
}
