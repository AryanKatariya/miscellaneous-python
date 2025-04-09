# def shout(word = "yes"):
#     return word.upper()+"!"

# scream = shout

# print(scream())


# def talk():
#     def whisper(word="yes"):
#         return word.lower()+"..."
    
#     return whisper

# print(talk()())

def getTalk(kind = "shout"):
    
    def shout(word="yes"):
        return word.upper()+"!"
    
    def whisper(word="yes"):
        return word.lower()+"..."
    
    if kind == "shout":
        return shout
    else:
        return whisper
    
talky = getTalk()

print(talky)
print(talky())
print(getTalk(kind = "whisper")())
    
    