#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt', 'r') as name_file:
    """
    Get the names from the file invited_names.txt
    https://www.w3schools.com/python/ref_file_readlines.asp
    """
    input_names = name_file.readlines()

print(input_names)

with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter= letter_file.read()  # Get the template of the letter


    for name in input_names:
        """
        Name contains a \n at the end which needs to be removed
        https://www.w3schools.com/python/ref_string_strip.asp
        https://www.w3schools.com/python/ref_string_replace.asp
        """
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER,stripped_name)
        
        """
        New letter created from the template and written to new file path
        """
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt','w') as completed_letter:
            completed_letter.write(new_letter)