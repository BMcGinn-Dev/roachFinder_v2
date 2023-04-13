print("hello world")

print("Beginning texty test")

try:
    with open("Include/texty.txt") as f:
        the_text = f.read()
        f.close()
except:
    print("Failed to read file")


try:
    print(the_text)
except:
    print(" 'the_text' does not exist ")