#QUESTION-1
import datetime
print(datetime.datetime.now().strftime("%d"))


#QUESTION-2
import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=cwQgjq0mCdE", new=2)


#QUESTION-3
import os
files = os.listdir('path or os.curdir{current directory}')
for file in files:

    newfile = file.replace(file.split('.')[1], 'jpg')
    os.rename(file, newfile)
print(os.listdir(os.curdir))
