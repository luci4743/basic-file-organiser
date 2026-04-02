import os
import shutil
import sys


def Organise_byUser(file):
    if file.endswith(("txt","doc","docx","odt","htm","html","xml","json","csv")):
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Text"))
        print(f"{file} moved to Text Folder")

    elif file.endswith(("png","jpg","jpeg","heic","gif","tiff")):
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Images"))
        print(f"{file} moved to Images Folder")

    elif file.endswith(("mp4","mov","wmv","avi","mkv")):
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Video"))
        print(f"{file} moved to Video Folder")

    elif file.endswith("pdf"):
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","PDFs"))
        print(f"{file} moved to PDFs Folder")

    elif file.endswith(("mp3","aac","ogg","flac","wav","m4a")):
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Audio"))
        print(f"{file} moved to Audio Folder")    

    elif file.endswith(("exe","bat")):
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Executable"))
        print(f"{file} moved to Executable Folder")    

    else:
        shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Other"))
        print(f"{file} moved to Other")
    

def Folder_Creator():

    Main_Files = ["Organised_Files","Unorganised_Files"]
    for Folder_type in Main_Files:
        if os.path.exists(Folder_type):
            pass
        else:
            os.mkdir(os.path.join(Folder_type))
                     

    Type_list = ["Audio","Executable","Images","Other","PDFs","Video","Text",]
    for Folder_type in Type_list:
        if os.path.exists(os.path.join("Organised_Files",Folder_type)):
            pass
        else:
            os.mkdir(os.path.join("Organised_Files",Folder_type))

def User_Input(): 
    user_ans = input("\n 1)Organise specific file \n 2)Organise all Files \n 3)Exit Application \n 4)Reset \n: ")

    if user_ans=="1":
        print([name for name in os.listdir("Unorganised_Files") if os.path.isfile(os.path.join("Unorganised_Files",name))])
        file_input = input("\nEnter a file name \n:")
        try:
            Organise_byUser(file_input)
        except:
            print(f"{file_input} not found \n")
        finally:
            User_Input()    
        
    elif user_ans=="2":
        Organise_all()
        User_Input()

    elif user_ans=="3":
        print("Application closed! \n")
        sys.exit()

    elif user_ans=="4":
        Reset_Files()
        User_Input()

    else:
        print("Please choose a correct option")
        User_Input()


def Organise_all(): #to-do add print statements for all the move function , find ways to print with loop
    File_list = [name for name in os.listdir("Unorganised_Files") if os.path.isfile(os.path.join("Unorganised_Files",name))]
    for file in File_list:
        if file.endswith(("txt","doc","docx","odt","htm","html","xml","json","csv")):
            shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Text"))
            print(f"{file} moved to Text Folder")

        elif file.endswith(("png","jpg","jpeg","heic","gif","tiff")):
            shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Images"))
            print(f"{file} moved to Images Folder")
            
        elif file.endswith(("mp4","mov","wmv","avi","mkv")):
            shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Video"))
            print(f"{file} moved to Video Folder")

        elif file.endswith("pdf"):
            shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","PDFs"))
            print(f"{file} moved to PDFs Folder")

        elif file.endswith(("mp3","aac","ogg","flac","wav","m4a")):
            shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Audio"))
            print(f"{file} moved to Audio Folder")

        else:
            shutil.move(os.path.join("Unorganised_Files",file),os.path.join("Organised_Files","Other"))
            print(f"{file} moved to Other Folder")
        

def Reset_Files(): 
    Type_list = ["Audio","Executable","Images","Other","PDFs","Video","Text"]
    for name in Type_list:
        for sub_name in os.listdir(os.path.join("Organised_Files",name)):
            if os.path.isfile(os.path.join("Organised_Files",name,sub_name)):
                shutil.move(os.path.join("Organised_Files",name,sub_name),"Unorganised_Files")



Folder_Creator()
# Reset_Files()
User_Input()
