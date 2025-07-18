# ZeroSploit Documentation

## Table of Contents
1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Features](#features)
4. [Configuration](#configuration)
5. [Advanced Usage](#advanced-usage)
6. [API Reference](#api-reference)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
- Python 3.7 or higher
- Linux operating system
- Network access for vulnerability lookups

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Optional: Install nmap
For enhanced port scanning capabilities:
```bash
# Ubuntu/Debian
sudo apt-get install nmap

# CentOS/RHEL
sudo yum install nmap

# Arch Linux
sudo pacman -S nmap
```

## Basic Usage

### Interactive Mode
```bash
python zerosploit.py
```

### Command Line Mode
```bash
python zerosploit.py --target example.com
python zerosploit.py --target 192.168.1.1
```

### Help
```bash
python zerosploit.py --help
```

## Features

### 1. Port Scanning
- Discovers open ports on target systems
- Uses nmap for advanced scanning (if available)
- Falls back to basic socket scanning
- Scans common ports by default

### 2. Vulnerability Lookup
- Identifies common vulnerabilities for discovered services
- Provides CVE references
- Shows severity ratings
- Suggests remediation steps

### 3. CVE Suggestions
- Shows recent high-impact CVEs
- Provides CVSS scores
- Includes affected systems information
- Offers remediation recommendations

### 4. Payload Suggestions
- Educational testing payloads
- Common vulnerability categories
- Safe testing examples
- Usage guidelines

### 5. Exploitation Tips
- Security testing methodology
- Best practices for authorized testing
- Responsible disclosure guidance
- Post-exploitation considerations

## Configuration

### Target Validation
ZeroSploit automatically validates and normalizes targets:
- IP addresses (e.g., 192.168.1.1)
- Domain names (e.g., example.com)
- URLs (protocol stripped automatically)

### Session Logging
- Automatic session logging
- JSON format output
- Timestamped activities
- Exportable results

## Advanced Usage

### Programmatic Usage
```python
from zerosploit import ZeroSploit

scanner = ZeroSploit()
scanner.target = "example.com"
scanner.port_scan()
scanner.vulnerability_lookup()
```

### Batch Processing
See `examples/batch_scan.py` for multi-target scanning.

### Custom Port Ranges
Modify the `common_ports` variable in the source code to scan specific ports.

## API Reference

### ZeroSploit Class

#### Methods

##### `__init__()`
Initialize a new ZeroSploit instance.

##### `validate_target(target)`
Validate and normalize a target string.
- **Parameters**: `target` (str) - Target URL or IP
- **Returns**: Normalized target string or False if invalid

##### `port_scan()`
Perform port scanning on the current target.

##### `basic_port_scan()`
Perform basic socket-based port scanning (fallback method).

##### `vulnerability_lookup()`
Look up vulnerabilities for discovered services.

##### `cve_suggestion()`
Suggest relevant CVEs for the target.

##### `payload_suggestion()`
Show educational testing payloads.

##### `exploitation_tips()`
Provide security testing methodology tips.

##### `log_activity(action, details)`
Log an activity to the session log.
- **Parameters**: 
  - `action` (str) - Action description
  - `details` (dict) - Activity details

##### `run(target=None)`
Main application loop.
- **Parameters**: `target` (str, optional) - Target to scan

## Examples

### Basic Scanning
```python
scanner = ZeroSploit()
scanner.run("example.com")
```

### Target Validation
```python
scanner = ZeroSploit()
valid_target = scanner.validate_target("http://example.com")
if valid_target:
    scanner.target = valid_target
    scanner.port_scan()
```

### Session Logging
```python
scanner = ZeroSploit()
scanner.log_activity("custom_action", {"key": "value"})
print(scanner.session_log)
```

## Troubleshooting

### Common Issues

#### "Command not found" errors
- Ensure Python 3.7+ is installed
- Check that script is executable: `chmod +x zerosploit.py`

#### Nmap scan failures
- Install nmap: `sudo apt-get install nmap`
- Check network connectivity
- Verify firewall settings
- Run with elevated privileges if needed

#### Permission errors
- Use `sudo` for network operations requiring privileges
- Check file permissions
- Verify target accessibility

#### Slow scanning
- Network latency affects scan speed
- Consider reducing scan scope
- Check target responsiveness

### Getting Help

1. Check the FAQ: `docs/FAQ.md`
2. Review examples in `examples/`
3. Open an issue on GitHub
4. Check the project wiki

### Debug Mode

For verbose output, modify the source code to include debug statements or increase verbosity in the logging configuration.

## Security Considerations

### Ethical Use
- Only test systems you own or have permission to test
- Follow responsible disclosure practices
- Respect rate limits and system resources
- Document all testing activities

### Legal Compliance
- Ensure testing is authorized
- Comply with local laws and regulations
- Maintain proper documentation
- Follow organizational policies

### Best Practices
- Start with minimal impact testing
- Gradually increase testing scope
- Monitor system resources
- Clean up after testing
- Maintain confidentiality of findings

## Contributing

### Development Setup
```bash
git clone https://github.com/yourusername/zerosploit.git
cd zerosploit
pip install -r requirements.txt
python -m pytest tests/
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include type hints where helpful

### Testing
- Add tests for new features
- Ensure backward compatibility
- Test on multiple Python versions
- Include integration tests

### Documentation
- Update README.md for new features
- Add examples for complex functionality
- Update API reference
- Include troubleshooting steps