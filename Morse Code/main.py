# -*- coding: utf-8 -*-
import json

def main():
    text = input("Type a text: ")
    code = ""
    
    data = getData()
    
    for i in text:
        for j in data:
            if j["Letter"] == i:
                code += j["code"] + " "
                break
            
    print("Text:", text)
    print("Code:", code)
    
    swapped_code = swap_discord(code)
    
    print("Swapped code:", swapped_code)
    
def getData():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    
    return data
    
def swap_discord(code):
    new_code = code
    new_code = new_code.replace("-", "|| ||")
    new_code = new_code.replace("_", "||   ||")
    return new_code

main()