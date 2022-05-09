
#define LEVELS_COUNT 5
#define OUTPUT_PINS_COUNT 1
int levels_durations_ms [] = {10,20,30,40,50};
int iteration_idx = 0; 
int initial_level = 0;
int neg_initial_level = 0;

int output_pins[] = {40}; 
int test_var = 0; 

void setup() {
  for(int i = 0 ; i < OUTPUT_PINS_COUNT ; i++)
  {
    pinMode(output_pins[i] , OUTPUT); 
    digitalWrite(output_pins[i] , initial_level); 
  }
  neg_initial_level = (initial_level + 1) % 2; 

  Serial.begin(115200);
}

void loop() {
  // reset iteration index if it overflows
  if(iteration_idx >= LEVELS_COUNT)
    iteration_idx = 0; 

  // write the proper value of the level to the output
  int level_value = (iteration_idx % 2) * neg_initial_level + ((iteration_idx + 1) % 2) * initial_level;
  Serial.print(level_value); 

  for(int output_pin_idx = 0 ; output_pin_idx < OUTPUT_PINS_COUNT ; output_pin_idx++)
  {
    if(level_value == 0)
        digitalWrite(output_pins[output_pin_idx] , LOW);
    else
        digitalWrite(output_pins[output_pin_idx] , HIGH);  
  }
  // wait until the time of the level is passed
  delay(levels_durations_ms[iteration_idx]); 

  // increase the level index
  iteration_idx++;
}