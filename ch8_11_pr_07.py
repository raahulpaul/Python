# this = "    Rahul is best      "
# print(this)
# print(this.strip()) # Strip function removes extra spaces


def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Rahul is best      "
n = remove_and_strip(this, "Rahul")
print(n)