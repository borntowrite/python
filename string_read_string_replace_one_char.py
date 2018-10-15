
############################################################
# Replace One Char in given position 
############################################################

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position]=character
    string=''.join(string_list) # convert to string from list array
    return string

if __name__ == '__main__':
    s_new = mutate_string("melong", 3, "c")
    print(s_new)
   

