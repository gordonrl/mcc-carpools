# Introduction

Congratulations for being elected to the EBoard position that gets to handle carpools!
I hope that all of the steps are very clear and easy, even if you don't have any computer science experience.

The basic idea of this software is to make creating carpools as fair as possible through as much randomization as possible. When I wrote this (the summer before the 2023-2024 school year) the EBoard (The Haddie Ketzenberger Administration) decided that the most fair choice was to **only create carpools for 6:45 departures on Tuesdays and Thursdays, and 9:45 for Sundays, reduce the likelyhood of someone being in a car twice in one week if there are others who have not already been selected, and to give dues paying members priority** So if anyone asks, that's how this system works.

Once again congratulations, and if you have any questions feel free to email me at gordonrl@umich.edu

# How to use
## Setup
***These only have to be done once -- your first time setting up the program***
1. Download this program from GitHub (Here's the link if you're reading this on Google Docs: https://github.com/gordonrl/mcc-carpools) and store it wherever you want on your computer as long as you can access it. To do this press "<> Code" then "Download ZIP

2. Follow the steps up to and including "Select a Python interpreter" here: https://code.visualstudio.com/docs/python/python-tutorial. This is pretty short but it will be longer and a little more confusing if you don't have coding experience. Just type what it tells you to type where it tells you to type it and you should be fine. **For the section titled "Start VS Code in a workspace folder" open mcc_carpools (the file you downloaded in step one) rather than creating a new one like they say to.**

## Standard Usage
1. **You can skip this step if you already have mcc_carpools open in VSCode** Open VSCode, select "Open" on the welcome screen and navigate to the download from the previous step. If you already have a project open on VSCode either do "file"->"new window" to open the program but keep your previous project open or "file"->"open folder" to just open this program (This is on mac, I'm not familiar with VSCode file navigation on windows).

TODO: FINISH WRITING



# How it works (Optional)
***This section is just explaining all the nerdy CS stuff going on under the hood, feel free to skip over it if you're not interested, but it could be useful if you want to make any tweaks in the future!***

Google forms allows you to download responses in the form of a csv (comma separated values) file, which allows two conveniences:

1. Python has a module (csv) that reads in csv files and stores them dictionaries (aka unoreded_map if you're used to c++). This makes it easy to find things like whether or not someone is a rider or driver or whether or not someone is a dues paying member.

2. Google sheets can be imported as csv files!! This means that as the program figures out cars it can write csv file(s) that can easily be sent to a sharable google sheet!


TODO: Explain the rest once you actually write the program

*P.S. This is my first Python project so if there are some poor practices I apologize! I heavily commented my code so I hope it is still readable and understandable for future carpool-makers who care to inspect it!!!*

*P.P.S. I'm sure there are faster, more streamlined ways to do this (ex: Makefile, command line funny business, Pipenv) but one of the problems with the previous carpool system was that it was very confusing and difficult to set up, even for people who kind of knew what they were doing (me!). So for this reason I decided to make some sacrifices in gracefulness and beauty in order to hopefully have it be more accessible and easier to use for future carpool-makers even if they don't know anything about coding. *

