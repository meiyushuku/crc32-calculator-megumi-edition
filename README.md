# crc32_calculator_megumi_edition

This is a tool that helps users know the CRC-32 value of  files by batch in current directory or walking the tree.
Users can also add custom file extension exclusions and choose create the report file or not.

Execution modes below are provided:

Scan modes

I. Current directory only
II. Tree traversal (including all sub folders)

Output modes

1. Vanish mode: the calculation result of CRC-32 are only displayed on screen.
2. Text file: create report as text file with readability.
3. CSV file: create report as CSV file for Microsoft Excel.
4. Both: create the text and CSV file both.

The folder named crc_report will be created (if none) in current directory and reports will be saved to there.
The report file will be named with system time converted to UTC+0 in ISO 8601 format.

Files and folders below have been excluded by default:

File: desktop.ini, Thumbs.db, .gitattributes, .gitignore
Folder: .git, crc_report
Extension: .py

You can also add custom file extension exclusions with a command.

Command list:

cal -v: Scan with mode I and output with mode 1.
cal -t: Scan with mode I and output with mode 2.
cal -c: Scan with mode I and output with mode 3.
cal -b: Scan with mode I and output with mode 4.
cal --walk-v: Scan with mode II and output with mode 1.
cal --walk-t: Scan with mode II and output with mode 2.
cal --walk-c: Scan with mode II and output with mode 3.
cal --walk-b: Scan with mode II and output with mode 4.
ex -add: Add custom file extension exclusions.
ex -rm: Remove custom file extension exclusions.
ex -show: Show custom file extension exclusions.

Developed by Meiyu Shuku https://github.com/meiyushuku
