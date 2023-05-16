#Introduction

Congratulations for being elected to the EBoard position that gets to handle carpools!
I hope that all of the steps are very clear and easy, even if you don't have any computer science experience.

The basic idea of this software is to make creating carpools as fair as possible through as much randomization as possible. When I wrote this (the summer before the 2023-2024 school year) the EBoard (The Haddie Ketzenberger Administration) decided that the most fair choice was to **only create carpools for 6:45 departures on Tuesdays and Thursdays, and 9:45 for Sundays, reduce the likelyhood of someone being in a car twice in one week if there are others who have not already been selected, and to give dues paying members priority** So if anyone asks, that's how this system works.

Once again, congratulations, and if you have any questions feel free to email me at gordonrl@umich.edu

#How to use
1. Start by following the steps up to and including "Select a Python interpreter" here: https://code.visualstudio.com/docs/python/python-tutorial. This will either be a lot to do or a little depending on your prior coding experience. ***THIS STEP ONLY HAS TO BE DONE ONCE***

2. Download this program from GitHub (if you're reading this from the README.md you're in the right place, otherwise: https://github.com/gordonrl/mcc-carpools) and store it wherever you want on your computer as long as you can access it. To do this press "<> Code>" then "Download ZIP"

3. Open VSCode, select "Open" on the welcome screen and navigate to the download from the previous step. If you already have a project open on VSCode either do "file"->"new window" to open the program but keep your previous project open or "file"->"open folder" to just open this program (This is on mac, I'm not entirely sure how this part would work on Windows unfortunately).

TODO: FINISH WRITING



#How it works
***This section is just explaining all the nerdy CS stuff going on under the hood, feel free to skip over it if you're not interested, but it could be useful if you want to make any tweaks in the future! (P.S. This is my first project in Python so I apologize for any poor practices, hopefully it is adequately commented and still readable!)***

Google forms allows you to download responses in the form of a csv (comma separated values) file, which allows two conveniences:

1. Python has a module (csv) that reads in csv files and stores them dictionaries (aka unoreded_map if you're used to c++). This makes it easy to find things like whether or not someone is a rider or driver or whether or not someone is a dues paying member.

2. Google sheets can be imported as csv files!! This means that as the program figures out cars it can write csv file(s) that can easily be sent to a sharable google sheet!


TODO: Explain the rest once you actually write the program

