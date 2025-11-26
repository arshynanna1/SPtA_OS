# Laboratory Work #2 Report
## Bash Script: File Counter in /etc Directory

### Student: Arshyn Anna
### Date: November 2024

### Objective:
Create a bash script to count regular files in /etc directory, excluding directories and symbolic links.

### Script Code (count_files.sh):
\`\`\`bash
#!/bin/bash
find /etc -maxdepth 1 -type f | wc -l
\`\`\`

### What the script does:
- Uses find command to search /etc directory
- -maxdepth 1 - looks only in first level (not subdirectories)
- -type f - finds only regular files (no directories, no links)
- wc -l - counts the number of files found

### Development Process:
- Script created and tested locally on Ubuntu
- Initial testing showed consistent results in local environment
- Script designed to be portable across different Linux systems

### Verification:
- Script executed successfully on local system
- Output provided correct file count for local /etc directory
- Code followed bash scripting best practices

### File Location:
- count_files.sh in repository root
- File is executable
