import emoji

user_i = input("imput a sentence: ")

res = user_i.split()
new_text = ""
final = ""

for text in res:
    new_text += emoji.emojize(":"+text+":")

for char in new_text:
    if char == ":":
        continue
    else:
        final += char

print(final)