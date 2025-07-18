#!/usr/bin/env python3
"""
ZeroSploit - Vulnerability Intelligence CLI Tool
Author: Security Research Team
Version: 1.0.0
License: MIT

LEGAL DISCLAIMER:
This tool is intended for authorized security testing only.
Only use this tool on systems you own or have explicit permission to test.
Unauthorized scanning or testing of systems is illegal and unethical.
The authors are not responsible for any misuse of this tool.
"""

import sys
import os
import re
import json
import time
import socket
import argparse
import urllib.parse
from datetime import datetime

try:
    import requests
    from colorama import Fore, Back, Style, init
    import nmap
except ImportError as e:
    print(f"Error: Missing required dependencies. Please install: {e}")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class ZeroSploit:
    """Main ZeroSploit CLI application class"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.target = None
        self.nm = nmap.PortScanner()
        self.session_log = []
        
    def display_banner(self):
        """Display the ZeroSploit banner"""
        banner = f"""
{Fore.CYAN}╔════════════════════════════════════╗
{Fore.CYAN}║{Fore.RED}         ZeroSploit v{self.version}           {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}    Vulnerability Intelligence      {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}           CLI Tool                 {Fore.CYAN}║
{Fore.CYAN}╠════════════════════════════════════╣
{Fore.CYAN}║ Target: {Fore.GREEN}{self.target:<23} {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}⚠️  ETHICAL USE ONLY - AUTHORIZED TESTING REQUIRED{Style.RESET_ALL}
"""
        print(banner)
    
    def display_menu(self):
        """Display the main menu options"""
        menu = f"""
{Fore.CYAN}Select an operation to perform:

