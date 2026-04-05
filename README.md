# IrisIp

Advanced Network Reconnaissance and Vulnerability Scanning Tool

<img width="1906" height="905" alt="Screenshot 2026-01-07 013434" src="https://github.com/user-attachments/assets/6a0345f4-c617-4097-a4db-563aaf7da9a3" />

IrisIp is a menu-driven cybersecurity automation tool designed to perform detailed network analysis and security assessments on target IP addresses or hosts.

Leveraging industry-standard tools such as Nmap and Nikto in the background, it accelerates the reconnaissance phase of penetration testing (pentest) operations.

By automating complex scanning commands that would otherwise be time-consuming to execute manually, it delivers rapid and reportable results to the user.

---

## Core Features

IrisIp is capable of performing the following analyses on target systems:

- **Port Scanning**
Detects open TCP/UDP ports on the target and identifies services running on those ports.

- **Service and Version Detection**
Analyzes running services (Apache, SSH, FTP, etc.) to determine vendor and version information.

- **Operating System Detection**
Uses TCP/IP stack analysis to identify the target's likely operating system (Linux, Windows, etc.).

- **Vulnerability Scanning**
Leverages Nmap Scripting Engine (NSE) and Nikto databases to identify known security vulnerabilities (CVE) and configuration misconfigurations.

- **Traceroute and Firewall Detection**
Maps the network path to the target and analyzes the presence of intermediate Firewalls / WAF (Web Application Firewall).

---

## Requirements

The following components must be installed on the system for the tool to function at full capacity:

- Python 3.x
- Nmap
- Nikto

---

## Installation

To clone the project to your local machine and set the required permissions:

- `git clone https://github.com/osmnabyram/IrisIp.git`
- `cd IrisIp`
- `chmod +x irisip.py`

---

## Usage

To launch the tool, execute the following command in the terminal:

- `python3 irisip.py`

Upon startup, the program presents a menu-driven interface containing scanning options.

---

## Example Usage Scenario

- Target IP address or hostname is entered
(Example: 192.168.1.10 or scanme.nmap.org)

- Desired scanning mode is selected from the menu
(Quick Scan, Comprehensive Scan, Vulnerability Analysis, etc.)

- Scan results are displayed on the terminal screen

---

## Legal Notice

IrisIp is developed exclusively for educational purposes and authorized penetration testing only.

Use against unauthorized systems is strictly prohibited and constitutes a legal offense.

The developer assumes no liability for any damages resulting from misuse of this tool.
