.dat to .sct2 File Converter
============================

Written by Ian Cowan

Executable for Windows Only

Installation and Usage
----------------------

1. Clone the repository or download the executable from GitHub.

2. Place the file in the folder with the executable and name it something simple to remember (i.e. "dat_file.dat").

3. Run the executable. The command line should open.

4. Type in the DAT filename exactly (including extension).
    - `Filename: dat_file.dat`

5. If the file exists in the folder, a file called "dat_to_sct2_output.txt" will be created.
    - Please note that if the file doesn't exist, the converter will close without an error but the file will not be created.

Troubleshooting
---------------
Please note that this utility is meant to be FUNCTIONAL and not user friendly. If the converter is not outputting the expected file:
- Make sure the file is within the same folder as the exe file.
- Make sure you are typing the filename exactly correct.
- The executable will only work on Windows (not Mac or Linux). If you would like to run on Mac or Linux, you must use the base python file, have Python 3.7 installed on your computer, and run in the command line:
    - `python dat_to_sct2.py`

Please note that the converter may break and not return errors due to the nature of this project.

Open Source
-----------
This program is open source and was written in Python 3.7. Feel free to make any changes but please do not distribute for compensation.
