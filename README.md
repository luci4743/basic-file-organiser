# basic-file-organiser
File Organizer (Python)

A simple command-line based file organizer built using Python. This tool helps you automatically sort and organize files into categorized folders like Images, Videos, Audio, Documents, etc.

 Features
 Automatically organizes files into categories
 Reset option to move files back to original folder
 Organize a specific file or all files at once
 Simple CLI (Command Line Interface)
 Folder Structure



After running the program, the following structure is created:


├── Unorganised_Files/
│   └── (your files here)


├── Organised_Files/
│   ├── Audio/
│   ├── Executable/
│   ├── Images/
│   ├── Other/
│   ├── PDFs/
│   ├── Video/
│   └── Text/


Supported File Types
Category	Extensions  
Text:	txt, doc, docx, odt, html, xml, json, csv  
Images:	png, jpg, jpeg, gif, heic, tiff   
Video:	mp4, mov, wmv, avi, mkv     
Audio:	mp3, wav, flac, aac, ogg, m4a   
PDFs:	pdf  
Executable:	exe, bat  
Other	All unsupported files


How to Run
Clone the repository:  
git clone https://github.com/your-username/file-organizer.git  
cd file-organizer  
Run the script:  
python your_script_name.py


Usage
After running, you will see options like:

1) Organise specific file
2) Organise all Files
3) Exit Application
4) Reset
Options:
1 → Organise specific file
Select a file manually from Unorganised_Files
2 → Organise all files
Automatically organizes all files
3 → Exit
Closes the program
4 → Reset
Moves all files back to Unorganised_Files

 
 Notes
Make sure files are placed inside the Unorganised_Files folder before organizing.
If folders don't exist, the script will create them automatically.
Avoid duplicate file names to prevent overwrite issues.


Feel free to fork this repo and improve it.
