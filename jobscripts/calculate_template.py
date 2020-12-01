import os
from vsc_irods.session import VSCiRODSSession
import matplotlib.pyplot as plt


with VSCiRODSSession(txt='-') as session:
    #Download all the files from irods collection molecules/Or download molecules as collection
    session.bulk.get(...)   
    
    #Do some calculation, count all hydrogens in files
    hydrogen_count=0
    for i in os.listdir("./molecules"):
        with open("./molecules/"+i, "r") as file:
            for character in file.read():
                if character == "H":
                    hydrogen_count += 1
    
    #Create a simple plot based on the counted number of hydrogens and the files.
    #Save it as a png file to upload it to iRODS
    plt.plot([len(os.listdir("./molecules")),hydrogen_count])
    plt.savefig("figure.png")
                    
    #Create a result directory(collection) in the irods training collection
    #Change your collection to the result collection
    session.path. ...
    session.path. ...
    
    #Upload the png file to iRODS, stageout the output result    
    session. ...
    
    #Add some different metadata to the result collection and the output file
    session. ...
    session. ...
    