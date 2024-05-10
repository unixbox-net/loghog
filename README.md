![loghog](https://github.com/unixbox-net/loghog/assets/104218206/351322c5-0962-427c-bb4c-2eb3ac3244c1)

# How to Install
  dnf/yum rhel8 systems
  ```bash
  git clone https://github.com/unixbox-net/loghog.git && cd loghog/ && dnf install -y json-c readline loghog-1.0.0-1.el8.x86_64.rpm
  ```
  or compile and run with clang
  ```bash
  clang loghog.c -o loghog -lreadline -ljson-c
  ```
  Depedicies
  ```bash
  json-c readline
  ```

## Purpose
LogHOG - No-Nonsense Digital Forensics

It's built for SPEED Offering FAST, comprehensive log analysis, searching, bug hunting, system diagnostics, and digital forensics tools. Designed with a no-nonsense approach, it simplifies log analysis so that anyone can effectively troubleshoot most issues, quickly and efficiently.

***TAIL MODE:**  
Automatically stitches logs together by timestamp, enabling real-time event monitoring. This mode makes it easy to follow and investigate incidents like authentication failures, permission denials, and SQL injections. **Press `CTRL+C`** to quit.

***LESS MODE:**  
Buffers from **TAIL MODE** are sent directly to **less** a powerful text-editing tool that allows for in-depth review, searches, and real-time log analysis.  
**Press `h` for help** or **`q` to quit**.

## Other key features include:

  **Tail Mode**: Automatically stitches logs together by timestamp, enabling real-time event monitoring. This mode makes it easy to follow and investigate incidents like authentication failures, permission denials, and SQL injections.
  **Regex Search**: Allows powerful searches across all logs using regular expressions, making it simple to detect patterns like IP addresses, error messages, and unauthorized access attempts.

**Network Protocol Filter**: Filters logs by protocol (HTTP, FTP, SSH, etc.) to quickly identify network-related issues.
**Error Filtering**: Isolates error-related events like failures, critical warnings, and socket timeouts for faster troubleshooting.
**Custom Log Paths**: Lets users specify custom log paths for precise, targeted searches.
**Export to JSON**: Exports search results to JSON format for further analysis or sharing with others.
**Live and Less Modes**: Enables real-time log monitoring or in-depth review through the less pager.

Whether you're a system administrator, developer, or security professional, LogHOG offers a comprehensive suite of tools for efficient log analysis and bug hunting. Its simplicity, speed, and robustness make it an indispensable tool for system diagnostics and digital forensics.  and I'm lazzy.
