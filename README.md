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
