# dictionaries
#phone = input("phone")
#digital_mapping = {

 #   "1":"one",
  #  "2":"two",
  #  "3":"three",
  #  "4":"four"

#}
#output = ""
#for ch in phone:
#    output += digital_mapping.get(ch,"!" ) + ""
#    print(output)

# Emoji Converter
#message = input(">")
#words = message.split(" ")
#emojis ={
#    ":)":"😄",
 #   ":(":"😔"
#}
#output=""
#for word in words:
#    output += emojis.get(word,word) + ""
#print(output)

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😄",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ""
    return output
message = input(">")
print(emoji_converter(message))