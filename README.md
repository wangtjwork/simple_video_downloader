# Simple Video Downloader

This downloader could be tried on video without a visible 'download' button.

## Introduction
Video platforms typically slice the video file into small chunks and send them one by one. The browser receives the files in sequence and plays one by one, which appears as continuous video to the end-user.

For some platforms, their content is put into browser cache to achieve a smoother user experience. This program watches over browser cache and extracts the newly added video files into another folder. Then the user could compress all chunks into a whole video again.

## Motivation
Yesterday one of my paid podcasts was telling me my access time expires within 9 months. I would still like to return to the videos probably a year afterward, so I set out to learn about the ways I could locally save the video file and watch whenever I like. With the only tools already installed on my computer, and given the fact that I'm not familiar with Windows command line, Python 2.7 was chosen as the scripting language.

## Check Video Applicability
Steps to see if a video could be downloaded with this script:
1. Go to the webpage with the video, and open Developer Tools > Network tab. Check if there are some files with size more than 1M, and more files keep coming at the same speed you're playing the video.
2. Locate the Google Chrome cache folder, sort the files by modification time, and see if new files keep coming consistently with Chrome Network file addition.
3. Open the first several files using any media player, see if it could be played, and if it is a slice of the video you want.
4. If they could be played and are in the correct sequence, you could use this script to download the video.

## Prerequisites
- OS: Windows 10 - Google Chrome cache location depends on Windows version, and Windows 10 is the only one I have to test this out
- Browser: Google Chrome - I'm using version 81.0
- Python 2.7 - I know it's out of date, but again, this is the only one I have dating back to 4 years ago on my desktop
- Basic knowledge of Windows PowerShell - No need for a GUI, this only works on very few selected platforms, so not going into the trouble of creating an all-purpose solution.

## Installation & Configuration
1. Either Git Clone this repo onto local, or just create a new folder anywhere, separately go to each python file and copy & paste.
2. Find out the Google Chrome cache folder on your platform, open `cache_watch.py`, and update line 7, `path_to_watch` variable, most likely only change the `<user-name>` section.

Open PowerShell, navigate to the local folder of these two files and run `python cache_watch.py`.
Then open Google Chrome, and go to some random webpage, you should be able to see some output on the terminal. Sample output:
```
Added f_000001
Copy from Cache\f_000001 to local_folder\orig\f_000001
```
Note the f_000001 here is a Chrome selected file identifier.

If output text looks like this format, it means the program is capable of watching over browser cache and we're ready to move on to usage.
Stop the watch for now with one or two `Ctrl + C`.

## Usage 
1. Open/Refresh the webpage with the video you would like to download.
2. Clear browser cache - either through Developer Tools > Network and right-click on resources, or through Settings.
3. Start watching on the cache with PowerShell > `python cache_watch.py`
4. Click play, and wait until the video is finished. <span style="color:red">Do not use Chrome browser to open any other website during this time, as it will change what's cached.</span>
5. If the video player supports accelerate, feel free to do so, it won't affect the downloaded video speed.
6. After the video has finished playing, interrupt watching on the cache, again with one or two `Ctrl + C`. <span style="color: red">Do not use Chrom browser to open any other website before interrupting watch.</span>
7. Start the combination of video files with `python file_compress.py`.
8. Follow the prompt to enter the new video file name, and wait for it to finish compressing, a 400M video would take about 30~50 seconds on my desktop.
9. The new video file would be in the same folder as the two python scripts.

## Known Issues
- Only support the most naive slicing of videos.
- Do not support compressing of more than 10^6 chunks of files.

## Contribution
Any contribution appreciated!

## License
This project is licensed under the terms of the MIT license.