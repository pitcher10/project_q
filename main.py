def decode_message(message_file):
    message_file = open(message_file)
    message_dictionary = {}
    message_list = []
    pyramid_list = []
    for row in message_file:
        #extract number from row
        number = row.split(" ")[0]
        word = row.split(" ")[1].replace("\n", "")
        message_dictionary[number] = word
        message_list.append(int(number))
    #sort list ascending 
    message_list.sort()
    #add starting start and stop values
    increment = 1
    start = 0
    #iterate over the whole list
    while increment < len(message_list)+1:
        new_list = []
        #create new list which adds to the pyramid list
        for i in message_list[start:increment]:
            new_list.append(i)
        pyramid_list.append(new_list)
        #increase start values by length of list just added
        start += len(new_list)
        #increase increment by length of new list + 1 so that the list is 1 number longer
        increment += len(new_list)+1
    decoded_message = ""
    #iterate over the pyramid list and get the last value of each row
    for i in pyramid_list:
        last_value_of_pyramid_row = i[-1]
        #adds the word to the decoded message by using the last value of the row as the key to the dictionary
        message_word = message_dictionary[str(last_value_of_pyramid_row)]
        decoded_message += f'{message_word} '
    return decoded_message.strip()
