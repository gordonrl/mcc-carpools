# Introduction

Congratulations for being elected to the EBoard position that gets to handle carpools!
I hope that all of the steps are very clear and easy, even if you don't have any computer science experience.

The basic idea of this software is to make creating carpools as fair as possible through as much randomization as possible. When I wrote this (the summer before the 2023-2024 school year) the EBoard (The Haddie Ketzenberger Administration) decided that the most fair choice was to **only create carpools for 6:45 departures on Tuesdays and Thursdays, and 9:45 for Sundays, reduce the likelyhood of someone being in a car twice in one week if there are others who have not already been selected, and to give dues paying members priority** So if anyone asks, that's how this system works.

Once again congratulations, and if you have any questions feel free to email me at gordonrl@umich.edu

# How to use
## Setup
***These only have to be done once -- your first time setting up the program***
1. Download this program from GitHub (Here's the link if you're reading this on Google Docs: https://github.com/gordonrl/mcc-carpools) and store it wherever you want on your computer as long as you can access it. To do this press "<> Code" then "Download ZIP" This will be called "mcc-carpools-main" when you download it. Feel free to rename it to whatever you want or leave it be.

2. Follow the steps up to and including "Select a Python interpreter" here: https://code.visualstudio.com/docs/python/python-tutorial. This is pretty short but it will be longer and a little more confusing if you don't have coding experience. Just type what it tells you to type where it tells you to type it and you should be fine. **For the section titled "Start VS Code in a workspace folder" open "mcc-carpools-main", or whatever you renamed it to, (i.e. the file you downloaded in step one) rather than creating a new one like they say to.**

## Standard Usage
**Unless you're intentionally modifying the program you should not have to write any code or modify any preexisting files!**

1. **You can skip this step if you already have mcc-carpools-main open in VSCode. If not:** Open VSCode, select "Open" on the welcome screen and navigate to the download from the previous step. If you already have a project open on VSCode either do "file"->"new window" to open the program but keep your previous project open or "file"->"open folder" to just open this program (This is on mac, I'm not familiar with VSCode file navigation on windows).

2. Download the carpool form responses for this week and rename the file to to "responses.csv". To do this open the Google Form, go to "responses", select the three vertical dots next to "View in Sheets", and select "Download responses (.csv)." Once you add the download to your computer (I just put in on my desktop on Mac) you can rename it to "responses.csv"

3. Download list of dues paying members as a csv and rename to "dues.csv". To do this open the dues paying members Google Sheet, select "file" under the name of the sheet, select "download", and finally "Comma Separated Values (.csv)". You can rename this the same way you renamed the responses.

4. Add "responses.csv" and "dues.csv" to VSCode, deleting last week's versions if needed. To do this select the icon in the top left of VSCode that looks like two pieces of paper (they call it "Explorer" -- If it's open you should see a list of all of the files just to the right of the icon) and drag and drop the files from wherever they are on your computer. Alternatively, you can find the folder for the entire program on your laptop (it will be called whatever you named it in step 1 of "Setup") and drag and drop the two files into it, they should show up in "Explorer" once you open VSCode.

5. In VSCode create 3 new files and name them "tuesday.csv", "thursday.csv", and "sunday.csv". To do this open "Explorer" again and select the icon that looks like a piece of paper with a plus in the bottom right corner or right click in the "Explorer" area and select "New File". You'll name the files as they're made.

6. In "Explorer", select "main.py" so its open in the main screen of VSCode ***DO NOT EDIT THIS FILE AT ALL, IT JUST NEEDS TO BE OPEN IN THE MAIN SCREEN!***

7. Press the control and f5 keys simultaneously. If all goes according to plan this should write information onto the three new files you made in step 5. If you're using a Mac with a touchbar (like me when I made this) you will also need to hold the "fn" key so the function keys show up in the touchbar.

8. Create a new Google Sheet, upload the csv files made in step 4, they should now have completed cars written in them

9. Make the sheets look pretty

10. CLEAR CARPOOL FORM RESPONSES IN PREPARATION FOR NEXT WEEK

11. Repeat weekly

***P.S. This software will only work if file format stays the same. If you do something like changing the questions (even just the wording of them!) on the Google Form or changing the format of the list of dues paying members the software will not work properly!!!!! If you need to do this either email me so I can edit the software or have a go at it yourself if you know what you're doing***

# FAQ

## Why do I only get in a car once a week?
To increase the number of people who get to go climbing, you're less likely to be put in a car on a second day if you're already in one, however you are still more likely to be put in another car than a non dues paying member (if you do pay dues). Other than this and the location you say you leave from, the process is entirely random.

## Why am I never picked?
The most likely cause of this is that your uniqname in the carpool Google form does not match your uniqname in the list of dues paying members (or you're not a dues paying member). Both the list of dues paying members and your uniqname from the Google Form are made lowercase before checking, so the issue would be a typo. **If you haven't paid dues you are significantly less likely to be selected**


# How it works (Optional)
***This section is just explaining all the nerdy CS stuff going on under the hood, feel free to skip over it if you're not interested, but it could be useful if you want to make any tweaks in the future!***

Google forms allows you to download responses in the form of a csv (comma separated values) file, which allows two conveniences:

1. Python has a module (csv) that reads in csv files and stores them as dictionaries (aka unoreded_map if you're used to c++). This makes it easy to find things like whether or not someone is a rider or driver or whether or not someone is a dues paying member.

2. Google sheets can be imported as csv files!! This means that as the program figures out cars it can write csv file(s) that can easily be sent to a sharable google sheet!


TODO: Explain the rest once you actually write the program

*P.S. This is my first Python project so if there are some poor practices I apologize! I heavily commented my code so I hope it is still readable and understandable for future carpool-makers who care to inspect it!!!*

*P.P.S. I'm sure there are faster, more streamlined ways to do this (ex: Makefile, command line funny business, Pipenv) but one of the problems with the previous carpool system was that it was very confusing and difficult to set up, even for people who kind of knew what they were doing (me!). So for this reason I decided to make some sacrifices in gracefulness and beauty in order to hopefully have it be more accessible and easier to use for future carpool-makers even if they don't know anything about coding.*

