This python script parses both the Radio Times and the Guardian TV recommendations sections and generates a text file in a format that can be read by TVWish http://www.templetons.com/brad/myth/tvwish.html and recorded with MythTV.

It works with Python 2.6.5, but not Python 3.

To use first setup TVWish, then download and save the recommend.py file. 

Create a text file called recommendations.txt in your TVWish/personal directory. It can be handy to symlink it to a file in a dropbox folder so that you can read it and edit it from other computers, or from a smartphone. 

ln -s /home/user/tvwish/personal/recommendations.txt /home/user/Dropbox/recommendations.txt

Add this text file to your tvwish/personal/master file:

Include: personal/recommendations.txt Priority=-2

It is best to insert this line near the end of the master file but before the TV suggest line. That way anything that comes up on one of your other lists first gains a higher priority on MythTV and if TVWish Suggest picks the same show as the recommender then it will get the higher priority from the recommender. Of course you may want to tweak the priority level to suit your setup.

You can also create a new group in MythTV and add these programmes to that group. Just change the master file line to include the group:

Include: personal/recommendations.txt Priority=-2 Group=Recommendations

Edit the recommendations.py file to the correct file path for your new recommendations.txt file. Also edit the unwanted titles and channels to suit your tastes and setup.

This script requires BeautifulSoup, to install:
sudo apt-get install python-beautifulsoup

Test the setup by running the python code. You will need to make sure it is marked as executable first.

python recommend.py

Check the recommendations.txt file, it should look something like this:

#Radio Times highlights on 2011-06-06
Show: Injustice
#James Purefoy stars as a barrister who moves to Suffolk and ends up in a cat-and-mouse game with a local detective. New thriller series from writer Anthony Horowitz.
Show: The Restaurant Inspector
#Fernando Peire looks like he's bitten off more than he can chew when he tries to rejuvenate the failing Margate restaurant of an unspeakably rude owner.
Show: Psychoville 2
#Reece Shearsmith and Steve Pemberton continue the dark - so very, very dark - comedy thriller with the strangest characters on TV.
Show: Glee
#A surprising left turn for the drama when the championships take a back seat after the death of a character. A beautifully effective change of gear.
27 Dresses
#In this fluffy, New York-set romantic comedy, Katherine Heigl (Knocked Up) plays Jane, a woman who is always the bridesmaid, never the bride - and she has 27 bridesmaid dresses in her wardrobe to prove it.

If there are any shows you aren’t interested in then either delete them or just put a # at the beginning of that line, and save the file. Like this:

#Radio Times highlights on 2011-06-06
Show: Injustice
#James Purefoy stars as a barrister who moves to Suffolk and ends up in a cat-and-mouse game with a local detective. New thriller series from writer Anthony Horowitz.
Show: The Restaurant Inspector
#Fernando Peire looks like he's bitten off more than he can chew when he tries to rejuvenate the failing Margate restaurant of an unspeakably rude owner.
Show: Psychoville 2
#Reece Shearsmith and Steve Pemberton continue the dark - so very, very dark - comedy thriller with the strangest characters on TV.
#Show: Glee
#A surprising left turn for the drama when the championships take a back seat after the death of a character. A beautifully effective change of gear.
27 Dresses
#In this fluffy, New York-set romantic comedy, Katherine Heigl (Knocked Up) plays Jane, a woman who is always the bridesmaid, never the bride - and she has 27 bridesmaid dresses in her wardrobe to prove it.

Now Glee won’t be recorded.

Add the recommend.py to your cron file:

crontab -e 
0 6 * * * python /home/user/recommend.py
This would run at 6am every day. Leave a few hours between running this and running TVWish so you can check the file first and remove anything you don't want before they are set up to record.

www.kbuss.co.uk
