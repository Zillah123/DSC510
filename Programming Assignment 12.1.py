#File name: Programming Assignment 12.1.py
#Name: Emmanuel Vidal
#Date: 02/28/2020
#Course: DSC510-T302 - Introduction to Programming (2203-1)
#Assignment number: 12.1
#Purpose of the assignment: Class Project. Creating an application to interacts with a webservice in order to obtain data.
print("Welcome Prof. Michael Eller. Thank you for grading my assignment") #Welcome Message
import requests
def main(): #Main function
    api_key = "680a8857e7c70fab55b34c1d45fd47ad" #Api key
    fahrenheit_unit = "imperial" #Using Fahrenheit unit for temperature
    base_url = "http://api.openweathermap.org/data/2.5/weather?" #Host website address
    request_user(api_key,fahrenheit_unit,base_url) #Calling the request_user function

def request_user(api_key,fahrenheit_unit,base_url): #Functions to request weather condition with 3 parameters passed
    while True: #While true execute the following
        user_cont = input('Do you want to look up another location weather condition, Y for yes and N for No?')  # Options for user to look up weather location
        if user_cont == 'Y':  # user selects Y do the following
            user_cont1=input('To search by city enter C, to search by zip code Z and enter Q to quit:') #Ask for user preference for search Zipcode, City ot quit
            if user_cont1.upper()=='Q': #User select quit
                print("You have chosen to quit") #Display user option of quit
                break #Break and exit the program

            else:#User selects something else
                if user_cont1=='C': #Selects to search for weather by City
                    print('You have chosen to search by City') #Display option the user selects
                    city_search(api_key,fahrenheit_unit,base_url) #Call the City search function
                elif user_cont1=='Z': #User selcts Z, zipcode search
                    print('You have chosen a zip code search')#Display user option of zip code search
                    zipcode_search(api_key,fahrenheit_unit,base_url)#Call the zipcode search function
                else:
                    print('Invalid Response')#Print invalid response if none of the 3 options (C,Z,Q) are chosen
        elif user_cont == 'N':#User selects No to looking up another location weather
            break #Quit the program
        else:#Else
            print("Invalid User Input")#Print Invalid response if none is chosen

def city_search(api_key,fahrenheit_unit,base_url): #City Search Function
    try:
        city_name = input("Enter city name:") #User enters city name(We were only told to do a city search and not city and state)
        if city_name.isalpha(): #If input is in alphabeths do the following
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + fahrenheit_unit #Assign the search to a variable called complete_url
            try:#Try the following
                response = requests.get(complete_url)#Assign the variable response to the request to get the complete data from the complete url
                print("Connection Successful")
                print(response.text)
            except requests.exceptions.HTTPError as er:#If the try was not successful and the reason was a HTTPError
                return "An Http Error Occurred:" + repr(er) #Return an HTTP Error occurred
            except requests.exceptions.ConnectionError as err: #If connection error
                return "An Error Connecting to the API occurred:" + repr(err) #Return this
            except requests.exceptions.Timeout as errh: #If time-out error
                return "A Timeout Error Occurred" + repr(errh) #return this
            except requests.exceptions.RequestException as e: #If exception error
                print(e) #PRint Error
                print("Connection unsuccessful please try again ")
            x = response.json() #Assign the variable x to parse the response
            pretty_print(city_name, x) #Call the function pretty_print to print the results

        else: #If Data entered for city search is not in alphabelts do the following
            print("Invalid data, Start from the beginning")#Return invalid data and start from the begining i.e "Do you want to look up another location"
    except:
        print('Enter Valid City name')

def zipcode_search(api_key,fahrenheit_unit,base_url):#Zip code search function with 3 parameters passed unto it
    try: #Try your zip code search with this
        zip_code=input("Enter Zip Code:") #Enter zipcode
        if zip_code.isdigit():#Zip code is a digit
            complete_url = base_url + "appid=" + api_key + "&zip="+zip_code + "&units=" + fahrenheit_unit #Complete URL to get weather information from the weather API
            try: #Try this
                response = requests.get(complete_url) #Get the complete URL REsponse
                print("Connection Successful") #Shows connection was successful
                print(response.text)
            except requests.exceptions.HTTPError as er:#If the try was not successful and the reason was a HTTPError
                return "An Http Error Occurred:" + repr(er)#Return an HTTP Error occurred
            except requests.exceptions.ConnectionError as err:#If connection error
                return "An Error Connecting to the API occurred:" + repr(err)#Return this
            except requests.exceptions.Timeout as errh:#If time-out error
                return "A Timeout Error Occurred" + repr(errh)
            except requests.exceptions.RequestException as e:#If exception error
                print(e)#PRint Error
                print("Connection unsuccessful please try again ")
            x = response.json()
            pretty_print2(zip_code, x)#Call the function pretty_print to print the results for zipcode search
        else:
            print("Invalid data, Start from the begining")
    except:
        print('Enter Valid Zip-Code')




def pretty_print(city_name,x):#Function to print for search by city name
    print("Current Weather Conditions For", city_name)#Display weather conditions for this city
    y=x["main"]#Create a variable to parse through the dictionary
    print("Current Temp:",y["temp"],chr(176),"F",sep="")#Print the current temperature in fahrenheit
    print("It feels like:",y["feels_like"],chr(176),"F",sep="")#It feels like what
    print("High Temperature:",y["temp_max"],chr(176),"F",sep="")#High Temperature
    print("Low Temperature:",y["temp_min"],chr(176),"F",sep="")#Low Temperature
    print("Pressure:",y["pressure"],"hPa",sep="")#PRessure and the unit
    print("Humidity:",y["humidity"],"%",sep="")#Humidity and the unit

def pretty_print2(zip_code,x):#PRint Function to print the results of Zip code search
    print("Current Weather Conditions For", zip_code)#Print Current Weather conditions for the zip code
    y = x["main"]#Create a variable y for the response of which I select main where the data for temp resides
    print("Current Temp:", y["temp"], chr(176), "F", sep="") #Print the current temperature in fahrenheit
    print("It feels like:", y["feels_like"], chr(176), "F", sep="")#It feels like what
    print("High Temperature:", y["temp_max"], chr(176), "F", sep="")#High Temperature
    print("Low Temperature:", y["temp_min"], chr(176), "F", sep="")#Low Temperature
    print("Pressure:", y["pressure"], "hPa", sep="")#PRessure and the unit
    print("Humidity:", y["humidity"], "%", sep="")#Humidity and the unit


if __name__ == '__main__':
    main()
