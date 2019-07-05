import os
import glob
import shutil 


os.chdir("C:\\Users\Ojas Gupta\Pictures")
print(os.listdir())

src="C:\\Users\Ojas Gupta\Pictures"
l=["*.py","*.c","*.class","*.cpp","*.cs","*.h",".java","*.sh","*.swift","*.vb","*.jpeg","*.jpg","*.png","*.gif","*.tiff","*.txt","*.doc","*.docx","*.odt","*.pdf","*.rtf","*.tex","*.wps","*.wpd","*.3g2","*.3gp","*.avi","*.flv","*.h264","*.m4v","*.mkv","*.mov","*.mp4","*.mpg","*.mpeg","*.rm","*.swf","*.vob","*.wmv"]



for j in l:
    if(j in ["*.jpeg","*.jpg","*.png","*.gif","*.tiff"]):
        if not os.path.exists("fspictures"):
            os.makedirs("fspictures")
        p="/fspictures"
        dest=src+p
    elif(j in ["*.txt","*.doc","*.docx","*.odt","*.pdf","*.rtf","*.tex","*.wps","*.wpd"]):
        if not os.path.exists("fsDocuments"):
            os.makedirs("fsDocuments")
        p="/fsDocuments"
        dest=src+p
    elif(j in ["*.3g2","*.3gp","*.avi","*.flv","*.h264","*.m4v","*.mkv","*.mov","*.mp4","*.mpg","*.mpeg","*.rm","*.swf","*.vob","*.wmv"]):
        if not os.path.exists("fsMovies"):
    
            os.makedirs("fsMovies")
        p="/fsMovies"
        dest=src+p
    elif(j in ["*.py","*.c","*.class","*.cpp","*.cs","*.h",".java","*.sh","*.swift","*.vb"]):
        if not os.path.exists("fsComp-Programs"):
            os.makedirs("fsComp-Programs")
        p="/fsComp-Programs"
        dest=src+p

        
    for files in glob.glob(j):
        #pictures
        if(j in ["*.jpeg","*.jpg","*.png","*.gif","*.tiff"]):
            shutil.move(files,dest)
        #documents      
        elif(j in ["*.txt","*.doc","*.docx","*.odt","*.pdf","*.rtf","*.tex","*.wps","*.wpd"]):
            shutil.move(files,dest)
        #videos    
        elif(j in ["*.3g2","*.3gp","*.avi","*.flv","*.h264","*.m4v","*.mkv","*.mov","*.mp4","*.mpg","*.mpeg","*.rm","*.swf","*.vob","*.wmv"]):    
            shutil.move(files,dest)

         #programfiles:
         elif(j in ["*.py","*.c","*.class","*.cpp","*.cs","*.h",".java","*.sh","*.swift","*.vb"]):
             shutil.move(files,dest)   




