import os

LEVEL_COUNT_PLACEHOLDER = "LEVEL_COUNT_PLACEHOLDER"
OUTPUT_PINS_COUNT_PLACEHOLDER = "OUTPUT_PINS_COUNT_PLACEHOLDER"
LEVEL_DURATIONS_PLACEHOLDER = "LEVEL_DURATIONS_PLACEHOLDER"
INITIAL_LEVEL_PLACEHOLDER = "INITIAL_LEVEL_PLACEHOLDER"
OUTPUT_PINS_PLACEHOLDER = "OUTPUT_PINS_PLACEHOLDER"

def generate_code(output_filepath , output_filename , template_file_fullpath , initial_level , levels_durations_list:list , output_pins_list:list): 
    assert len(levels_durations_list) != 0 , "levels_durations_list should not be empty"
    assert len(output_pins_list) != 0 , "output_pins_list should not be empty"

    with open(template_file_fullpath , 'r') as file: 
        template_text = file.read()

    output_pins_text = ""
    for idx , output_pin in enumerate(output_pins_list):
        output_pins_text += "{}".format(output_pin)
        if(idx != len(output_pins_list) - 1): 
            output_pins_text += ","

    level_durations_text = ""
    for idx , level_duration in enumerate(levels_durations_list): 
        level_durations_text += "{}".format(level_duration)
        if(idx != len(levels_durations_list) - 1): 
            level_durations_text += ","        

    
    template_text = template_text.replace(LEVEL_COUNT_PLACEHOLDER , "{}".format(len(levels_durations_list)))
    template_text = template_text.replace(OUTPUT_PINS_COUNT_PLACEHOLDER , "{}".format(len(output_pins_list)))
    template_text = template_text.replace(LEVEL_DURATIONS_PLACEHOLDER , level_durations_text)
    template_text = template_text.replace(INITIAL_LEVEL_PLACEHOLDER , "{}".format(initial_level))
    template_text = template_text.replace(OUTPUT_PINS_PLACEHOLDER , output_pins_text)

    output_folder = os.path.join(output_filepath , output_filename)
    if(not os.path.isdir(output_folder)):
        os.mkdir(output_folder)
    output_file = os.path.join(output_folder , "{}.ino".format(output_filename))

    with open(output_file , 'w') as outfile: 
        outfile.write(template_text)


generate_code("." , "genfile" , "./ino_template" , 0 ,  [10,20,30,40,50] , [40])

    