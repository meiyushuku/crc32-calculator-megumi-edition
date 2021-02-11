This is a tool that helps users know the CRC-32 value of  files by batch in current directory or walking the tree. Users can also add custom file extension exclusions and choose create the report file or not.

Execution modes below are provided:

Scan modes

1. Current directory only
2. Tree traversal (including all sub folders)

Output modes

1. Vanish mode: the calculation result of CRC-32 are only displayed on screen.
2. Text file: create report as text file with readability.
3. CSV file: create report as CSV file for Microsoft Excel.
4. Both: create the text and CSV file both.

The folder named crc_report will be created (if none) in current directory and reports will be saved to there. The report file will be named with system time converted to UTC+0 in ISO 8601 format.

Files and folders below have been excluded by default:

1. File: desktop.ini, Thumbs.db, .gitattributes, .gitignore
2. Folder: .git, crc_report
3. Extension: .py

You can also add custom file extension exclusions with a command.

Command list:

1. cal -v: Scan with mode 1 and output with mode 1.
2. cal -t: Scan with mode 1 and output with mode 2.
3. cal -c: Scan with mode 1 and output with mode 3.
4. cal -b: Scan with mode 1 and output with mode 4.
5. cal --walk-v: Scan with mode 2 and output with mode 1.
6. cal --walk-t: Scan with mode 2 and output with mode 2.
7. cal --walk-c: Scan with mode 2 and output with mode 3.
8. cal --walk-b: Scan with mode 2 and output with mode 4.
9. ex -add: Add custom file extension exclusions.
10. ex -rm: Remove custom file extension exclusions.
11. ex -show: Show custom file extension exclusions.

Developed by Meiyu Shuku https://github.com/meiyushuku
