# Port Scanner

A simple yet effective command-line-based Port Scanner built in Python. This tool allows users to scan a target host to identify open ports in the range of 0–1023. The script is beginner-friendly and demonstrates fundamental concepts of network programming and socket communication in Python.

## Features

- **User-Friendly Interface:** Displays a banner using the `pyfiglet` library.
- **Target Scanning:** Accepts a target IP address and scans ports from 0 to 1023.
- **Real-Time Updates:** Shows scanning progress and lists open ports in real-time.
- **Error Handling:** Handles exceptions gracefully for scenarios like invalid IP, hostname resolution issues, or user interruptions.
- **Timestamp Tracking:** Logs the start and end time of the scanning process for time tracking.

## Requirements

- Python 3.8+
- Libraries:
  - `pyfiglet`
  - `socket`

Install the required dependencies using:
```bash
pip install pyfiglet
```
## Usage
1. Clone or download this repository.
```bash
git clone https://github.com/d3vda5/port-scanner.git
```
2. Open a terminal and navigate to the folder containing `Port_Scanner.py`.
```bash
cd port-scanner
```
3. Run the script with the following command:
```bash
python Port_Scanner.py <target_IP>
```
Replace `<target_IP>` with the IP address of the target you want to scan.
## Example
```bash
python Port_Scanner.py 192.168.1.1
```
## Output:
```bash
PORT SCANNER
--------------------------------------------------
Scanning Target: 192.168.1.1
Scanning started at: 2025-01-17 14:00:00
--------------------------------------------------
Port 80 is open
Port 443 is open
...
--------------------------------------------------
Scanning ended at: 2025-01-17 14:00:15
Total Scanning time: 15 seconds
```
## File Details

`Port_Scanner.py`: The main script for scanning ports on the target host.
## How It Works

1. The script accepts a target IP address as a command-line argument.
2. Resolves the hostname to ensure it's valid.
3. Iterates through ports 0–1023, attempting to establish a connection using the `socket` library.
4. If a connection is successful, the port is marked as open.
5. Displays the open ports and the total scanning time at the end.
## Error Handling
1. **Invalid Arguments**: Prompts the user if the IP address is missing.
2. **Hostname Resolution Error**: Notifies if the hostname cannot be resolved.
3. **Socket Error**: Informs if the server is unresponsive.
4. **Keyboard Interrupt**: Safely exits the program if interrupted by the user.
## Notes
* The script currently scans only well-known ports (0–1023). For a broader scan, adjust the `range()` function in the code.
* This scanner is meant for educational and authorized use only. Unauthorized scanning of systems is illegal and unethical.
## Future Improvements
* Add support for custom port ranges.
* Enable multi-threaded scanning for faster results.
* Enhance the output format for better readability.
* Include advanced features like service detection and protocol analysis.

## Disclaimer:
This tool is intended for educational purposes only. Ensure you have proper authorization before scanning any target.
