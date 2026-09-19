Date: 16|09|2006

```Overview```
Hii, this prject is based on the sentiment analysis based on the text which will be provided by the user. I'm implementing this with the help of TextBlob module which helps in displaying the polarity and subjective.
- In this, the polarity explain the user's response(positive, negative or netural) about the context that have been given.
- Subjective indicates the fact or the opinion of the user's text. Simpily it means where the text that the user have provided is a fact or just an opinion.

```Current Status```

All this will be implemented with the help of TextBlob as mentioned before and python Flask.
Currently I don't have any prior experience with TextBlob and I don't know a lot about Flask so I'll be spending my time of their documentation to get some insiders and internal implementation about how and what they work.

Now, for the frontend I'll be using html and css to make the webpage and the application more impressive and user friendly.
To get to know about how the `GET` and `POST` works and how I can utilize them, validate them and implement them according to my prefernces, that's I'll be more focused upon.

I'm using the Flask because I want a web server to handle the requests, a NLP library to analyze sentiment(in my case TextBlob) and the frontend(HTML and CSS) to take the inputs and display the results.

```Project Directory```
Currently I;m thinking of a simple diectory which consists of the following:
-main.py
-requrements.txt
-README.md
-frontend
    -webpage.html
    -stye.css
1. In the actual directory, the files will be present first and the files will be arranged in alphabetical order, this is just the overview so please bare with me.
I have given the main.py file first because this is the entry point of the application where the acutual code will be written.
2. The requrements.txt file cosists of all the required libraries for the sentiment_analysis, we can install the requirements with the help of `pip insall -r requrements.xt` command.
3. In the frontend folder, it consists of 2 files:
    1. webpage.html (the project structure of the application)
    2. style.css (to make the application more visually beautiful)
That's all for today, thanks for writing and I'll be coming back soon.
If you have any recommendations, feel free to reach out to me or comment.


Date: 17|09|2026

`Overview`
I have made the frontend of the application with the help of HTML, CSS and javascript. I was getting confused about which background color should I choose for my application, so I have taken 3(light, dark and darkblue) the user can adjust the Styling according to his preference by clicking on the top-right corner button. I was able to achieve this with the help of javascript which I personally liked a lot.

Most of my yesterday's time was spend on making the user interface as user friendly and attractive as possible.

Now, I'll be working on the backend of the applicatiob(Flask).

After installing the TextBlob from the requirments.txt or simply with the `pip` command. We have to download the TextBlob necessary data files(corpora) with the help of `python -m textblob.download_corpora` command executing in the terminal. This helps the sentiment analysis to work.

`NOTE`: If you have 3.11 version if Python Interpreter in you IDE then use 'pip install -r requirements.txt'
If you're using 3.14 version of Interpreter then use 'python -m pip install -r requirements.txt'.


Date: 18|09|2026
`main.py`
<!-- Write everything about this file in detail -->

How to run:
Start the server from the terminal with the help of `python main.py` command
go to http://127.0.0.1:5000 to utilize the application.

