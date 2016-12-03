# pyDhammapada
Displays random verses from a Buddhist book called the Dhammapada

I have another program that is very similar - called Hakagure.

This version has the WHOLE book (The Dhammapada) stored in a text file, and when the button is selected, a random verse is displayed to the user. The GUI version allows the user to just keep clicking to see new verses, and the text version asks the user if they want another verse.

This book is quite personal to me, I have taken a lot of wosdom and advice from within its pages, and applied it to real life. Even if you are not a full procticing Buddhist, you can get a lot from this book. It is freely available to read or download, as long as it is in a non-profit way, so not to make money off it. 

The wisdom and advice is very much applicable to real life situations in our modern times. I wanted to make a little program out of it as it is something I like a lot.

The program itself:
-----------------------
The whole book is 423 verses. Each verse has been put into an individual line within a text file. The function that handles everything is almost the same in both plain and GUI versions...it picks a random line from the text file and displays it.

With this versionm I didn't have too much trouble with this because the verses are all quite short, and the text file didn't end up being too large. I used the same function as I did in Hakagure.

In the Hakagure version I had trouble, because the verses are really long, so with the whole verse condensed into 1 line, it was printing out an ugly block of text each time - no spacing or paragraphing etc. The other problem was that the way in which Python picked the random line seemed to favour the mid-length lines only, meaning the shorter and longer lines weren't being shown - almost non-random! so I had a look at different methids of doing the random line and the method I went with is more reliable - it really is a random choice of lines, regardless of length.

Use:
------
* Both versions require the same text file (dhammapada.txt) to store and show verses
* Written and tested in Python 3
* Needs no extra modules (plain version is just python3 and GUI version uses Tkinter which comes with python by default)
* Just run the Python file as normal (open and run in IDLE, or another IDE, or with a terminal command)  

