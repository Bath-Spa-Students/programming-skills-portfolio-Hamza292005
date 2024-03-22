#making a dictionary
glossary = {
    "variable" : "A location in memory used to store a value.",
    "string" : "A sequence of characters that represent a text.",
    "functions" : "modules of code that accomplsh specific tasks.",
    "list": "a varable that stores collection of data in specific order.",
    "operator" : "A character that represents a specific mathematical or logical process."
       
}
#printing
for key, value in glossary.items():
    print(f" {key}: {value}\n")