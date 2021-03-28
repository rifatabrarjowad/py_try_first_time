massage = input(">")
words = massage.split(' ')  # split is make a list
emojiis = {
    ":)": "🙂",
    ":(": "😔"
}
output = " "
for word in words:
    output += emojiis.get(word, word) + " "
print(output)
