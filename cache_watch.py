# This script serves to copy new files entering Google Chrome Cache into own folder
# 
# Simple Polling used here to check for file change every 5 seconds, copied from Stack Overflow
# To address Chrome cache size limitation
import os, time, shutil, glob

path_to_watch = "/Users/<user-name>/AppData/Local/Google/Chrome/User Data/Default/Cache"
path_to_copy = "./orig/"

# clear orig folder
if not os.path.isdir(path_to_copy): os.mkdir(path_to_copy)
old_files = glob.glob(path_to_copy + "*")
for old_file in old_files:
	os.remove(old_file)
print "Successfully cleared old files"
print "Now starting to monitor new files entering cache"

# monitor cache change
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
	time.sleep (5)
	after = dict ([(f, None) for f in os.listdir (path_to_watch)])
	added = [f for f in after if not f in before]
	if added: 
		print "Added: ", ", ".join (added)
		for file in added:
			src = path_to_watch + "/" + file
			dst = path_to_copy + file
			print "Copy from: " + src + " to: " + dst
			
			# This try block catches the corner case when Chrome created the new file, but is still writing the content
			# There'll be a protection on the file before Chrome finish writing into the file, so just try copy 2 seconds later
			try:
				shutil.copyfile(src, dst)
			except IOError:
				time.sleep(2)
				shutil.copyfile(src, dst)
	before = after