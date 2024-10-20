
import os
 #We can use the remove() method of the os module to remove a file not a directory.
os.remove('h.txt')
# similarly we can use rmdir() to delete directory
os.rmdir('Folder_name')

#removing a directory is that the directory must be empty. 
# Otherwise, an exception will be raised.