// #include <SPI.h>
// #include <SD.h>


int analogPin = A0; // A0 analog to digital converter input pin, connected to the photodetector, powered 3.3v
float adc_val = 0.0;  // variable to store the value read
float voltage = 0.0; // voltage at photodetector
float ppm = 0.0; //derived ppm phosphate from voltage
int ss_mode = 0; //slide switch detected on or off, to trigger sensor cycle
int cycle_fin = 0; //extra value to prevent infinite looping of sensor cycle when activated

#if 0
File myFile;
#endif 

// (ss must be reset to off state before activating again)
void setup() {
  delay(500);
  Serial.println("test");


  Serial.begin(9600); //  setup serial
  pinMode(2, INPUT);

  #if 0
  Serial.println("\n\n\n\n\nThis is the start of a new iteration...");
  #endif

  #if 0
  Serial.println("Phosphate       |                Time");
  Serial.println("Measurements    |               Taken");
  Serial.println("----------------|--------------------");
  #endif 

  // Delete the file if it already exists
  // if (SD.exists("data.txt")) {
    // SD.remove("data.txt");  // ❌ Deletes the old file
    // Serial.println("Old data.txt removed.");
  // }


  // myFile = SD.open("data.txt", FILE_WRITE);

  // if (!myFile){
    // Serial.println("ERROR");
    // exit(1);
  // }

    // myFile.println("Logging started...");
    // myFile.println("Phosphate       |                Time");
    // myFile.println("Measurements    |               Taken");
    // myFile.println("----------------|--------------------");
    // myFile.close();


}



void loop() {
  // myFile = SD.open("data.txt", FILE_WRITE);

  // if (!myFile){
    // Serial.println("ERROR");
    // exit(1);
  }


  adc_val = float(analogRead(analogPin));  // read the input adc pin
  voltage = 5 * adc_val / 1023; //convert pin value to voltage (adc pin works from 0-5v)
  ppm = max(0, (voltage - 1.65447100313479622535) / -0.00899216300940438272); //ppm conversion
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

  #if 0 
  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.print(" PPM: ");
  Serial.print(ppm);
  Serial.print(" SlideSwitch mode: ");
  Serial.print(ss_mode);
  Serial.print(" Cycle finished?: ");
  Serial.println(cycle_fin);
  #endif


  #if 1
  // myFile.println(voltage);
  // myFile.println(ppm);


  #endif


  // myFile.close();

  delay(333);

  

}
