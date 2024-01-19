def decode(message_file):  # define the function and its parameters
    message_dict = {}  # create a dictionary to store every line from the message file

    with open(message_file, 'r') as file:  # open the file in read mode

        for line in file:  # iterate through every line within the file
            number, word = line.split()  # split the line into a number and word variable
            number = int(number)  # convert number from string to integer
            message_dict[number] = word  # add the number and word to the dictionary in a (number : word) pair

    sorted_message_dictionary = dict(sorted(message_dict.items()))  # sort the dictionary by the keys (sort by number)

    pyramid_length = len(sorted_message_dictionary)  # The character length of the pyramid equals the dictionary length

    x = list(sorted_message_dictionary.keys())[0]  # The pyramid begins at the smallest number within the dictionary
    decoded_message = [sorted_message_dictionary[x]]  # Stores the word values associated with the decoded message

    for i in range(x, pyramid_length):  # Iterate over the length of the given data
        if x < len(sorted_message_dictionary):  # Continue decoding if the length of the dictionary is not surpassed
            for j in range(i):
                if x < pyramid_length:
                    x += 1  # only increment by one if the x value is less then the length of th dictionary
            if x < pyramid_length:  # append decoded word only using values that are less than the pyramid length
                decoded_message.append(sorted_message_dictionary[x+i])  # append the new-found decoded word to the list

    return " ".join(decoded_message)  # return the decoded message as a string separated by a singular space


print(decode("message_file.txt"))  # call the function and print its return value
