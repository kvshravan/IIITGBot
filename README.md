# IIITGBot
Auto join classes using the IIITGBot written using python and selenium module. Version 1.0. The bot now has basic functionalities but not yet intelligible to determine which class to be chosen when there are two classes running simultaneously. A database or a text file can be used to store the time table which will be rolled out in the later versions. Currently it joins the class which is either ongoing or the one which is about to start. Bot works based on the assumption that no two class start or run at the same time [exception granted for HS classes, HS class variable is taken in cred.py to determine the right HS class to attend ].

## Prerequisites
Python

## Install Selenium  
Install Selenium using pip
```
pip install selenium
```

## Download Chrome driver
Download chrome driver from this [link](https://chromedriver.chromium.org/downloads) and place it in your C directory. If not specify the chrome driver path in main.py.

## Steps
1) Clone the repo

2) Fill in the creds in cred.py

## Running the IIITGBot
Run the bot using the following command :
```
python main.py
```
This bot has been written in a rush [ around 2 hours ] :) , So any pull requests fixing issues and bugs are always welcome!
