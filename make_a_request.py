import requests as req
import bs4
import re
import translate as tr

'''
    file: make_a_request.py
    writen by: S. Stathopoulos
    date: 17/05/2023
    version: 1.1
    place: Patras, Greece
    description:

    this function makes a request to the website of the Patras University
    and returns a dictionary with the results of the request
    it searches contact information of a person by name, phone or email.
    if the request is successful it returns a dictionary with the results
    if the request is not successful it returns a dictionary with the results
    and the value of the key "results" is False

    the function takes 4 arguments:
        URL: the url of the website you want to make the request, default is the url of the Patras University
                https://ds.upatras.gr/index.php
        name: the name of the person you want to search default is None
        phone: the phone number of the person you want to search default is None
        email: the email of the person you want to search default is None

    the function returns a dictionary with the results of the request
        if the request is successful it returns a dictionary with the results
        the dictionary has the following keys:
            "results": True
            "name": the name of the person
            "phone": the phone number of the person
            "email": the email of the person
            "department": the department of the person
            
        if the request is not successful it returns a dictionary with the results
        the dictionary has the following keys:
            "results": False
        
    the function uses the following libraries:
        requests as req and version 2.28.2
        bs4 known as BeautifulSoup and version 4.12.2
        re 
    
    the function uses the following functions:
        requests.post() to make the request to the website
        BeautifulSoup.find() to find the html element we want
        BeautifulSoup.findNextSiblings() to find the next html element we want
        re.compile() to compile a regular expression
This app was made for ths Electrical and Computer Engineering Department of the University of Patras
in the course of introduction to the sciences of electrical and computer engineering
'''


# noinspection PyTypedDict
def makeRequest(URL="https://ds.upatras.gr/index.php", fname=None, phone_input=None, email=None):
    name = None
    phone = None
    if fname is not None:
        name = tr.translate_text(fname)
    elif phone_input is not None:
        phone = tr.translate_phone(phone_input)

    response = {}  # the dictionary we will return
    if name is not None:
        # make the request using the requests.post() function and the name of the person
        request = req.post(URL, data={"surname": name})
    elif phone is not None:
        # make the request using the requests.post() function and the phone number of the person
        request = req.post(URL, data={"phone": phone})
    elif email is not None:
        # make the request using the requests.post() function and the email of the person
        request = req.post(URL, data={"email": email})
    else:
        # if none of the arguments were given return the dictionary with the results set to False
        response["results"] = False
        response["error"] = "No arguments were given"
        return response

    if request.status_code == 200:
        # if the request was successful.
        # parse the html of the website using BeautifulSoup
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        # find the html element we want to use BeautifulSoup.find()
        # if the result is "Δε βρέθηκαν εγγραφές." then the request was not successful due to 
        # the fact that the person we searched was not found

        if soup.find(string=re.compile("Δε βρέθηκαν εγγραφές.")):
            # return the dictionary with the results set to False
            response["results"] = False
            response["error"] = "Δε βρέθηκαν εγγραφές."

            return response
            # if the person was found then return the dictionary with the results set to True
        # find the next html element we want to use BeautifulSoup.findNextSiblings()
        else:
            result = soup.find("form").findNextSiblings()
            error = soup.find("form")
            # if the result is "Με Ελληνικούς χαρακτήρες," then the request was not successful due to
            # the fact that the person we searched was not found
            if error.text[15:40] == "Με Ελληνικούς χαρακτήρες,":
                response["results"] = False
                response["error"] = "Με Ελληνικούς χαρακτήρες, παρακαλώ."
                return response
            # if the result is "Δώστε ένα έγκυρο email ή," then the request was not successful due to
            # the fact that the email we searched was not found
            elif error.text[26:50] == "Δώστε ένα έγκυρο email ή":
                response["results"] = False
                response["error"] = "Δώστε ένα έγκυρο email ή τηλέφωνο."
                return response
            # if the result is "Σε δεκαψήφια μορφή," then the request was not successful due to
            # the fact that the phone number we searched was not found
            elif error.text[40:58] == "Σε δεκαψήφια μορφή":
                response["results"] = False
                response["error"] = "Σε 2610XXXXXX μορφή, παρακαλώ."
                return response
            # if the person was found then return the dictionary with the results set to True
            response["results"] = True
            # find the next html element we want to use BeautifulSoup.findNextSiblings()
            # and set the value of the key "name" to the text of the html element which is the name of the person
            response["name"] = result[0].text
            # we use the same method to find the phone number, email and department of the person
            response["phone"] = result[3].text
            response["email"] = (soup.find(string=re.compile("@")))
            # we use the soup.find() function to find the department of the person with the
            # help of the re.compile() function to compile a regular expression
            result = soup.find(string=re.compile("Τμήμα"))
            response["department"] = result
            # return the dictionary with the results
            return response
    else:
        # if the request was not successful return the dictionary with the results set to False
        response["results"] = False
        response["error"] = request.status_code
        return response


if __name__ == '__main__':
    while True:
        name = input("Give me a name: ")
        print(makeRequest(fname=name))
