# Medict-Health-Analyzer

Note: MUST USE PYTHON 32 BIT (preferably 3.9.0 and on Windows)

Use these commands to run
1) go to the folder you want this to run in 
2) ```git clone https://github.com/shloakr/Medict-Health-Analyzer.git```
3) ```virtualenv med-analyzer```
4) ```source med-analyzer/bin/activate```
5) ```pip install -r /path/to/requirements.txt```
6) ```python app.py```
7) run ```http://localhost:5000/``` on your browser 

-------------------------------------------------------------------------------------------------

If that does not work, you can also clone the repos like above
and then pip install the following packages
(or ```pip install -r /path/to/requirements.txt```):
1) ```scikit-learn```
2) ```pandas```
3) ```numpy```
4) ```flask```

Then run app.py by typing the following in cmd:
```C:\Users\{user}\AppData\Local\Programs\Python\Python38-32\python.exe C:/path/to/app.py```
Make sure you call the full path to python.exe or it may cause errors.

Finally, run ```http://localhost:5000/``` on your browser.


-------------------------------------------------------------------------------------------------

## Inspiration
**$2.2 trillion** is spent on healthcare each year in the US alone.
We could save so much money, and so many families from stress, if we prevent the diseases from happening in the first place.

## What it does
A website that predicts that you'll get a disease before you get it.
Users will input personal data such as weight, age, and country of residence. Using that info, we will tell them what diseases they are likely to face in the future with the power of machine learning.

## How we built it
We used Flask to develop the frontend and seamlessly integrate it with a machine learning model. 
We also used HTML and CSS for the front end.
We trained the "National Center for Health Statistics" Dataset with TensorFlow and Pandas

## Challenges we ran into
**Formatting the Data** - Formatting multiple large datasets while only selecting specific column values was tough and took us multiple hours to get right.
**Accuracy** - The accuracy was initially pretty bad, but with lots of trial and error picking inputs and model types, we were able to get the average accuracy to be 85%+
**Frontend** - We tried a glass blur effect for our input form. Initially, it was lackluster, but after multiple revisions, we got it to look better. 

## Accomplishments that we're proud of
Creating this website in less than 2 days. Working together as a team despite sitting in different corners of the world.

## What we learned
**Machine Learning** - We learned a lot about machine learning, like how to format complex data and the effectiveness of various models.
**Frontend** - We learned how to incorporate new design techniques like glass blur and still keep convenience in mind. 
**Collaboration** - We learned how to work over different time zones as our members were 9 hours 30 minutes apart. 

## What's next for Medict Health Analyzer
We plan to expand on this website in the future by having the user input symptoms they're currently having and diseases that run in their family. This data will help make our output even more accurate. We might soon turn Medict Health Analyzer into an app!

## Team Mebers
1) Matthew Zahian
2) Reanna Chowdhury
3) Kevin L
4) Shloak Rathod
