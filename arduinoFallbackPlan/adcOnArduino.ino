int analogPin = A0; // A0 analog to digital converter input pin, connected to the photodetector, powered 3.3v
float adc_val = 0.0;  // variable to store the value read
float voltage = 0.0; // voltage at photodetector
float ppm = 0.0; //derived ppm phosphate from voltage
int ss_mode = 0; //slide switch detected on or off, to trigger sensor cycle
int cycle_fin = 0; //extra value to prevent infinite looping of sensor cycle when activated

int isFirstRun = 1;

// (ss must be reset to off state before activating again)
void setup() {
  Serial.begin(9600); //  setup serial
  pinMode(2, INPUT);

  // Serial.println("\n\n\n\nThiskjdsjkds is the start of a new iteration...");
  delay(5000); // Give you time to open the Serial Monitor

  isFirstRun = 1;
}



void loop() {
  // Serial.println(isFirstRun);

  if (isFirstRun == 1){
    // Serial.println("This is the first run...\n\n");
    isFirstRun = 0;

    #if 0
    exit(1);
    #endif

    Serial.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    Serial.println("Phosphate       |             Voltage");
    Serial.println("Measurements    |               Level");
    Serial.println("----------------|--------------------");


  }

  #if 0
  Serial.println("\n\n\n\nThisdskj is the start of a new iteration...");
  #endif

  adc_val = float(analogRead(analogPin));  // read the input adc pin
  voltage = 5 * adc_val / 1023; //convert pin value to voltage (adc pin works from 0-5v)
  ppm = float( max(0, (voltage - 1.65447100313479622535) / -0.00899216300940438272) ); //ppm conversion

  ss_mode = digitalRead(2);
  if(ss_mode == 1 && cycle_fin == 0){
    #if 0
    //run a sensing cycle, meaning get the motors, valves, and pumps to operate
    Serial.println("operating operation");
    Serial.println("operation finished");
    cycle_fin = 1;
    #endif

  }


  else if(ss_mode == 0 && cycle_fin == 1){
    cycle_fin = 0;
  }

  #if 1
  Serial.print("PPM: ");
  Serial.print(ppm);

  // Serial.print(",");

  if (ppm < 10) Serial.print(" ");

  Serial.print("                    V: ");



  Serial.println(voltage);
  #endif



  #if 0
  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.print(" SlideSwitch mode: ");
  Serial.print(ss_mode);
  Serial.print(" Cycle finished?: ");
  Serial.println(cycle_fin);
  #endif


  delay(333);
}