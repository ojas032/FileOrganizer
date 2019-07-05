import os
import glob
import shutil 


def organise(add):
    os.chdir(add)
    print(os.listdir())

    src=add
    l=["*.aif","*.cda","*.mid","*.midi","*.mp3","*.mpa","*.ogg","*.wav","*.wma","*.wpl","*.py","*.c","*.class","*.cpp","*.cs","*.h",".java","*.sh","*.swift","*.vb","*.jpeg","*.jpg","*.png","*.gif","*.tiff","*.txt","*.doc","*.docx","*.odt","*.pdf","*.rtf","*.tex","*.wps","*.wpd","*.3g2","*.3gp","*.avi","*.flv","*.h264","*.m4v","*.mkv","*.mov","*.mp4","*.mpg","*.mpeg","*.rm","*.swf","*.vob","*.wmv"]

    for j in l:            
        for files in glob.glob(j):
            #pictures
            if(j in ["*.jpeg","*.jpg","*.png","*.gif","*.tiff"]):
                if not os.path.exists("fspictures"):
                    os.makedirs("fspictures")
                p="/fspictures"
                dest=src+p
                shutil.move(files,dest)
            #documents      
            elif(j in ["*.txt","*.doc","*.docx","*.odt","*.pdf","*.rtf","*.tex","*.wps","*.wpd"]):
                if not os.path.exists("fsDocuments"):
                    os.makedirs("fsDocuments")
                p="/fsDocuments"
                dest=src+p
                shutil.move(files,dest)
            #videos    
            elif(j in ["*.3g2","*.3gp","*.avi","*.flv","*.h264","*.m4v","*.mkv","*.mov","*.mp4","*.mpg","*.mpeg","*.rm","*.swf","*.vob","*.wmv"]):    
                if not os.path.exists("fsMovies"):
                    os.makedirs("fsMovies")
                p="/fsMovies"
                dest=src+p
                shutil.move(files,dest)

            #programfiles:
            elif(j in ["*.py","*.c","*.class","*.cpp","*.cs","*.h",".java","*.sh","*.swift","*.vb"]):
                if not os.path.exists("fsComp-Programs"):
                    os.makedirs("fsComp-Programs")
                p="/fsComp-Programs"
                dest=src+p
                shutil.move(files,dest)
            #Audio
            elif(j in ["*.aif","*.cda","*.mid","*.midi","*.mp3","*.mpa","*.ogg","*.wav","*.wma","*.wpl"]):
                if not os.path.exists("fsAudio"):
                    os.makedirs("fsAudio")
                p="/fsAudio"
                dest=src+p
                shutil.move(files,dest)
            #Compressed    
            elif(j in ["*.7z","*.arj","*.deb","*.pkg","*.rar","*.rpm","*.tar.gz","*.z","*.zip"]):
                if not os.path.exists("fsCompressed"):
                    os.makedirs("fsCompressed")
                p="fsCompressed"
                dest=src+p
                shutil.move(files,dest)       






