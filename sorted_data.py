#read the file
#loop through each line and enter it into dictionary
#call .items() on dictionary to make pairs - returns a list of pairs
#sort list by key name
#print string of restaurant and rating

from sys import argv

script, filename = argv

text = open(filename)

filetext = text.read()
text.close()

def dictionary_compile(any_text):
    list_of_lines = any_text.split("\n")
    double_split_list = []
    for item in list_of_lines:
        double_split_list.append(item.split(":"))

    d = {}
    for item in double_split_list:
        d[item[0]] = item[1]
    return d
    
rest_dict = dictionary_compile(filetext)

def sort_dictionary(any_dict):
    a = any_dict.items() # return a list of tuples
    a.sort()
    for item in a:
        print "Restaurant %s is rated at %s." % (item[0], item[1])


sort_dictionary(rest_dict)







