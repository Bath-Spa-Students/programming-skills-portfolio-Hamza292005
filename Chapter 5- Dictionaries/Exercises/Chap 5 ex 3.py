#making a list
glossary = {
    "variable" : "A location in memory used to store a value.",
    "string" : "A sequence of characters that represent a text.",
    "functions" : "modules of code that accomplsh specific tasks.",
    "list": "a varable that stores collection of data in specific order.",
    "operator" : "A character that represents a specific mathematical or logical process."
       
}
#adding more values and keys

glossary["loop"] = "A sequence of instructions hat is continually repeated until a certain condition is fulfilled."
glossary["dictionary"] = "data structure that stores items in key-value pairs."
glossary["constant"] = "A value that is not altered by the program."
glossary["error"] = "issues or defects that arise within the program."
glossary["command"] = "An action that is asked to a computer to perform."

#printing
for key, value in glossary.items():
    print(f" {key}: {value}\n")
