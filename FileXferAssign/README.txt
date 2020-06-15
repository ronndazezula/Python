Files used for this project are from the EnronSent Corpus: Styler, Will (2011). The EnronSent Corpus. Technical Report 01-2011,
   University of Colorado at Boulder Institute of Cognitive Science, Boulder, CO. http://verbs.colorado.edu/enronsent/README.txt

For sound data governance reasons, the team decided not to move native files to be sent to Corporate HQ.
The shutil.copy method is employed as an alternatve to preserve the original file metadata.

See: The Python Standard Library at https://docs.python.org/3/library/shutil.html.
  "Warning Even the higher-level file copying functions...cannot copy all file metadata.
   On POSIX platforms, this means that file owner and group are lost as well as ACLs.
   On Mac OS, the resource fork and other metadata are not used.
   This means that resources will be lost and file type and creator codes will not be correct.
   On Windows, file owners, ACLs and alternate data streams are not copied."

To ensure the most recent file versions are sent to Corporate HQ:
   ***IMPORTANT!*** Files copied to the HomeOffice folder replaces files with the same file name and extension.
   Refer to Data Governance Policy 5.1 for version control processes (e.g., file storage locations and file naming conventions).
	See Dev for a historical log of transfers or with questions about using this application.

TO USE THIS APPLICATION:

At any time, before or after the transfer (copy) process is complete, Click Exit to leave the application.
  [Note: if you have clicked 'Copy files...' (step 9) that process will complete before you can Exit.]

1.  Open 'FileXfer_main.py' in Python

2.  "Hit" the F5 button on your keyboard.

3.  Click 'Get files from...'

4.  Browse to the folder containing files added or altered since the previous transfer (source).
      [Note: the app automatically navigates to customary location.]

5.  Click 'Select Folder'.

6.  Click 'Copy files to...'.

7.  Browse to the folder the files should be copied to (destination).
      [Note: the app automatically navigates to customary location.]

8.  Click 'Select Folder'.

9.  When both source and destination are set, Click 'Copy files...'.

10. Click 'Ok' then 'Exit' to leave the application.
