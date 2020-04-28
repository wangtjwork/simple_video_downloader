# This script serves to copy binary files from './orig' folder to './dest' folder, and rename according to sequence
# 
# The rename is based on the fact that Chrome uses 16-based naming for cache, and windows copy method could not figure out the correct sequence of cached files
# Therefore translated into 10-based and add zero-padding for windows to correctly detect the sequence of files
# 
# The "v_" was a personal preference
# 
# The program may fail to correctly run if the file number exceed 10^6, when the padding is not enough to create correct sequence
import os
import glob
import shutil

orig_path = "./orig/"
dest_path = "./dest/"
copy_cmd = "copy /b .\\dest\\v_* .\\" # command found somewhere on youtube to combine binary ts files

# prompt user for new file name
new_video_file_name = raw_input("What will the new file name be?") + ".ts"
print "New file would be " + new_video_file_name

# capture all files to be copy & rename
files = list(filter(os.path.isfile, glob.glob(orig_path + "f_*")))
files = [os.path.basename(f) for f in files]

# clear dest folder
if not os.path.isdir(dest_path): os.path.mkdir(dest_path)
old_files = glob.glob(dest_path + "*")
for old_file in old_files:
	os.remove(old_file)
print "Successfully cleared old files"

print "Copying original files..."
# copy to destination and rename
for filename in files:
	file_num = filename.split("_")[1]
	new_file = "v_" + str(int(file_num, 16)).zfill(6)
	shutil.copyfile(orig_path + filename, dest_path + new_file)

print "Compressing video..."
# combine all files into new file
os.system(copy_cmd + new_video_file_name)
	
exit()