{Fore.WHITE}[1] {Fore.GREEN}Port Scan
{Fore.WHITE}[2] {Fore.GREEN}Vulnerability Lookup (based on services)
{Fore.WHITE}[3] {Fore.GREEN}CVE Suggestion
{Fore.WHITE}[4] {Fore.GREEN}Payload Suggestion
{Fore.WHITE}[5] {Fore.GREEN}Exploitation Tips
{Fore.WHITE}[0] {Fore.RED}Exit{Style.RESET_ALL}
"""
        print(menu)
    
    def get_user_input(self, prompt):
        """Get user input with colored prompt"""
        return input(f"{Fore.CYAN}>> {prompt}: {Style.RESET_ALL}")
    
    def log_activity(self, action, details):
        """Log activities for session tracking"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.session_log.append({
            "timestamp": timestamp,
            "action": action,
            "details": details
        })
    
    def validate_target(self, target):
        """Validate and normalize target input"""
        if not target:
            return False
        
        # Remove protocol if present
        target = re.sub(r'^https?://', '', target)
        
        # Validate IP address
        ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        if re.match(ip_pattern, target):
            return target
        
        # Validate domain name
        domain_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-_.]*[a-zA-Z0-9]$'
        if re.match(domain_pattern, target):
            return target
        
        return False
    
    def port_scan(self):
        """Perform port scanning on the target"""
        if not self.target:
            print(f"{Fore.RED}[!] No target specified{Style.RESET_ALL}")
            return
        
        print(f"{Fore.YELLOW}[*] Starting port scan for {self.target}...{Style.RESET_ALL}")
        
        try:
            # Common ports to scan
            common_ports = "21,22,23,25,53,80,110,111,135,139,143,443,993,995,1723,3306,3389,5432,5900,8080,8443"
            
            # Perform the scan
            self.nm.scan(self.target, common_ports, arguments='-sV -sC')
            
            open_ports = []
            
            for host in self.nm.all_hosts():
                print(f"{Fore.GREEN}[+] Host: {host} ({self.nm[host].hostname()}){Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] State: {self.nm[host].state()}{Style.RESET_ALL}")
                
                for proto in self.nm[host].all_protocols():
                    ports = self.nm[host][proto].keys()
                    
                    for port in ports:
                        state = self.nm[host][proto][port]['state']
                        if state == 'open':
                            service = self.nm[host][proto][port]['name']
                            version = self.nm[host][proto][port].get('version', 'unknown')
                            
                            print(f"{Fore.GREEN}[+] {port}/{proto} - {service} {version}{Style.RESET_ALL}")
                            
                            open_ports.append({
                                'port': port,
                                'protocol': proto,
                                'service': service,
                                'version': version
                            })
            
            if not open_ports:
                print(f"{Fore.YELLOW}[!] No open ports found{Style.RESET_ALL}")
            
            self.log_activity("port_scan", {"target": self.target, "open_ports": open_ports})
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error during port scan: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Falling back to basic socket scan...{Style.RESET_ALL}")
            self.basic_port_scan()
    
    def basic_port_scan(self):
        """Basic port scanning using socket (fallback method)"""
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080, 8443]
        
        print(f"{Fore.YELLOW}[*] Performing basic port scan on {self.target}...{Style.RESET_ALL}")
        
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                sock.close()
                
                if result == 0:
                    print(f"{Fore.GREEN}[+] Port {port}/tcp - Open{Style.RESET_ALL}")
                    open_ports.append(port)
                    
            except socket.gaierror:
                print(f"{Fore.RED}[!] Could not resolve hostname: {self.target}{Style.RESET_ALL}")
                break
            except Exception as e:
                continue
        
        if not open_ports:
            print(f"{Fore.YELLOW}[!] No open ports found{Style.RESET_ALL}")
        
        self.log_activity("basic_port_scan", {"target": self.target, "open_ports": open_ports})
    
    def vulnerability_lookup(self):
        """Look up vulnerabilities for discovered services"""
        print(f"{Fore.YELLOW}[*] Performing vulnerability lookup for {self.target}...{Style.RESET_ALL}")
        
        # This would typically query CVE databases
        # For demo purposes, we'll simulate some common vulnerabilities
        
        common_vulns = [
            {"service": "SSH", "port": 22, "cve": "CVE-2020-15778", "severity": "High", "description": "OpenSSH scp vulnerability"},
            {"service": "HTTP", "port": 80, "cve": "CVE-2021-44228", "severity": "Critical", "description": "Log4j Remote Code Execution"},
            {"service": "HTTPS", "port": 443, "cve": "CVE-2014-0160", "severity": "High", "description": "OpenSSL Heartbleed"},
            {"service": "FTP", "port": 21, "cve": "CVE-2010-4221", "severity": "Medium", "description": "ProFTPD Directory Traversal"},
        ]
        
        print(f"{Fore.GREEN}[+] Common vulnerabilities to check:{Style.RESET_ALL}")
        for vuln in common_vulns:
            print(f"{Fore.CYAN}    - {vuln['service']} ({vuln['port']}/tcp): {vuln['cve']} - {vuln['severity']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}      Description: {vuln['description']}{Style.RESET_ALL}")
        
        self.log_activity("vulnerability_lookup", {"target": self.target, "vulns_checked": len(common_vulns)})
    
    def cve_suggestion(self):
        """Suggest CVEs based on target analysis"""
        print(f"{Fore.YELLOW}[*] Generating CVE suggestions for {self.target}...{Style.RESET_ALL}")
        
        # Simulate CVE database lookup
        cve_suggestions = [
            {
                "cve": "CVE-2023-4966",
                "cvss": "9.4",
                "description": "NetScaler Buffer Overflow",
                "affected": "Citrix NetScaler ADC and Gateway",
                "recommendation": "Update to latest version"
            },
            {
                "cve": "CVE-2023-34362",
                "cvss": "9.8",
                "description": "MOVEit SQL Injection",
                "affected": "Progress MOVEit Transfer",
                "recommendation": "Apply security patches immediately"
            },
            {
                "cve": "CVE-2023-28252",
                "cvss": "7.8",
                "description": "Windows Common Log File System Driver",
                "affected": "Microsoft Windows",
                "recommendation": "Install Windows updates"
            }
        ]
        
        print(f"{Fore.GREEN}[+] Recent high-impact CVEs to consider:{Style.RESET_ALL}")
        for cve in cve_suggestions:
            print(f"{Fore.RED}    {cve['cve']} (CVSS: {cve['cvss']}){Style.RESET_ALL}")
            print(f"{Fore.WHITE}    Description: {cve['description']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}    Affected: {cve['affected']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    Recommendation: {cve['recommendation']}{Style.RESET_ALL}")
            print()
        
        self.log_activity("cve_suggestion", {"target": self.target, "cves_suggested": len(cve_suggestions)})
    
    def payload_suggestion(self):
        """Suggest educational payloads for testing"""
        print(f"{Fore.YELLOW}[*] Educational payload suggestions for {self.target}...{Style.RESET_ALL}")
        print(f"{Fore.RED}[!] WARNING: These are for educational purposes only!{Style.RESET_ALL}")
        
        payloads = [
            {
                "category": "SQL Injection",
                "payload": "' OR '1'='1",
                "description": "Basic SQL injection test",
                "usage": "Test in login forms or URL parameters"
            },
            {
                "category": "XSS",
                "payload": "<script>alert('XSS')</script>",
                "description": "Basic XSS test payload",
                "usage": "Test in input fields and search boxes"
            },
            {
                "category": "Command Injection",
                "payload": "; ls -la",
                "description": "Basic command injection test",
                "usage": "Test in parameters that might execute system commands"
            },
            {
                "category": "Directory Traversal",
                "payload": "../../../etc/passwd",
                "description": "Path traversal test",
                "usage": "Test in file upload or path parameters"
            }
        ]
        
        print(f"{Fore.GREEN}[+] Educational test payloads:{Style.RESET_ALL}")
        for payload in payloads:
            print(f"{Fore.CYAN}    Category: {payload['category']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}    Payload: {payload['payload']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}    Description: {payload['description']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    Usage: {payload['usage']}{Style.RESET_ALL}")
            print()
        
        self.log_activity("payload_suggestion", {"target": self.target, "payloads_shown": len(payloads)})
    
    def exploitation_tips(self):
        """Provide educational exploitation tips"""
        print(f"{Fore.YELLOW}[*] Educational exploitation tips for {self.target}...{Style.RESET_ALL}")
        print(f"{Fore.RED}[!] REMEMBER: Only test on authorized systems!{Style.RESET_ALL}")
        
        tips = [
            {
                "phase": "Reconnaissance",
                "description": "Information gathering is crucial",
                "techniques": [
                    "Use nmap for port scanning",
                    "Enumerate services and versions",
                    "Check for default credentials",
                    "Look for exposed directories"
                ]
            },
            {
                "phase": "Vulnerability Assessment",
                "description": "Identify potential weaknesses",
                "techniques": [
                    "Run vulnerability scanners",
                    "Check CVE databases",
                    "Test for common vulnerabilities",
                    "Analyze error messages"
                ]
            },
            {
                "phase": "Exploitation",
                "description": "Test identified vulnerabilities",
                "techniques": [
                    "Use proof-of-concept exploits",
                    "Test with minimal impact",
                    "Document all findings",
                    "Maintain access responsibly"
                ]
            },
            {
                "phase": "Post-Exploitation",
                "description": "Assess impact and document",
                "techniques": [
                    "Determine scope of access",
                    "Document security impact",
                    "Prepare remediation advice",
                    "Follow responsible disclosure"
                ]
            }
        ]
        
        print(f"{Fore.GREEN}[+] Security testing methodology:{Style.RESET_ALL}")
        for tip in tips:
            print(f"{Fore.CYAN}    {tip['phase']}: {tip['description']}{Style.RESET_ALL}")
            for technique in tip['techniques']:
                print(f"{Fore.WHITE}      - {technique}{Style.RESET_ALL}")
            print()
        
        self.log_activity("exploitation_tips", {"target": self.target, "tips_shown": len(tips)})
    
    def save_session_log(self):
        """Save session log to file"""
        if not self.session_log:
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"zerosploit_session_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.session_log, f, indent=2)
            print(f"{Fore.GREEN}[+] Session log saved to {filename}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error saving session log: {e}{Style.RESET_ALL}")
    
    def run(self, target=None):
        """Main application loop"""
        print(f"{Fore.YELLOW}[*] Starting ZeroSploit - Vulnerability Intelligence CLI{Style.RESET_ALL}")
        
        if not target:
            target = self.get_user_input("Enter target URL or IP address")
        
        validated_target = self.validate_target(target)
        if not validated_target:
            print(f"{Fore.RED}[!] Invalid target: {target}{Style.RESET_ALL}")
            return
        
        self.target = validated_target
        self.log_activity("session_start", {"target": self.target})
        
        while True:
            self.display_banner()
            self.display_menu()
            
            choice = self.get_user_input("Enter your choice")
            
            if choice == '1':
                self.port_scan()
            elif choice == '2':
                self.vulnerability_lookup()
            elif choice == '3':
                self.cve_suggestion()
            elif choice == '4':
                self.payload_suggestion()
            elif choice == '5':
                self.exploitation_tips()
            elif choice == '0':
                print(f"{Fore.YELLOW}[*] Exiting ZeroSploit...{Style.RESET_ALL}")
                self.save_session_log()
                break
            else:
                print(f"{Fore.RED}[!] Invalid choice: {choice}{Style.RESET_ALL}")
            
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="ZeroSploit - Vulnerability Intelligence CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python zerosploit.py
  python zerosploit.py --target example.com
  python zerosploit.py --target 192.168.1.1

Legal Notice:
This tool is for authorized security testing only.
Only use on systems you own or have explicit permission to test.
        """
    )
    
    parser.add_argument(
        '--target', '-t',
        help='Target URL or IP address',
        type=str
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='ZeroSploit 1.0.0'
    )
    
    args = parser.parse_args()
    
    try:
        zerosploit = ZeroSploit()
        zerosploit.run(args.target)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[*] Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!] Unexpected error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()