import time


def create_dictionary(word_length, output_name):
    start_start = time.clock()

    lista = [0 for x in xrange(word_length)]
    x = word_length-1
    string = "abcdefghijklnmopqrstuvwxyz0123456789"
    file1 = file(output_name, "w")
    while(x > -1):
        result = ""
        if lista[x] == len(string)-1:
            for z in xrange(word_length):
                result += string[lista[z]]
            lista[x] = 0
            x -= 1
        elif x == word_length-1:
            for z in xrange(word_length):
                result += string[lista[z]]
            lista[x] += 1
        else:
            for z in xrange(word_length):
                result += string[lista[z]]
            lista[x] += 1
            if x > 0:
                x += 1
            else:
                x = word_length-1
        file1.write(result+"\n")

    finish_time = time.clock()
    total_time = finish_time - start_start
    print ("Done! in " + str(total_time) + " seconds.")
