story = "Once upon a time there was a developer who started QwikSol with a minimum investment and now the company has 2000cr annual turnover."

# String Functions
print(len(story)) # --> Tells the length of the string
print(story.endswith("turnover.")) # --> It'll check that the string ends with the given words or not.
print(story.count("a")) # --> Tells how many times the given word is used in the string.
print(story.capitalize()) # --> It'll capatalize the first word of string
print(story.find("Once")) # --> finds the word is in the string or not and also tells the position of that. And if not find the given word, it returns -1
print(story.replace("developer", "Rahul")) # --> It'll replace the given word with the provided word all over the string.
