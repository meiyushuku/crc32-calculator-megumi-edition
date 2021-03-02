<h1>crc32-calculator-megumi-edition</h1>
<img src="https://i.imgur.com/XEB6vDQ.png">
<br>
<img src="https://i.imgur.com/Zuwyeao.png">
<br>
This is a tool that helps users know the CRC-32 value of files by batch from current directory or through a directory tree.
<br>
Users can also add custom file extension exclusions and choose create the report file or not.
<br>
<br>
Execution modes below are provided:
<br>
<br>
Scan modes
<br>
I. Current directory only
<br>
II. Tree traversal (including all sub folders)
<br>
<br>
Output modes
<br>
1. Vanish mode: the calculation result of CRC-32 are only displayed on screen.
<br>
2. Text file: create report as text file with readability.
<br>
3. CSV file: create report as CSV file for Microsoft Excel.
<br>
4. Both: create the text and CSV file both.
<br>
<br>
The folder named crc_report will be created (if none) in current directory and reports will be saved to there.
<br>
The report file will be named with system time converted to UTC+0 in ISO 8601 format.
<br>
<br>
Files and folders below have been excluded by default:
<br>
<br>
File: desktop.ini, Thumbs.db, .gitattributes, .gitignore, README.md
<br>
Folder: .git, crc_report
<br>
Extension: .py
<br>
<br>
Users can also add custom file extension exclusions with a command.
<br>
<br>
Command list:
<br>
<br>
cal -v: Scan with mode I and output with mode 1.
<br>
cal -t: Scan with mode I and output with mode 2.
<br>
cal -c: Scan with mode I and output with mode 3.
<br>
cal -b: Scan with mode I and output with mode 4.
<br>
cal --walk-v: Scan with mode II and output with mode 1.
<br>
cal --walk-t: Scan with mode II and output with mode 2.
<br>
cal --walk-c: Scan with mode II and output with mode 3.
<br>
cal --walk-b: Scan with mode II and output with mode 4.
<br>
ex -add: Add custom file extension exclusions.
<br>
ex -rm: Remove custom file extension exclusions.
<br>
ex -show: Show custom file extension exclusions.
<br>
<br>
Developed by Meiyu Shuku https://github.com/meiyushuku
