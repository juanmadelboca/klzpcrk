import time


def create_dictionary(word_length, output_name):
    start_start = time.clock()
    # creates a list of states used to make all posible words
    dictionary_state = [0 for x in xrange(word_length)]
    x = word_length-1
    alphabet = "abcdefghijklnmopqrstuvwxyz1234567890"
    file_handler = file(output_name, "w")

    while(x > -1):
        result = ""
        if dictionary_state[x] == len(alphabet)-1:
            print "entre if"
            for z in xrange(word_length):
                result += alphabet[dictionary_state[z]]
            dictionary_state[x] = 0
            x -= 1
        elif x == word_length-1:
            print "entre elseif"
            for z in xrange(word_length):
                result += alphabet[dictionary_state[z]]
            dictionary_state[x] += 1
        else:
            print "entre else"
            for z in xrange(word_length):
                result += alphabet[dictionary_state[z]]
            dictionary_state[x] += 1
            if x > 0:
                x += 1
            else:
                x = word_length-1

        file_handler.write(result+"\n")

    finish_time = time.clock()
    total_time = finish_time - start_start
    print ("Done! in " + str(total_time) + " seconds.")
