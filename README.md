## Installing
1. Go to releases and download the exe file.
2. Create a new folder for this exe and put it there,in that folder make a accounts.txt where you will put your accounts in like this: username:password.

## Usage
1. To use the .exe file its really simple
2. Just run the file,and it will start,it will tell you if you have entered wrong details or a captcha needs to be done,it will also tell you how many 199,299,399 and how many energy elixirs you can gift.It'll make its own output.txt file at the end.

## Building exe
```sh
$ git clone https://github.com/SnupDoggyDog/CrownCounter
$ cd CrownCounter
$ pip install -r requirments.txt
$ pip install pyinstaller
$ pyinstaller --onefile CrownCounter.py
```
Compiled exe should now be in the `dist/` dir

## Running as python file
1. Download the zip file containing the .py file and requirments.txt and extract them in a folder together,make a accounts.txt as well and put accounts like: username:password.
2. You'll need to use CMD to CD into the directory where your CrownCounter.py and accounts.txt is located
3. Once you are in the directory you'll use this command: pip install -r requirments.txt.
4. And finally you will do python CrownCounter.py
5. It should automatically start checking your accounts for how much crowns they have and how much packs and energy elixirs they can gift.
