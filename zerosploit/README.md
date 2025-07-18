# ZeroSploit - Vulnerability Intelligence CLI Tool

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)](https://www.linux.org/)

A comprehensive command-line interface tool for vulnerability assessment and penetration testing. ZeroSploit helps security professionals identify vulnerabilities, suggest payloads, and provide exploitation guidance for authorized security testing.

## ⚠️ Legal Disclaimer

**IMPORTANT: This tool is intended for authorized security testing only.**

- Only use this tool on systems you own or have explicit permission to test
- Unauthorized scanning or testing of systems is illegal and unethical
- The authors are not responsible for any misuse of this tool
- Always follow responsible disclosure practices
- Ensure you have proper authorization before conducting any security assessments

## 🎯 Features

- **Port Scanning**: Discover open ports and running services
- **Vulnerability Lookup**: Search for known vulnerabilities based on detected services
- **CVE Suggestions**: Get relevant CVE information for discovered services
- **Payload Suggestions**: Educational payload examples for testing
- **Exploitation Tips**: Guidance for security testing approaches
- **Interactive CLI**: User-friendly command-line interface with colorful output

## 📋 Requirements

- Python 3.7 or higher
- Linux operating system
- Network access for CVE lookups
- Optional: nmap (for advanced port scanning)

## 🚀 Installation

### Method 1: Clone and Install
```bash
git clone https://github.com/yourusername/zerosploit.git
cd zerosploit
pip install -r requirements.txt
chmod +x zerosploit.py
```

### Method 2: Direct Download
```bash
wget https://raw.githubusercontent.com/yourusername/zerosploit/main/zerosploit.py
chmod +x zerosploit.py
pip install requests colorama python-nmap
```

## 🔧 Usage

### Basic Usage
```bash
python zerosploit.py
```

### Command Line Options
```bash
python zerosploit.py --target example.com
python zerosploit.py --target 192.168.1.1
python zerosploit.py --help
```

### Interactive Mode
1. Run the tool: `python zerosploit.py`
2. Enter target URL or IP address
3. Select from the menu options:
   - [1] Port Scan
   - [2] Vulnerability Lookup
   - [3] CVE Suggestion
   - [4] Payload Suggestion
   - [5] Exploitation Tips
   - [0] Exit

## 📊 Example Output

```
╔════════════════════════════════════╗
║         ZeroSploit v1.0           ║
║    Vulnerability Intelligence      ║
║           CLI Tool                 ║
╠════════════════════════════════════╣
║ Target: https://example.com        ║
╚════════════════════════════════════╝

Select an operation to perform:
[1] Port Scan
[2] Vulnerability Lookup (based on services)
[3] CVE Suggestion
[4] Payload Suggestion
[5] Exploitation Tips
[0] Exit

>> Enter your choice: 1

[+] Starting port scan for example.com...
[+] Open ports found:
    - 80/tcp (HTTP)
    - 443/tcp (HTTPS)
    - 22/tcp (SSH)
```

## 🛡️ Ethical Guidelines

- **Authorization Required**: Always obtain proper authorization before testing
- **Responsible Disclosure**: Report vulnerabilities responsibly to vendors
- **Educational Purpose**: Use this tool to learn about security, not to cause harm
- **Legal Compliance**: Ensure your testing complies with local laws and regulations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [CVE Database](https://cve.mitre.org/)
- [National Vulnerability Database](https://nvd.nist.gov/)
- [Exploit Database](https://www.exploit-db.com/)

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Wiki](https://github.com/yourusername/zerosploit/wiki) for documentation
- Review the [FAQ](https://github.com/yourusername/zerosploit/blob/main/FAQ.md)

## 🔄 Changelog

### v1.0.0
- Initial release
- Port scanning functionality
- CVE lookup integration
- Interactive CLI interface
- Educational payload suggestions

---

**Remember: With great power comes great responsibility. Use this tool ethically and legally.**