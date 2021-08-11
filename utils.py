def add_new_command(command_to_add, speech, text):
    with open('commands.py', 'a') as file_object:
        file_object.write('        if \'{}\' in command:', command_to_add)
        file_object.write('            speak(\'{}\')', speech)
        file_object.write('            print(\'{}\')', text)
