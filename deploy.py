#!/usr/bin/env python3
"""
ESP32 MicroPython Deployment Script
Helps deploy Python files to ESP32 using mpremote
"""

import subprocess
import sys
import os
import time

# Configuration
ESP32_PORT = "/dev/tty.usbserial-0001"  # Update this if your port is different
BAUD_RATE = "115200"

def run_mpremote_command(cmd_args):
    """Run mpremote command with error handling"""
    try:
        cmd = ["mpremote", "connect", ESP32_PORT] + cmd_args
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Command succeeded")
            if result.stdout.strip():
                print(f"Output: {result.stdout}")
            return True
        else:
            print(f"❌ Command failed with return code {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Command timed out")
        return False
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return False

def check_connection():
    """Check if ESP32 is connected and responsive"""
    print("🔍 Checking ESP32 connection...")
    return run_mpremote_command(["ls"])

def deploy_files():
    """Deploy main.py and helper.py to ESP32"""
    files_to_deploy = ["main.py", "helper.py"]
    
    print("📁 Deploying files to ESP32...")
    
    for file in files_to_deploy:
        if not os.path.exists(file):
            print(f"❌ File {file} not found!")
            continue
            
        print(f"📤 Uploading {file}...")
        if run_mpremote_command(["cp", file, ":"]):
            print(f"✅ {file} uploaded successfully")
        else:
            print(f"❌ Failed to upload {file}")
            return False
    
    return True

def list_files():
    """List files on ESP32"""
    print("📋 Files on ESP32:")
    run_mpremote_command(["ls"])

def run_main():
    """Run main.py on ESP32"""
    print("🚀 Running main.py on ESP32...")
    run_mpremote_command(["run", "main.py"])

def reset_esp32():
    """Reset ESP32"""
    print("🔄 Resetting ESP32...")
    run_mpremote_command(["reset"])

def clean_esp32():
    """Remove test files from ESP32"""
    print("🧹 Cleaning ESP32...")
    files_to_remove = ["main.py", "helper.py", "test.ipynb", "test.code-workspace"]
    
    for file in files_to_remove:
        print(f"🗑️ Removing {file}...")
        run_mpremote_command(["rm", file])

def interactive_menu():
    """Interactive menu for ESP32 operations"""
    while True:
        print("\n" + "="*50)
        print("ESP32 MicroPython Deployment Menu")
        print("="*50)
        print("1. Check connection")
        print("2. Deploy files (main.py + helper.py)")
        print("3. List files on ESP32")
        print("4. Run main.py")
        print("5. Reset ESP32")
        print("6. Clean ESP32 (remove test files)")
        print("7. Deploy and run (2 + 4)")
        print("8. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            check_connection()
        elif choice == "2":
            deploy_files()
        elif choice == "3":
            list_files()
        elif choice == "4":
            run_main()
        elif choice == "5":
            reset_esp32()
        elif choice == "6":
            clean_esp32()
        elif choice == "7":
            if deploy_files():
                time.sleep(1)
                run_main()
        elif choice == "8":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    print("🎯 ESP32 MicroPython Deployment Tool")
    print(f"📱 Target device: {ESP32_PORT}")
    
    if len(sys.argv) > 1:
        # Command line mode
        command = sys.argv[1].lower()
        if command == "check":
            check_connection()
        elif command == "deploy":
            deploy_files()
        elif command == "list":
            list_files()
        elif command == "run":
            run_main()
        elif command == "reset":
            reset_esp32()
        elif command == "clean":
            clean_esp32()
        elif command == "all":
            if deploy_files():
                time.sleep(1)
                run_main()
        else:
            print(f"❌ Unknown command: {command}")
            print("Available commands: check, deploy, list, run, reset, clean, all")
    else:
        # Interactive mode
        interactive_menu()
