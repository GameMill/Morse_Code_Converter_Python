import os

def safe_int_input_min_max(text,min,max):
    try:
        data =  int(input(text).strip())
        if data >= min and data <= max:
            return data
        else:
            return safe_int_input_min_max(text,min,max)
    except:
        return safe_int_input_min_max(text,min,max)

morse_code = {
    "a":"▄ ▄▄▄",
    "b":"▄▄▄ ▄ ▄ ▄",
    "c":"▄▄▄ ▄ ▄▄▄ ▄",
    "d":"▄▄▄ ▄ ▄",
    "e":"▄",
    "f":"▄ ▄ ▄▄▄ ▄",
    "G":"▄▄▄ ▄▄▄ ▄",
    "h":"▄ ▄ ▄ ▄",
    "i":"▄ ▄",
    "j":"▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "k":"▄▄▄ ▄ ▄▄▄",
    "l":"▄ ▄▄▄ ▄ ▄",
    "m":"▄▄▄ ▄▄▄",
    "n":"▄▄▄ ▄",
    "o":"▄▄▄ ▄▄▄ ▄▄▄",
    "p":"▄ ▄▄▄ ▄▄▄ ▄",
    "q":"▄▄▄ ▄▄▄ ▄ ▄▄▄",
    "r":"▄ ▄▄▄ ▄",
    "s":"▄ ▄ ▄",
    "t":"▄▄▄",
    "u":"▄ ▄ ▄▄▄",
    "v":"▄ ▄ ▄ ▄▄▄",
    "w":"▄ ▄▄▄ ▄▄▄",
    "x":"▄▄▄ ▄ ▄ ▄▄▄",
    "y":"▄▄▄ ▄ ▄▄▄ ▄▄▄",
    "z":"▄▄▄ ▄▄▄ ▄ ▄",
    "1":"▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄▄",
    "2":"▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "3":"▄ ▄ ▄ ▄▄▄ ▄▄▄",
    "4":"▄ ▄ ▄ ▄ ▄▄▄",
    "5":"▄ ▄ ▄ ▄ ▄",
    "6":"▄▄▄ ▄ ▄ ▄ ▄",
    "7":"▄▄▄ ▄▄▄ ▄ ▄ ▄",
    "8":"▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄",
    "9":"▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄",
    "0":"▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
    " ":"    "
}


def get_morse_code(user_input):
    global morse_code
    code = ""
    for i in range(len(user_input)):
        try:
            if morse_code.__contains__(user_input[i]): 
                code += morse_code[user_input[i]]
                if i < len(user_input)-1:
                    if user_input[i] != " ":
                        code += "   "
        except:
            pass
    return code

def morse_code_to_char(morse_code_to_convert):
    if(morse_code_to_convert == "@"):
            return " "
    for item in morse_code:
        if morse_code[item] == morse_code_to_convert:
            return item
    return ""
            
def Title():
    os.system("cls||clear")
    print("#"*50)
    print(" International Morse Code Converter ".center(50,"#"))
    print("#"*50)
    print()
Title()

option = safe_int_input_min_max("1. Text -> Morse code\n2. Morse code -> Text\n\nPlease select an option: ",1,2)
Title()

if option == 1: # Text -> Morse code
    option = safe_int_input_min_max("How do you what your Morse Code formatted\neach of the example are sos in morse code\n\n1. ▄ ▄ ▄   ▄▄▄ ▄▄▄ ▄▄▄   ▄ ▄ ▄\n2. ...   ---   ...\n3. 101010001110111011100010101\n\nPlease select an option: ",1,3)
    
    Title()

    user_input = input("Please enter the Text to be converted: ").lower().strip()
    

    user_input_morse_code = get_morse_code(user_input)

    if option == 2: # ... --- ... = sos
        user_input_morse_code = user_input_morse_code.replace("       ","@")
        user_input_morse_code = user_input_morse_code.replace("   ","|")
        user_input_morse_code = user_input_morse_code.replace("▄▄▄","-")
        user_input_morse_code = user_input_morse_code.replace("▄",".")
        user_input_morse_code = user_input_morse_code.replace(" ","")
        user_input_morse_code = user_input_morse_code.replace("|","   ")

        user_input_morse_code = user_input_morse_code.replace("@","       ")
    if option == 3:
        user_input_morse_code = user_input_morse_code.replace(" ","0")
        user_input_morse_code = user_input_morse_code.replace("▄","1")
    Title()
    print(f"Text:\n{user_input}\n\nMorse Code:\n{user_input_morse_code}\n\n")




elif option == 2:
    Title()

    code_to_convert_org = input("Please input your morse code:\n").strip().lower()
    code_to_convert = ""
    if code_to_convert_org.__contains__("1"):       
        code_to_convert_org2 = code_to_convert_org
        code_to_convert_org2 = code_to_convert_org2.replace("1","▄")
        code_to_convert_org2 = code_to_convert_org2.replace("0"," ")
        code_to_convert = code_to_convert_org2.replace("       ","   @   ").split("   ")
    elif code_to_convert_org.__contains__("."):
        print("true")
        code_to_convert_org2 = code_to_convert_org
        code_to_convert_org2 = code_to_convert_org2.replace("       ","@")
        code_to_convert_org2 = code_to_convert_org2.replace("   ","|")
        code_to_convert_org2 = code_to_convert_org2.replace(" ","")
        code_to_convert_org2 = code_to_convert_org2.replace("-","▄▄▄ ")
        code_to_convert_org2 = code_to_convert_org2.replace(".","▄ ")
        code_to_convert_org2 = code_to_convert_org2.replace("@","   @   ")
        code_to_convert_org2 = code_to_convert_org2.replace("|","   ")
        
        code_to_convert = code_to_convert_org2.strip().split("   ")
        for item in range(len(code_to_convert)):
            code_to_convert[item]= code_to_convert[item].strip()
    else:
        code_to_convert = code_to_convert_org.replace("       ","   @   ").split("   ")

    text = ""
    for item in code_to_convert:
        text += morse_code_to_char(item)

    Title()
    print(f"Text:\n{text}\n\nMorse Code:\n{code_to_convert_org}\n\n")
