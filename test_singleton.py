#!/usr/bin/env python3
"""
Test script to demonstrate the corrected SensorConfiguration singleton pattern.
"""

from configurations.sensor import SensorConfiguration

def test_singleton_pattern():
    """Test that SensorConfiguration follows singleton pattern correctly."""
    
    print("=== Testing SensorConfiguration Singleton ===\n")
    
    # Test 1: Create multiple instances - should be the same object
    print("1. Creating multiple instances...")
    config1 = SensorConfiguration()
    config2 = SensorConfiguration()
    config3 = SensorConfiguration.get_instance()
    
    print(f"config1 id: {id(config1)}")
    print(f"config2 id: {id(config2)}")
    print(f"config3 id: {id(config3)}")
    print(f"All instances are the same object: {config1 is config2 is config3}")
    
    # Test 2: Load and access configuration data
    print("\n2. Loading configuration data...")
    try:
        config_data = config1.get()
        print(f"Full config: {config_data}")
        print(f"Config type: {type(config_data)}")
        
        # Test specific key access
        include_list = config1.get("include")
        print(f"Include list: {include_list}")
        
        # Test non-existent key
        non_existent = config1.get("non_existent_key")
        print(f"Non-existent key: {non_existent}")
        
    except Exception as e:
        print(f"Error loading config: {e}")
    
    # Test 3: Verify that data is cached
    print("\n3. Testing data caching...")
    config_data_1 = config1.get()
    config_data_2 = config2.get()
    print(f"Same cached data object: {config_data_1 is config_data_2}")
    
    print("\n=== Singleton test completed ===")

def demo_usage():
    """Demonstrate proper usage of SensorConfiguration."""
    
    print("\n=== Usage Examples ===\n")
    
    # Method 1: Direct instantiation (recommended)
    config = SensorConfiguration()
    sensors = config.get("include")
    print(f"Enabled sensors: {sensors}")
    
    # Method 2: Using get_instance class method
    config_instance = SensorConfiguration.get_instance()
    full_config = config_instance.get()
    print(f"Full configuration object: {full_config}")
    
    # Method 3: Checking specific sensors
    if sensors:
        print(f"\nSensor availability:")
        for sensor in sensors:
            print(f"  - {sensor}: enabled")
    
    print("\n=== Usage examples completed ===")

if __name__ == "__main__":
    test_singleton_pattern()
    demo_usage()
