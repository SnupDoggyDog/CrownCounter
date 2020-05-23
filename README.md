##Installing
Go to releases and download the exe file.
Create a new folder for this exe and put it there,in that folder make a accounts.txt where you will put your accounts in like this: username:password.
Usage
To use the .exe file its really simple
Just run the file,and it will start,it will tell you if you have entered wrong details or a captcha needs to be done,it will also tell you how many 199,299,399 and how many energy elixirs you can gift.It'll make its own output.txt file at the end.
##Building exe
$ git clone https://github.com/SnupDoggyDog/CrownCounter
$ cd CrownCounter
$ pip install -r requirments.txt
$ pip install pyinstaller
$ pyinstaller --onefile CrownCounter.py
Compiled exe should now be in the dist/ dir

##Running as python file
Download the zip file containing the .py file and requirments.txt and extract them in a folder together,make a accounts.txt as well and put accounts like: username:password.
You'll need to use CMD to CD into the directory where your CrownCounter.py and accounts.txt is located
Once you are in the directory you'll use this command: pip install -r requirments.txt.
And finally you will do python CrownCounter.py
It should automatically start checking your accounts for how much crowns they have and how much packs and energy elixirs they can gift.
