from time import sleep
import SMS
import scraper

# get the data from udayton
file1 = open("data.txt", "r+")
oldData = file1.read()
# sleep(60)
data = scraper.parse()

#scraper.push(data)

# every 10 min check if the data has changed. If so, send text.
while True:
    if data != oldData:
        print('Website updated!')
        file2 = open("data.txt", "w")
        file2.write(data)
        file2.close()
        scraper.push(data)
        break
    elif data == oldData:
        print(data)
        print('Website the same')
        data = scraper.parse()
        sleep(600)
        
