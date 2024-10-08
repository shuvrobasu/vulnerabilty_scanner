# Vulnerability Scanner for Domain

## Overview

The **Vulnerability Scanner for Domain** is a Python-based tool designed to scan directories on a specified domain to identify potential vulnerabilities. It checks both lowercase and uppercase directory names, supports HTTP and HTTPS, and saves the results to a file. The tool is primarily aimed at security researchers and developers who need to quickly identify possible security issues on a website.

## Features

- **Domain Validation:** Automatically checks if the provided domain is reachable over HTTP and HTTPS.
- **Directory Scanning:** Scans a predefined set of directories in both lowercase and uppercase.
- **Scanning from file with folder names:** Use the DEF.FOL file for some 40+ common folders.
- **Customizable Case Scanning:** Allows users to choose whether to scan lowercase, uppercase, or both cases.
- **Result Summary:** Provides a summary of found links and the option to view them.
- **File Saving:** Saves the results to a timestamped file with a detailed summary.

## Installation

To use this tool, you need to have Python 3 installed on your system. You can install the required Python packages using `pip`.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shuvrobasu/vulnerability_scanner.git
   cd vulnerability_scanner
# Usage

Run the Scanner:

bash 
python scanner.py

Follow the prompts:

<br>Enter the domain you wish to scan (e.g., example.com).
<br>Choose the case option (lowercase, uppercase, or both).
<br>Decide whether to view the found links.
<br>Choose whether to save the results to a file.

# Example

<br>Enter the domain name (e.g., example.com) [Blank to Exit]: example.com
<br>Do you want to scan with lower case, upper case, or both? (l/u/b): b
<br>Do you want to see the links? (y/n): y
<br>Do you want to save the found links to a file? (y/n): y

# Customization 
<br>You can customize the list of directories to scan by modifying the directories list in the scanner.py script OR modifying the included DEF.FOL file. You may also add your edit this file based on your needs. This file should be in the same folder as the script. If the file is not present, then the script will scan only a small set of folder, which you can edit in the script directly. 

# Contribution
<br>Contributions are welcome! If you have suggestions or improvements, please submit an issue or a pull request. Ensure that your code adheres to the existing style and includes appropriate tests and comments for me (and others).

# License
<br>This project is licensed under the MIT License - see the LICENSE file for details.

# Disclaimer
<br>[!] Legal disclaimer: Usage of this tool without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

# Contact
<br>For any questions or feedback, please contact:

<br>Developer: Shuvro Basu
<br>Email: shuvbasu24@gmail.com
<br>GitHub: shuvrobasu
