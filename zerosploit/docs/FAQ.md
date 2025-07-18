# Frequently Asked Questions

## General Questions

### Q: What is ZeroSploit?
A: ZeroSploit is a command-line vulnerability intelligence tool designed for authorized security testing. It helps security professionals identify vulnerabilities, suggest payloads, and provide exploitation guidance.

### Q: Is ZeroSploit legal to use?
A: ZeroSploit is legal when used for authorized security testing on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.

### Q: What operating systems does ZeroSploit support?
A: ZeroSploit is designed specifically for Linux environments. It may work on other Unix-like systems but is not tested or supported.

## Installation Questions

### Q: How do I install ZeroSploit?
A: You can install ZeroSploit by cloning the repository and installing dependencies:
```bash
git clone https://github.com/yourusername/zerosploit.git
cd zerosploit
pip install -r requirements.txt
chmod +x zerosploit.py
```

### Q: What dependencies does ZeroSploit require?
A: ZeroSploit requires Python 3.7+ and the following packages:
- requests
- colorama
- python-nmap

### Q: Do I need to install nmap separately?
A: For full functionality, yes. Install nmap using your package manager:
```bash
# Ubuntu/Debian
sudo apt-get install nmap

# CentOS/RHEL
sudo yum install nmap

# Arch Linux
sudo pacman -S nmap
```

## Usage Questions

### Q: How do I run ZeroSploit?
A: Simply run:
```bash
python zerosploit.py
```
Or specify a target directly:
```bash
python zerosploit.py --target example.com
```

### Q: What types of targets can I scan?
A: ZeroSploit accepts:
- IP addresses (e.g., 192.168.1.1)
- Domain names (e.g., example.com)
- URLs (protocol will be stripped)

### Q: Why is my port scan slow?
A: Port scanning speed depends on network conditions and target responsiveness. The tool scans common ports by default to balance speed and coverage.

### Q: Can I scan multiple targets at once?
A: Currently, ZeroSploit processes one target at a time. You can create scripts to iterate through multiple targets if needed.

## Technical Questions

### Q: How accurate are the vulnerability suggestions?
A: The vulnerability suggestions are based on common vulnerabilities and should be used as a starting point. Always verify findings with additional tools and manual testing.

### Q: Are the payloads in ZeroSploit real exploits?
A: The payloads are educational examples for testing purposes. They are not full exploits and should be used responsibly for authorized testing only.

### Q: How does ZeroSploit handle false positives?
A: Like any security tool, ZeroSploit may produce false positives. Always verify findings through manual testing and additional tools.

### Q: Can I save my scan results?
A: Yes, ZeroSploit automatically saves session logs in JSON format when you exit the program.

## Troubleshooting

### Q: I'm getting "command not found" errors
A: Make sure you have the required dependencies installed and the script is executable:
```bash
chmod +x zerosploit.py
pip install -r requirements.txt
```

### Q: Nmap scans are failing
A: This could be due to:
- Missing nmap installation
- Network connectivity issues
- Firewall blocking
- Insufficient permissions

The tool will fall back to basic socket scanning if nmap fails.

### Q: Why am I getting permission denied errors?
A: Some network scanning functions require elevated privileges. Try running with sudo:
```bash
sudo python zerosploit.py
```

## Ethical and Legal Questions

### Q: Can I use ZeroSploit on any website?
A: No. Only use ZeroSploit on systems you own or have explicit written permission to test. Unauthorized scanning is illegal.

### Q: What should I do if I find a vulnerability?
A: Follow responsible disclosure practices:
1. Do not exploit the vulnerability maliciously
2. Document your findings
3. Contact the system owner or vendor
4. Give them time to fix the issue
5. Only publish details after remediation

### Q: Is ZeroSploit suitable for production security assessments?
A: ZeroSploit is designed as an educational tool and starting point. For production assessments, use it alongside other professional security tools and manual testing.

## Contributing

### Q: How can I contribute to ZeroSploit?
A: Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Q: Can I request new features?
A: Yes! Please open an issue on GitHub with your feature request and use case.

## Support

### Q: Where can I get help?
A: You can:
- Check this FAQ
- Review the documentation
- Open an issue on GitHub
- Check the project wiki

### Q: How do I report bugs?
A: Please open an issue on GitHub with:
- Your operating system
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Any error messages