#!/usr/bin/env python3
"""
Batch scanning example for ZeroSploit
Shows how to scan multiple targets
"""

import sys
import os
import json
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zerosploit import ZeroSploit

def batch_scan_example():
    """Example of scanning multiple targets"""
    print("=== ZeroSploit Batch Scanning Example ===")
    
    # List of targets (use only authorized targets)
    targets = [
        "127.0.0.1",
        "localhost",
        # Add your authorized targets here
    ]
    
    results = []
    
    for target in targets:
        print(f"\n--- Scanning {target} ---")
        
        scanner = ZeroSploit()
        validated_target = scanner.validate_target(target)
        
        if validated_target:
            scanner.target = validated_target
            
            # Perform basic scan
            scanner.basic_port_scan()
            scanner.vulnerability_lookup()
            
            # Collect results
            target_results = {
                "target": validated_target,
                "timestamp": datetime.now().isoformat(),
                "session_log": scanner.session_log
            }
            
            results.append(target_results)
            print(f"✓ Completed scan for {target}")
        else:
            print(f"✗ Invalid target: {target}")
    
    # Save batch results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"batch_scan_results_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Batch scan completed. Results saved to {filename}")
    print(f"  Total targets scanned: {len(results)}")

if __name__ == "__main__":
    try:
        batch_scan_example()
    except KeyboardInterrupt:
        print("\nBatch scan interrupted by user")
    except Exception as e:
        print(f"Error in batch scan: {e}")
        sys.exit(1)