# Vulnerability Scanner for Domain

## Overview

The **Vulnerability Scanner for Domain** is a Python-based tool designed to scan directories on a specified domain to identify potential vulnerabilities. It checks both lowercase and uppercase directory names, supports HTTP and HTTPS, and saves the results to a file. The tool is primarily aimed at security researchers and developers who need to quickly identify possible security issues on a website.

## Features

- **Domain Validation:** Automatically checks if the provided domain is reachable over HTTP and HTTPS.
- **Directory Scanning:** Scans a predefined set of directories in both lowercase and uppercase.
- **Customizable Case Scanning:** Allows users to choose whether to scan lowercase, uppercase, or both cases.
- **Result Summary:** Provides a summary of found links and the option to view them.
- **File Saving:** Saves the results to a timestamped file with a detailed summary.

## Installation

To use this tool, you need to have Python 3 installed on your system. You can install the required Python packages using `pip`.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shuvrobasu/vulnerability_scanner.git
   cd vulnerability_scanner
Usage
Run the Scanner:

bash
Copy code
python scanner.py
Follow the prompts:

Enter the domain you wish to scan (e.g., example.com).
Choose the case option (lowercase, uppercase, or both).
Decide whether to view the found links.
Choose whether to save the results to a file.
Example
bash
Copy code
Enter the domain name (e.g., example.com) [Blank to Exit]: example.com
Do you want to scan with lower case, upper case, or both? (l/u/b): b
Do you want to see the links? (y/n): y
Do you want to save the found links to a file? (y/n): y
Customization
You can customize the list of directories to scan by modifying the directories list in the scanner.py script. You can also adjust the terminal color codes and banner text as needed.

Contribution
Contributions are welcome! If you have suggestions or improvements, please submit an issue or a pull request. Ensure that your code adheres to the existing style and includes appropriate tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
[!] Legal disclaimer: Usage of this tool without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

Contact
For any questions or feedback, please contact:

Developer: Shuvro Basu
Email: shuvbasu24@gmail.com
GitHub: shuvrobasu
