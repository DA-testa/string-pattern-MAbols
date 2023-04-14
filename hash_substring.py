# python3
b=33
q=284
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    command_input=input()
    if "I" in command_input:
        pattern=input()
        text=input()
    elif "F" in command_input:
        testa_fails=open("./tests/06")
        pattern=testa_fails.readline()
        text=testa_fails.readline()
    # print(P)
    # print(T)
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())
def get_hash(pattern:str)-> int:
    global b,q
    m=len(pattern)
    result=0
    for i in range(m):
        result=(b*result+ord(pattern[i]))%q
    return result
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global b,q
    pattern_len=len(pattern)
    pattern_hash=get_hash(pattern)
    
    text_len=len(text)
    pos_count=0
    result=[]
    for i in range(text_len):
        text_atdal=text[i:pattern_len+i]
        if len(text_atdal)<pattern_len:
            break
        else:
            #print(text_atdal)
            text_hash=get_hash(text_atdal)
            if text_hash==pattern_hash:
                if text_atdal==pattern:
                    result.append(pos_count)
                    pos_count=pos_count+1
                else:
                    pos_count=pos_count+1
            else:
                pos_count=pos_count+1

    # print(pattern_hash)
    # print(tex_hash) 
    # print(text[:pattern_len])
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

