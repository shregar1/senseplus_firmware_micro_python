# ESP32 SensePlus Firmware (MicroPython)

This project contains MicroPython firmware for the ESP32-based SensePlus device, featuring LED control patterns and sensor abstractions.

## 🚀 Quick Start

### Prerequisites

1. **ESP32 with MicroPython**: Ensure your ESP32 has MicroPython firmware installed
2. **Python Tools**: Install required tools on your computer:
   ```bash
   pip install mpremote rshell
   ```

### Hardware Setup

- **ESP32 Development Board** connected via USB
- **Built-in LED** on GPIO 2 (most ESP32 boards)
- **USB Port**: `/dev/tty.usbserial-0001` (update in `deploy.py` if different)

## 📁 Project Structure

```
senseplus_firmware_micro_python/
├── main.py           # Main application entry point
├── helper.py         # LED pattern helper functions
├── deploy.py         # Deployment script for ESP32
├── abstractions/     # Hardware abstraction modules
├── micropythonrc     # MicroPython configuration
└── README.md         # This file
```

## 🔧 Deployment Options

### Option 1: Using the Deployment Script (Recommended)

The `deploy.py` script provides an easy way to manage your ESP32:

```bash
# Interactive menu
python deploy.py

# Command line usage
python deploy.py deploy    # Upload files
python deploy.py run      # Run main.py
python deploy.py all      # Deploy and run
python deploy.py list     # List files on ESP32
python deploy.py clean    # Remove test files
python deploy.py reset    # Reset ESP32
```

### Option 2: Using mpremote directly

```bash
# Deploy files
mpremote connect /dev/tty.usbserial-0001 cp main.py :
mpremote connect /dev/tty.usbserial-0001 cp helper.py :

# Run the program
mpremote connect /dev/tty.usbserial-0001 run main.py

# List files
mpremote connect /dev/tty.usbserial-0001 ls
```

### Option 3: Using rshell

```bash
# Connect to ESP32
rshell -p /dev/tty.usbserial-0001 -b 115200

# Copy files
cp main.py /pyboard/
cp helper.py /pyboard/

# Exit rshell and run with mpremote
mpremote connect /dev/tty.usbserial-0001 run main.py
```

## 💡 LED Patterns

The project includes several LED patterns in `helper.py`:

### Available Functions

1. **`blink_led(led_pin, count=10, delay=0.5)`**
   - Basic on/off blinking
   - Configurable count and delay

2. **`fast_blink(led_pin, count=20, delay=0.1)`**
   - Rapid blinking pattern
   - Good for status indicators

3. **`morse_sos(led_pin)`**
   - SOS morse code pattern (... --- ...)
   - Emergency signal demonstration

4. **`breathing_led(led_pin, cycles=3)`**
   - Smooth PWM fade in/out effect
   - Falls back to blinking if PWM unavailable

5. **`test_all_patterns(led_pin)`**
   - Sequential test of all patterns
   - Great for demonstrations

### Usage Example

```python
import machine
from helper import blink_led, morse_sos, breathing_led

# Initialize LED
led = machine.Pin(2, machine.Pin.OUT)

# Basic blinking
blink_led(led, count=5, delay=0.3)

# SOS signal
morse_sos(led)

# Breathing effect
breathing_led(led, cycles=2)
```

## 🔧 Customization

### Changing LED Pin

If your ESP32 uses a different GPIO for the built-in LED, update `main.py`:

```python
# Change from GPIO 2 to your LED pin
led = machine.Pin(YOUR_GPIO_NUMBER, machine.Pin.OUT)
```

### Adding New Patterns

Add new functions to `helper.py`:

```python
def custom_pattern(led_pin):
    """Your custom LED pattern"""
    # Implementation here
    pass
```

Then import and use in `main.py`:

```python
from helper import custom_pattern
# ... in main function ...
custom_pattern(led)
```

## 🐛 Troubleshooting

### Common Issues

1. **"ImportError: no module named 'helper'"**
   - Ensure `helper.py` is uploaded to ESP32
   - Use deployment script: `python deploy.py deploy`

2. **"mpremote: could not read file"**
   - File path might be incorrect
   - Use relative filenames: `main.py` not `/pyboard/main.py`

3. **"ImportError: no module named 'pycom'"**
   - You're using PyCom-specific code on standard ESP32
   - This project uses standard MicroPython (no pycom library needed)

4. **Connection issues**
   - Check USB cable and port
   - Verify ESP32 has MicroPython firmware
   - Update port in `deploy.py` if needed
   - Try different baud rate: `rshell -p /dev/tty.usbserial-0001 -b 921600`

### Verification Steps

1. **Check connection:**
   ```bash
   python deploy.py check
   ```

2. **List files on ESP32:**
   ```bash
   mpremote connect /dev/tty.usbserial-0001 ls
   ```

3. **Test REPL access:**
   ```bash
   mpremote connect /dev/tty.usbserial-0001 repl
   # Press Ctrl+D to exit
   ```

## 🚀 Next Steps

1. **Add Sensors**: Implement sensor reading in `abstractions/` folder
2. **Networking**: Add WiFi connectivity for IoT features  
3. **Data Logging**: Implement sensor data collection
4. **Web Interface**: Create web-based control panel

## 📚 Resources

- [MicroPython ESP32 Documentation](https://docs.micropython.org/en/latest/esp32/quickref.html)
- [mpremote Documentation](https://docs.micropython.org/en/latest/reference/mpremote.html)
- [ESP32 GPIO Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html)
