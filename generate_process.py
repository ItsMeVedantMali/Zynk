# this file looks for new folders inside user uploads and convert them to reel if they are not already converted
import os

def text_to_audio(folder):
    print("TTA - ",folder)


def create_reel(folder):
    print("CR - ",folder)


if __name__=="main":
    with open("done.txt","r") as f:
        done_folders = f.readlines()



    folders = os.listdir("user_uploads")
    for folder in folders:
        if(folder not in done_folders):
            text_to_audio(folder) #Generate teh audi.mp3 from desc.txt
            create_reel(folder)   #Convert the images and audio.mp3 inside the folder to a reel 
            with open("done.txt","W") as f:
                f.write(folder + "\n")


