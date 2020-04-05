#!/usr/bin/env python3

'''Merge two pdfs in the same directory.
See http://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs-with-python/

To use this script - run it in the command line or a bash terminal.  It will prompt 
you to enter the number of files you are going to merge, then will ask for the path 
to each file, one at a time.  Finally, it will ask what name to save the merged file under.  
The file will save in the same directory as the two files to merge.  

This script is currently written to work with a mac or linux OS.  
On these systems it is easy to get the path to a file - simply right 
click the file and hold down the option key and select "copy file as pathname".  
I am not sure how it will run on a Windows system.  You will definitely have to change the '/' 
characters to '\' characters for a Windows path, and there should be a way to easily 
copy a pathname.

Mac/Linux path looks like: /Users/nicholascooper/Documents/BYU/CRE/file.pdf

If your Anaconda distribution does not have pyPDF2 installed simply run:
pip install pyPDF2
in the bash terminal or comamand line.
'''

from PyPDF2 import PdfFileMerger

def merger(output_path, input_paths):
	pdf_merger = PdfFileMerger()
	file_handles = []

	for path in input_paths:
		pdf_merger.append(path)

	with open(output_path, 'wb') as fileobj:
		pdf_merger.write(fileobj)


if __name__ == "__main__":

    numFiles = int(input("Enter number of files to merge: "))

    paths = []
    for i in range(numFiles):
        paths.append(input(f"Enter path to file {i+1}: "))

    saveas = input("Enter desired name of merged file: ")
    if saveas[-4:] != '.pdf':
        saveas += '.pdf'
    # savepath = input("Enter the path to the folder where the file will be saved: ")
    split = paths[0].split('/')[:-1]            # change to '\' for Windows
    savepath = ""
    for s in split:
        savepath += s + '/'                     # change to '\' for Windows

    print(savepath+saveas)

    merger(savepath+saveas, paths)
