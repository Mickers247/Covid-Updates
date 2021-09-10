### Covid-Updates ###

Mick Ward

## About ##

During my fall 2020 semester at University of Dayton, the Unviersity created a dashboard that was very transparent about how many covid cases there were on campus. However, it would update daily at seemingly random times, so people had no idea what time to check for the new cases. Because of the web scraping techniques I had learned in my internship at Ingram Micro, I decided I would make a tool to send notifications as soon as the website updated.

Scraping the website was relatively easy, and I had the script running on my Pi constantly, but how it would notify me (and others) was the major problem. It was fairly easy for me to send email's with python, but Reddit tipped me off on how to send text messages. Apparently, all phone numbers have an email you can send emails to that convert to SMS. These emails consist of the phone number, and then some domain that is relative to the carrier.

I collected my peers numbers and carriers and have my script send an email to their SMS emails when the website changed. Many of my friends and profesors loved this because it kept them updated on how safe the campus was!

## How it works ##

Every 10 minutes the script checks if the description of the image on Dayton's covid campus status dashboard has changed. It does this by comparing it to the previous text that was sent out, which is stored in data.txt. Then, it will send a text message to everyone in subscribers.txt, which must consist of a 10 digit number and the name of their carrier. It also writes the new text into data.txt, and continues to check if it changes.
