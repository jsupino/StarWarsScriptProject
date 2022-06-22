#Download script from Kaggle, refer to readme for link. Save to your computer.

#Input the file name
input_file = input("Enter Star Wars Episode V File Name: ")

#Input character name to retreieve their lines
sw_dic = []
char_name = input("Which character's lines would you like to read? ")

with open(input_file, 'r') as text:
    text = text.readlines()[1:]  #skip first line in file
    for line in text:
        line = line.lower().split('"') #lowercase all words and split by quotes
        dialogue = line.pop(5)
        name = line.pop(3)
        line_number = line.pop(1)
        new_obj = {
            "line": line_number,
            "name": name,
            "dialogue": dialogue
        }
        if name == char_name.lower():
            sw_dic.append(new_obj)
        elif char_name == "all":
            sw_dic.append(new_obj)
    print(sw_dic)





