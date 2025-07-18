#!/usr/bin/env python3
"""
Test suite for ZeroSploit CLI Tool
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zerosploit import ZeroSploit

class TestZeroSploit(unittest.TestCase):
    """Test cases for ZeroSploit functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.zero_sploit = ZeroSploit()
    
    def test_validate_target_valid_ip(self):
        """Test target validation with valid IP address"""
        valid_ips = [
            "192.168.1.1",
            "10.0.0.1",
            "127.0.0.1",
            "8.8.8.8"
        ]
        
        for ip in valid_ips:
            result = self.zero_sploit.validate_target(ip)
            self.assertEqual(result, ip, f"Failed to validate IP: {ip}")
    
    def test_validate_target_valid_domain(self):
        """Test target validation with valid domain names"""
        valid_domains = [
            "example.com",
            "google.com",
            "localhost",
            "sub.domain.com"
        ]
        
        for domain in valid_domains:
            result = self.zero_sploit.validate_target(domain)
            self.assertEqual(result, domain, f"Failed to validate domain: {domain}")
    
    def test_validate_target_invalid(self):
        """Test target validation with invalid inputs"""
        invalid_targets = [
            "",
            "999.999.999.999",
            "invalid..domain",
            "special@characters",
            None
        ]
        
        for target in invalid_targets:
            result = self.zero_sploit.validate_target(target)
            self.assertFalse(result, f"Should have failed validation: {target}")
    
    def test_validate_target_with_protocol(self):
        """Test target validation with protocol prefixes"""
        targets_with_protocol = [
            ("http://example.com", "example.com"),
            ("https://google.com", "google.com"),
            ("http://192.168.1.1", "192.168.1.1")
        ]
        
        for input_target, expected in targets_with_protocol:
            result = self.zero_sploit.validate_target(input_target)
            self.assertEqual(result, expected, f"Failed to handle protocol: {input_target}")
    
    def test_log_activity(self):
        """Test activity logging functionality"""
        initial_count = len(self.zero_sploit.session_log)
        
        self.zero_sploit.log_activity("test_action", {"test": "data"})
        
        self.assertEqual(len(self.zero_sploit.session_log), initial_count + 1)
        
        last_log = self.zero_sploit.session_log[-1]
        self.assertEqual(last_log["action"], "test_action")
        self.assertEqual(last_log["details"]["test"], "data")
        self.assertIn("timestamp", last_log)

class TestZeroSploitIntegration(unittest.TestCase):
    """Integration tests for ZeroSploit"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.zero_sploit = ZeroSploit()
        # Use a safe test target
        self.zero_sploit.target = "127.0.0.1"
    
    def test_basic_port_scan(self):
        """Test basic port scanning functionality"""
        # This is a safe test that scans localhost
        try:
            self.zero_sploit.basic_port_scan()
            # If no exception is raised, test passes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Basic port scan failed: {e}")
    
    def test_vulnerability_lookup(self):
        """Test vulnerability lookup functionality"""
        try:
            self.zero_sploit.vulnerability_lookup()
            # If no exception is raised, test passes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Vulnerability lookup failed: {e}")
    
    def test_cve_suggestion(self):
        """Test CVE suggestion functionality"""
        try:
            self.zero_sploit.cve_suggestion()
            # If no exception is raised, test passes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"CVE suggestion failed: {e}")
    
    def test_payload_suggestion(self):
        """Test payload suggestion functionality"""
        try:
            self.zero_sploit.payload_suggestion()
            # If no exception is raised, test passes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Payload suggestion failed: {e}")
    
    def test_exploitation_tips(self):
        """Test exploitation tips functionality"""
        try:
            self.zero_sploit.exploitation_tips()
            # If no exception is raised, test passes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Exploitation tips failed: {e}")

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)