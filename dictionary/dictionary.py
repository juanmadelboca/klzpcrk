import time


def create_dictionary(word_length, output_name, dictionary_type):
    start_start = time.clock()
    # creates a list of states used to make all posible words
    dictionary_state = [0 for x in xrange(word_length)]
    x = word_length-1
    alphabet = __choose_dictionary__(dictionary_type)
    file_handler = file(output_name, "w")

    while(x > -1):
        result = ""
        # save actual state in file
        for z in xrange(word_length):
            result += alphabet[dictionary_state[z]]
        file_handler.write(result+"\n")

        # get the new dictionary state
        if dictionary_state[x] == len(alphabet)-1:
            dictionary_state[x] = 0
            x -= 1
        elif x == word_length-1:
            dictionary_state[x] += 1
        else:
            print "else:", result
            dictionary_state[x] += 1
            if x > 0:
                x += 1
            else:
                x = word_length-1

    finish_time = time.clock()
    total_time = finish_time - start_start
    print ("Done! in " + str(total_time) + " seconds.")


def __choose_dictionary__(dictionary_type):

    if(dictionary_type == "full"):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890"
    elif(dictionary_type == "normal"):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890"
    elif(dictionary_type == "numbers"):
        alphabet = "1234567890"
    else:
        alphabet = dictionary_type
    return alphabet
