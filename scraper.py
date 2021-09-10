import requests
from time import sleep
import bs4
import SMS

# parse through Dayton's website and return the information to send
def parse():
    # get the covid dashboard
    url = "https://udayton.edu/coronavirus/case_dashboard.php"
    page = requests.get(url)

    # parse it to get the chart description
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    chart = soup.find_all('div',{'class':'wysiwyg'})
    chart = str(chart)

    # clean the data so it is actually readable
    index = chart.find('Chart depicting COVID-19 cases among UD students, employees and visitors since January 1, 2021.')
    print(index)
    if index != -1:
        chart = chart[index+96:]

    index = chart.find('active case')
    if index != -1:
        chart =  chart[:index+13]
    return chart

# make the text able to send and send it to all numbers in the sub list    
def push(data):
    # break it up into two texts to meet character limit
    text1 = data[:139]
    #text2 = data[139:]
    # read from the list of subscribers, then send to each one
    f = open("subscribers.txt", "r")
    subscriberList =f.readlines()
    extracted_data = []
    for i in subscriberList:
        phone = i[:10]
        print("Sending to " + phone)
        index = i.find('\n')
        provider = i[11:index]
        try:
            SMS.send(text1, phone, provider)
            #sleep(1)
            #SMS.send(text2, phone, provider)
            sleep(5)
        except:
            print('text didnt send to' + str(phone))
