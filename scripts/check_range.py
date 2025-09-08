#!/usr/bin/env python3
"""
Number Range Validation Script
==============================

This script performs precise numerical range checking to avoid LLM calculation errors.

Usage:
    python3 scripts/check_range.py [value] [min] [max] [value] [min] [max] ...

Examples:
    # Health metrics
    python3 scripts/check_range.py 185 125 200 92 70 100 85 80 120
    
    # Budget categories  
    python3 scripts/check_range.py 650 500 700 250 200 300
    
    # Financial targets
    python3 scripts/check_range.py 15.5 10.0 20.0 8.2 5.0 15.0
"""

import sys

def check_range(value, min_val, max_val):
    """Check if value is within the specified range (inclusive)"""
    return min_val <= value <= max_val

def format_result(value, min_val, max_val, in_range):
    """Format the result for display"""
    status = "✅ In range" if in_range else "❌ Out of range"
    return f"{value:8.1f} | [{min_val:6.1f} - {max_val:7.1f}] | {status}"

def main():
    """Main function to process command line arguments"""
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Usage: python3 check_range.py [value] [min] [max] [value] [min] [max] ...")
        print("Example: python3 check_range.py 185 125 200 92 70 100")
        return
    
    if len(args) % 3 != 0:
        print("❌ Error: Arguments must be in groups of 3 (value, min, max)")
        print("Example: python3 check_range.py 185 125 200 92 70 100")
        return
    
    print("🔍 Range Check:")
    print("=" * 50)
    
    # Process arguments in groups of 3
    for i in range(0, len(args), 3):
        try:
            value = float(args[i])
            min_val = float(args[i + 1])
            max_val = float(args[i + 2])
            
            in_range = check_range(value, min_val, max_val)
            result = format_result(value, min_val, max_val, in_range)
            print(result)
            
        except ValueError as e:
            print(f"❌ Error processing arguments {i//3 + 1}: {e}")
            return
        except IndexError:
            print("❌ Error: Incomplete argument group")
            return
    
    print("=" * 50)

if __name__ == "__main__":
    main()
