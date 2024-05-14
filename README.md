![loghog](https://github.com/unixbox-net/loghog/assets/104218206/351322c5-0962-427c-bb4c-2eb3ac3244c1)

# Install Notes.

  The installer automatically builds both an .rpm package and binary. It will attempt to install
  via DNF (aka) **ANY** version of Rhel, Fedora, CentOS, Alma, Rocky... It may work on Oracle, Scientific
  or Amazon Linux?. But in theory the applciation its self only uses standard posix so it should compile
  and run on all UNIX/UNIX-like and GNU-Linux systems.  I test on Rocky 8.9

  cmd:
  ```bash
  sudo su -
  curl -sL https://github.com/unixbox-net/lh/raw/main/install.sh | sudo bash
  lh
  ```

  Output files can be found
  ```bash
  ~/lh/rpmbuild/BUILD/lh-1.0.0/lh (compiled binary)
  ~/lh/rpmbuild/RPMS/x86_64/lh-1.0.0-1.el8.x86_64.rpm (package)
  etc
  ```
   
  Depedicies
  ```bash
  json-c readline
  ```

## Purpose

Identify system issues as quickly as possible

## "modes"

**TAIL**  *Default*
Automatically stitches logs together by timestamp, enabling real-time event monitoring. This mode makes 
it easy to follow and investigate incidents like authentication failures, permission denials, and SQL 
injections. **Press `CTRL+C`** to quit.

**LESS**  *Secondary*
Buffers are sent directly to **less** for further editing and in-depth review, searches, and complex log 
analysis.  
**Press `h` for help** or **`q` to quit to menu**.

**Remote Operation**
Changing paths also works on network shares, allowing for both local and remote operation

IE:
changeing the loging path to a remote location, or many remote locations can be combined with simple powerful regular expressions



## Other key features include:
  
**Regex Search**: Allows powerful searches across all logs using regular expressions, making it simple to detect 
patterns like IP addresses, error messages, and unauthorized access attempts.
**Network Protocol Filter**: Filters logs by protocol (HTTP, FTP, SSH, etc.) to quickly identify network-related 
issues.
**Error Filtering**: Isolates error-related events like failures, critical warnings, and socket timeouts for faster 
troubleshooting.
**Custom Log Paths**: Lets users specify custom log paths (local or remote) for precise, targeted searches.
**Export to JSON**: Exports search results to JSON format for further analysis or sharing with others.
**Live and Less Modes**: Enables real-time log monitoring or in-depth review through the less pager.
**Ultra Small** around 21,815 bytes (21kb) its about the same size as a BLANK word document.

Whether you're a system administrator, developer, or security professional, LogHOG offers a comprehensive suite of 
tools for efficient log analysis and bug hunting. Its simplicity, speed, and robustness make it an indispensable 
forensics tool.

## Known Issues

RegEx Searches do not display output, however the file is still written to disk
