import pyperclip

def run():
    print(f"\n\nDiscord Regional Indicator Spammer\n")
    inputString = input("Please enter in the string to spam: ")

    if len(inputString) == 0:
        exit()
    
    print(f"\n")
    RIString = ""
    for letter in inputString:
        match letter:
            case " ":
                RIString += "\n\n"
            case "a":
                RIString += ":a:"
            case "b":
                RIString += ":b:"
            case "i":
                RIString += ":information_source:"
            case "m":
                RIString += ":m:"
            case "o":
                RIString += ":o2:"
            case "p":
                RIString += ":parking:"
            case ".":
                RIString += ":record_button:"
            case "?":
                RIString += ":question:"
            case "!":
                RIString += ":exclamation:"
            case "#":
                RIString += ":hash:"
            case "*":
                RIString += ":asterisk:"
            case _:
                try:
                    intTest = int(letter)
                    #Number FOund
                    match intTest:
                        case 0:
                            RIString += ":zero:"
                        case 1:
                            RIString += ":one:"
                        case 2:
                            RIString += ":two:"
                        case 3:
                            RIString += ":three:"
                        case 4:
                            RIString += ":four:"
                        case 5:
                            RIString += ":five:"
                        case 6:
                            RIString += ":six:"
                        case 7:
                            RIString += ":seven:"
                        case 8:
                            RIString += ":eight:"
                        case 9:
                            RIString += ":nine:"
                    # print(f"", end=" ")
                except:
                    RIString += f":regional_indicator_{letter}:"
        if RIString[-1] != "\n":
            RIString += " "
    print(RIString)
    pyperclip.copy(RIString)
    print(f"String sent to clipboard.")

if __name__ == "__main__":
    while True:
        run()
