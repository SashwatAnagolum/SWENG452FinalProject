
# Enhanced Alarm Clock: SWENG 452 Final Project

### Sashwat Anagolum

## Setup
Setting up the system is quite simple. First, check if you have Python installed on your system. You can do this by opening up a terminal shell and running the following command:

	python --version

If you do not, you will receive an error, and need to follow the instructions on the [official Python webpage](https://www.python.org/) to install Python on your device. The system has been tested with Python version 3.9.6, but later versions should work as well.


Once you have installed Python on you system, run the following command in a terminal window (if you have Git set up on your device) to download the source code files:

	git clone https://github.com/SashwatAnagolum/SWENG452FinalProject.git

If you do not have Git installed on your system, visit [this webpage](https://github.com/SashwatAnagolum/SWENG452FinalProject.git), a GitHub repository which contains all of the source code required to build the system. Download these files by clicking on the green 'Code' button above the list of files in the repository, and clicking the 'Download ZIP' option. Once the files have finished downloading, extract the contents of the ZIP file.

Open up a terminal shell, and enter the folder containing all of the source code files from the repository (the folder should be called ```SWENG452FinalProject``). Inside this folder, run the following command:

	pip install -r requirements.txt

This will install all of the required Python packages that the system makes use of.

## Execution
Once you have performed the necessary setup steps, you can begin execution of the program by running the following command in a terminal:

	python main.py