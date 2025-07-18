#!/usr/bin/env python3
"""
Example usage of ZeroSploit CLI Tool
This demonstrates how to use ZeroSploit programmatically
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zerosploit import ZeroSploit

def example_basic_usage():
    """Basic usage example"""
    print("=== ZeroSploit Basic Usage Example ===")
    
    # Create ZeroSploit instance
    scanner = ZeroSploit()
    
    # Set target
    target = "127.0.0.1"  # Safe test target
    validated_target = scanner.validate_target(target)
    
    if validated_target:
        print(f"Target validated: {validated_target}")
        scanner.target = validated_target
        
        # Perform basic port scan
        print("\nPerforming basic port scan...")
        scanner.basic_port_scan()
        
        # Show vulnerability suggestions
        print("\nShowing vulnerability suggestions...")
        scanner.vulnerability_lookup()
        
        # Show session log
        print(f"\nSession log entries: {len(scanner.session_log)}")
        for entry in scanner.session_log:
            print(f"  {entry['timestamp']}: {entry['action']}")
    else:
        print(f"Invalid target: {target}")

def example_target_validation():
    """Target validation examples"""
    print("\n=== Target Validation Examples ===")
    
    scanner = ZeroSploit()
    
    test_targets = [
        "192.168.1.1",
        "example.com",
        "http://google.com",
        "https://localhost",
        "invalid..domain",
        "999.999.999.999"
    ]
    
    for target in test_targets:
        result = scanner.validate_target(target)
        status = "✓ Valid" if result else "✗ Invalid"
        print(f"  {target:<20} -> {status}")
        if result and result != target:
            print(f"    Normalized to: {result}")

def example_educational_content():
    """Show educational content examples"""
    print("\n=== Educational Content Examples ===")
    
    scanner = ZeroSploit()
    scanner.target = "example.com"
    
    print("\nCVE Suggestions:")
    scanner.cve_suggestion()
    
    print("\nPayload Suggestions:")
    scanner.payload_suggestion()
    
    print("\nExploitation Tips:")
    scanner.exploitation_tips()

if __name__ == "__main__":
    try:
        example_basic_usage()
        example_target_validation()
        example_educational_content()
    except KeyboardInterrupt:
        print("\nExample interrupted by user")
    except Exception as e:
        print(f"Error in example: {e}")
        sys.exit(1)