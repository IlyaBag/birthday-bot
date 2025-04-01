import subprocess


def get_raspberry_cpu_temp() -> str:
    """Get CPU temperature if it runs on RaspberryPi OS."""
    try:
        temp = subprocess.run(['vcgencmd', 'measure_temp'],
                              capture_output=True, text=True)
        return temp.stdout
    except FileNotFoundError:
        return "Seems like i'm not in Raspberry Pi..."
