#define SPEED_STEP  (255 / (3 - 1))

void setup() {
  // put your setup code here, to run once:
	pinMode(9,OUTPUT);
	for (int i = 5; i <= 7 ; i++)
	{
		pinMode(i,INPUT_PULLUP);
	}
}

void loop() {
  // put your main code here, to run repeatedly:
	for (int i = 0; i < 3; i++)
	{
		if (digitalRead(i+5))
			continue;
		int speed = i * SPEED_STEP;
	}
	analogWrite(9,speed);
}