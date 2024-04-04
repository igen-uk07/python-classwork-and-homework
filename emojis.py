#message = input("enter")
def emoji_converter(message):
    words = message.split('')
    emojis = {
        ":)" : "😁",
        "(:" : "🤷‍♂️"
    }
    output = ''
    for words in words:
        output+=emojis.get(word,word)
message = input("Enter the message")
emoji_converter(message)
print(output)

