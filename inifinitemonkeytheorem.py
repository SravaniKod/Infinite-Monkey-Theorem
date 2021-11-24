import random

def generate(letters, shakespeare_string):
    gen_string = ""
    while len(gen_string) <= len(shakespeare_string):
        gen_string += random.choice(letters)
    return gen_string

def compare(generated_string, shakespeare_string):
    global count
    if generated_string == shakespeare_string:
        print("success!! the generated string matched with \
              shakespeare sentence")
        print("the string generated is %s at %d \
              iteration"%(generated_string, count ))
    else: 
        count=count+1
        if count%1000==0:
            with open("infinitemonkeytheorem.txt","a") as f:
                f.write(generated_string)
                f.write("\n")

def iterate(letters, shakespeare_string):
    while True:
        generated_string = generate(letters,shakespeare_string)
        result = compare(generated_string, shakespeare_string)
        if result == True:
            break
            
shakespeare_string = "methinks it is like a weasel"
letters=[]
count = 0
for letter in shakespeare_string:
    if letter not in letters:
        letters.append(letter)
iterate(letters, shakespeare_string)
        