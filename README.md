# npdatocfg

Source files are at: resources/app

to open the app: download this rep and open npda2cfg.exe

### Used Libraries:
- vis.js for graph input
- electron to make it a win32 app
- ionicon for state icons
- pyshell for communictaing between python and electron/nodejs

#### How it Works!?
Main.js Loads index.html (which makes up ui), when cfg button is clicked the drawn npda is sent to python (via pyshell) as json and python script calculates cfg and prints it, which electron gets as a message. Then the recieved message is shown at cfg box

#### Weird Issues
- Lambda and arrow create problem when tranferred  between js and python. for this reason lambda and arrow are sent alongside other information
- Arrows are Somehow not right
