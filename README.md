# Introduction
Congratulations for being elected to the EBoard position that gets to handle carpools!

The basic idea of this software is to make creating carpools as fair as possible through as much randomization as possible. When I wrote this (the summer before the 2023-2024 school year) the EBoard (The Haddie Ketzenberger Administration) decided that the most fair choice was to **only create carpools for 6:45 departures on Tuesdays and Thursdays, and 9:45 for Sundays, reduce the likelyhood of someone being in a car twice in one week if there are others who have not already been selected, and to give dues paying members priority** So if anyone asks, that's how this system works.

I know this is a pretty long guide but I promise it's not that bad. I just wanted to be sure that anyone, no matter their computer science experience, can make this work so we can easily get fair carpools out for the club.

Once again congratulations, and if you have any questions feel free to email me at gordonrl@umich.edu

# How to use
## Setup
***These only have to be done once -- your first time setting up the program***
1. Download this program from GitHub (Here's the link if you're reading this on Google Docs: https://github.com/gordonrl/mcc-carpools) and store it wherever you want on your computer as long as you can access it. To do this press "<> Code" then "Download ZIP" This will be called "mcc-carpools-main" when you download it. Feel free to rename it to whatever you want or leave it be.

2. Follow the steps up to and including "Select a Python interpreter" here: https://code.visualstudio.com/docs/python/python-tutorial. This is pretty short but it will be longer and a little more confusing if you don't have coding experience. Just type what it tells you to type where it tells you to type it and you should be fine. **For the section titled "Start VS Code in a workspace folder" open "mcc-carpools-main", or whatever you renamed it to, (i.e. the file you downloaded in step one) rather than creating a new one like they say to.**

## Standard Usage
**Unless you're intentionally modifying the program you should not have to write any code or modify any preexisting files!**

***If you'd prefer to watch a video for all of this I've made and included a walkthrough of these steps in the "Carpools" folder of the Google Drive***

1. **You can skip this step if you already have mcc-carpools-main open in VSCode. If not:** Open VSCode, select "Open" on the welcome screen and navigate to the download from the previous step. If you already have a project open on VSCode either do "file"->"new window" to open the program but keep your previous project open or "file"->"open folder" to just open this program (This is on mac, I'm not familiar with VSCode file navigation on windows).

2. Download the carpool form responses for this week and rename the file to to "responses.csv". To do this open the Google Form, go to "responses", select the three vertical dots next to "View in Sheets", and select "Download responses (.csv)." Once you add the download to your computer (I just put in on my desktop on Mac) you can rename it to "responses.csv"

3. Download list of dues paying members as a csv and rename to "dues.csv". To do this open the dues paying members Google Sheet, select "file" under the name of the sheet, select "download", and finally "Comma Separated Values (.csv)". You can rename this the same way you renamed the responses.

4. Add "responses.csv" and "dues.csv" to VSCode, deleting last week's versions if needed. To do this select the icon in the top left of VSCode that looks like two pieces of paper (they call it "Explorer" -- If it's open you should see a list of all of the files just to the right of the icon) and drag and drop the files from wherever they are on your computer. Alternatively, you can find the folder for the entire program on your laptop (it will be called whatever you named it in step 1 of "Setup") and drag and drop the two files into it, they should show up in "Explorer" once you open VSCode.

5. In "Explorer", select "main.py" so its open in the main screen of VSCode. You'll know it's open because its tab on the top of VSCode will be highlighted, just like a web browser. ***DO NOT EDIT THIS FILE AT ALL, IT JUST NEEDS TO BE OPEN IN THE MAIN SCREEN!***

6. Press the control and f5 keys simultaneously. This will create three files, "tuesday.csv", "thursday.csv", and "sunday.csv" that contain the carpools in a nice, easy-to-upload format. If you're using a Mac with a touchbar (like me when I made this) you will also need to hold the "fn" key so the function keys show up in the touchbar. *If you get an error saying "File exits: [file name], make sure to delete the "tuesday.csv", "thursday.csv", and "sunday.csv" files that the program created last week*

7. Create a new Google Sheet, upload the csv files made in the previous step. To do this in the sheet go "File"->"Import"->"Upload" then select one of "tuesday.csv", "thursday.csv", or "sunday.csv" (Unfortunately Google Sheets doesn't let you select multiple files at once for uploading so you'll have to do this step three times, once for each file). *For the first file you upload (probably "tuesday.csv")*, once the file is uploaded, select the dropdown undernearth "Import location" and select "Replace spreadsheet", you can leave everything else as it is (ignore the warning), then select "Import data". The process is the same for the next two files except this time *select "Insert new sheet(s) under "Import location"*. If you did this correctly then all three files should be in the same Google Sheet. There should be three tabs at the bottom, called "tuesday", "thursday", and "sunday".

8. Make the sheets look pretty. There are pictures (Carpool Upload BEFORE and Carpool Upload AFTER) in the Google Drive in the "Carpools" folder. Some of the beautification is probably unecessary but it took me like 30 seconds per sheet so it's not that bad. What really matters is that people can differentiate between cars and people adding their cars later on know how to make them look.

9. Share the Google Sheet. Change "General access" to "University of Michigan" then change the role (on the right) to "Editor", then copy the link to be put into the email/GroupMe.

10. ***CLEAR CARPOOL FORM RESPONSES AND DELETE CREATED FILES IN VSCODE IN PREPARATION FOR NEXT WEEK*** To do this go to the "Responses" section of the Google Form, click the three vertical dots next to "Link to Sheets", and select "Delete all responses". To delete the files in VSCode, open "Explorer", select "tuesday.csv", "thursday.csv", and "sunday.csv", right click, and select "delete". ***Don't delete any other files in VSCode!!!***

11. Repeat weekly

***P.S. This software will only work if file format stays the same. If you do something like changing the questions (even just the wording of them!) on the Google Form or changing the format of the list of dues paying members the software will not work properly!!!!! If you need to do this either email me so I can edit the software or have a go at it yourself if you know what you're doing***

# FAQ

Here are some answers to a few questions I anticipate being asked by people if there are complaints about not getting put in cars. If other questions come up that you cannot answer then feel free to email me: gordonrl@umich.edu

## Why do I only get in a car once a week?
To increase the number of people who get to go climbing, you're less likely to be put in a car on a second day if you're already in one, however you are still more likely to be put in another car than a non dues paying member (if you do pay dues). Other than this and the location you say you leave from, the process is entirely random.

## Why am I never picked?
The most likely cause of this is that your uniqname in the carpool Google form does not match your uniqname in the list of dues paying members (or you're not a dues paying member). Both the list of dues paying members and your uniqname from the Google Form are made lowercase before checking, so the issue would be a typo. **If you haven't paid dues you are significantly less likely to be selected**

Another possible reason is that you made a mistake when filling out the Google Form. For example, if you say you're going to be a Rider on Tuesday but then accidentally select "Not Going" for Tuesday location then you won't be eligible to be put into a car on Tuesday. I tried to reduce the chances of things like this happening as much as possible (it was a big issue with the previous software) but there's only so much I can do without falling back on making things overly-complicated again.

## Why is my car not being added to the carpools?
This would happen if you make a mistake when filling out the Google Form such as saying no to "Will you be driving at least one day this week?" or accidentally selecting "Not Going" as your location. The reason you are kept out of the carpool is these scenarios is to avoid confusion and having to cancel cars. I think people would be unhappy if they're put in a car incorrectly then can't go to the gym rather than just not being put in a car in the first place -- one is the result of randomization while the other is human error. If this happens and you still want to drive then you can still add your car to the spreadsheet manually once it is sent out.


# How it works (Optional)
***This section is just explaining all the nerdy CS stuff going on under the hood, feel free to skip over it if you're not interested, but it could be useful if you want to make any tweaks in the future!***

## How the code works

Google forms allows you to download responses in the form of a csv (comma separated values) file, which allows two conveniences:

1. Python has a module (csv) that reads in csv files and stores them as dictionaries (aka unoreded_map if you're used to c++). This makes it easy to find things like whether or not someone is a rider or driver or whether or not someone is a dues paying member.

2. Google sheets can be imported as csv files!! This means that as the program figures out cars it can write csv file(s) that can easily be sent to a sharable google sheet!

The first thing I do is create lists for the riders and drivers for each day of the week. These are global variables because a single function appends people to all of them (make_lists) but individual ones need to be used for specific functions later on (the make_day functions). The reason I don't have separate list-populating functions for each day has to do with iteration through responses.csv. I wasn't able to restart at the top of the file when trying to read it for the next day, this also saves time because I'm not iterating through responses.csv three separate times (O(n) vs O(3n) does technically make a difference. It definitely is negligible for this program as responses.csv will probably never have millions of items but it's good practice regardless).

For reading each response I can use square brackets to check if each person is either riding, driving, or not going on each given day (the make_lists function). If the person is going on the given day then I create an instance of either the Rider or Driver class (see classes.py) and append it to the list. Each class holds information necessary for printing onto the spreadsheet such as car capacity and location. Additionally I specify how to write each class as a string so that they can be easily printed in the future. This includes also means that a boolean is needed for drivers to tell whether or not it's sunday because the time is different when printing the class as a string.

The next step is to actually create the spreasheets for each day. This process is basically identical for each day. The first thing to do is check if there is anyone riding or driving on the given day. If there are no drivers then there's nothing to be done and the function just returns, if there are drivers but no riders then I still write the sheet with the information of the drivers and create spaces for riders to put their information in once the sheet is sent out in an email/in the GroupMe. If there are riders or drivers to create carpools then things are a bit of fun.

The process for creating cars is actually pretty simple (this whole program is actually pretty simple haha). For each day I go through the list of riders and check whether or not they've paid dues (and whether or not they've already been put in a car earlier in the week if it's Thursday or Sunday). Based on this information I put them on either the left or the right of a deque. Originally I was using different lists but I didn't like having so many variables so switching to a deque was nice. It makes things easy because I can put people in on different sides but only read from one. For example, for Tuesday, if a randomly selected rider paid dues then I'd append them to the right side of the deque, if they didn't pay dues then I'd append them to the left side. When actually putting them in cars I would then only take people off from the right side of the deque, thus selecting the dues paying members first! Super cool, super easy.

## How other people can easily use the code

To be honest my original hope was people could just download this code, press a few buttons and be good to go but of course it didn't turn out that way and that's okay. It's possible that this could've worked for people who don't code but it would definitely have caused issues if the next person making carpools was already coding other projects in Python. That's because of different versions of packages and Python itself. So, for this reason and from the advice of someone with infinitely more experience then me, I setup a Conda environment for this program (that's what the "environment.yml" file is for). I was a little unhappy about this because it meant that whoever does carpools next will have to download Conda and everything, but even if I didn't do this they'd end up having to download at least Python and VSCode so I'm not sure it really would've been much better. The process for downloading Conda does look a little scary but the instructions they provide are extremely well done and thorough and hopefully the instructions I write are good as well.

If you haven't used Conda before it is super cool and I'm definitely going to be using it a lot in the future so I'd recommend it. I really really hope we don't run into any Conda-related issues with sharing this software in the future!

This is a pretty broad description but hopefully it gives a general idea of what's going on. I tried ot comment my code well so I'd recommend actually taking a look at functions.py and classes.py if you aren't bored yet and really want to see what's going on.

*P.S. This is my first Python project so if there are some poor practices I apologize! I heavily commented my code so I hope it is still readable and understandable for future carpool-makers who care to inspect it!!!*

