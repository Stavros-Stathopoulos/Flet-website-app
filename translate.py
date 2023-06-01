"""
    File: translate.py
    Created by: Stavros Stathopoulos
    Date: 17/05/2023
    Version: 1.1
    Place: Patras, Greece
    description:

    this file is used by the mainX.X.py file
    this file contains the following functions:
        translate_text() to translate the text from Greeklish to Greek
            this function is used to avoid any errors when the user enters the name in Greeklish
            this function is able to handle the following formats:
                Greeklish
                Greek
            the function returns the text in Greek format with the first letter of the text in uppercase

        translate_phone() to translate the phone number to the correct format
            the correct format is: 2610XXXXXX because the app was made for the University of Patras
            and the area code in Patras, Greece is 2610
            we remove the country code if it exists
            we add the area code if it doesn't exist
            this function is used to avoid any errors when the user enters the phone number in the wrong format
            this function is able to handle the following formats:
                2610XXXXXX
                00302610XXXXXX
                +302610XXXXXX
                XXXXXXXX
    these changes are necessary because the app is going to make a request to the University of Patras' website
    which is: https://ds.upatras.gr/index.php and it only accepts the search keys in specific formats
    This app was made for ths Electrical and Computer Engineering Department of the University of Patras
    in the course of introduction to the sciences of electrical and computer engineering

"""


# function to convert Greeklish to Greek
def translate_text(text):
    # dictionary with the Greek letters and their corresponding Greeklish letters
    double = False
    first = True
    letters = {
        "a": "α",
        "b": "β",
        "g": "γ",
        "d": "δ",
        "e": "ε",
        "z": "ζ",
        "h": "η",
        "th": "θ",
        "i": "ι",
        "k": "κ",
        "l": "λ",
        "m": "μ",
        "n": "ν",
        "ks": "ξ",
        "o": "ο",
        "p": "π",
        "r": "ρ",
        "s": "σ",
        "t": "τ",
        "u": "υ",
        "f": "φ",
        "x": "χ",
        "ps": "ψ",
        "w": "ω",
        " ": " ",
        "c": "κ",
        "v": "β",
        "j": "ζ",
        "q": "κ",
        "y": "ι"
    }
    traslation = ""
    # convert the text to lowercase
    text = text.lower()
    for i in range(len(text)):

        if double:
            double = False
            continue
        # check if the letter is in the Greek letter
        if text[i] in letters.values():
            return greekText(text)
        else:
            # check if the letter is a double letter like th, ks, ps
            if text[i] == "t" and text[i + 1] == "h":
                if first:
                    traslation += "Θ"
                    first = False
                else:
                    traslation += "θ"
                double = True
                continue
            elif text[i] == "k" and text[i + 1] == "s":
                if first:
                    traslation += "Ξ"
                    first = False
                else:
                    traslation += "ξ"
                double = True
                i += 1
                continue
            elif text[i] == "p" and text[i + 1] == "s":
                if first:
                    traslation += "Ψ"
                    first = False
                else:
                    traslation += "ψ"
                double = True
                i += 1
                continue
            # if the letter is not a double letter translate it
            else:
                if first:
                    traslation += letters[text[i]].upper()
                    first = False
                else:
                    traslation += letters[text[i]]
    return traslation


# function to handle the case where the user enters the name in Greek
def greekText(text):
    result = ""
    if text[0].isupper():
        return text
    else:
        for i in range(len(text)):
            if i == 0:
                result += text[i].upper()
            else:
                result += text[i]
    return result


# function to convert the phone number to the correct format
def translate_phone(phone):
    telephone = ""
    # remove the country code if it exists and its in +30 format
    if phone[0:3] == "+30":
        # check if the area code exists
        if phone[3:7] == "2610":
            telephone = phone[3:]
        # if the area code doesn't exist add it
        else:
            telephone = "2610" + phone[3:]
    # remove the country code if it exists and its in 0030 format
    elif phone[0:4] == "0030":
        # check if the area code exists
        if phone[4:8] == "2610":
            telephone = phone[4:]
        # if the area code doesn't exist add it
        else:
            telephone = "2610" + phone[4:]
    # handle the case where the user enters the phone number in the correct format
    elif phone[0:4] == "2610":
        telephone = phone
    # handle the case where the user enters the phone number without the area code
    else:
        telephone = "2610" + phone
    return telephone


if __name__ == "__main__":
    while True:
        try:
            text = input("Enter text: ")
            print(translate_text(text))
        except Exception as e:
            print(e)
