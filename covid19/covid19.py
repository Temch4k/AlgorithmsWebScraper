# Artsiom Skarakhod
# 3/30/2020
# Extra Credit
import bs4 as bs
import requests
import webbrowser


# makes sure that the space is an int when it's compared
def clean(bob):
    # if bob is not a number then turn it into a zero
    if bob != " " and bob != "":
        # if it is a number then remove comma
        return bob.replace(",", "")
    else:
        return 0


# gets the url
url = "https://www.worldometers.info/coronavirus/"
html_content = requests.get(url).text

# reads off the html and puts it into soup
soup = bs.BeautifulSoup(html_content, features="html.parser")

# finds the table inside the soup
table = soup.find(id="main_table_countries_today")

# finds all the rows starting with tr
rows = table.find_all('tr')

# creates an array that stores arrays inside of itself
papa = []

# while there are still rows keep on reading it in
for tr in rows:

    td = tr.find_all('td')
    r = [i.text for i in td]
    # if the line is not blank then add it to the array
    if r != []:
        papa.append(r)

# sorts the array full of arrays by the 8th spot of the inside array
papa.sort(key=lambda x: float(str("0" if x[8] == "" else x[8]).replace(",", "")))
# reverses the array
papa.reverse()

# got this form homework 2
f = open('table.html', 'w')
# clreates a message out of html and then will be put into html file
# uses """+str(list[0])+""" to put values into the document's table
message = """
    <head>
    <style>
        table, th, td {
          border: 2px solid grey;
          border-collapse: collapse;
        }
    </style>
    </head>

    <table>
        <tbody>
            <tr>
                <td>Country</td>   
                <td>Total Cases</td>
                <td>Total Deaths</td>
                <td>Total Recovered</td>
                <td>Total cases/ 1M</td>
                <td>Death/Confirmed</td>
                <td>Recovered/Confirmed</td/>
            </tr>
"""

# they will be added between each row
header = "\n            <tr>"
ender = "\n            </tr>"
#add every papa row into the table
for x in range(len(papa)):

    txtLine = ""
    r = papa[x]
    message = message + header
    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(r[0])
    txtLine = txtLine + "</td>"

    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(r[1])
    txtLine = txtLine + "</td>"

    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(r[3])
    txtLine = txtLine + "</td>"

    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(r[5])
    txtLine = txtLine + "</td>"

    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(r[8])
    txtLine = txtLine + "</td>"

    dPrecent = (int(clean(r[3])) / int(clean(r[1]))) * 100

    dPrecent = round(dPrecent, 2)

    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(dPrecent) + "%"
    txtLine = txtLine + "</td>"

    aPrecent = (int(clean(r[5])) / int(clean(r[1]))) * 100

    aPrecent = round(aPrecent, 2)

    txtLine = txtLine + "\n                <td>"
    txtLine = txtLine + str(dPrecent) + "%"
    txtLine = txtLine + "</td>"

    message = message + txtLine
    message = message + ender

end = "\n        </tbody>"
end2 = "\n    </table>"

# adds the last two parts to html
message = message + end + end2

# prints the output
print(message)

# adds the html into the file
f.write(message)
f.close()
webbrowser.open_new_tab('table.html')
