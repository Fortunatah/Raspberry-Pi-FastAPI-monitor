## This script will gather my data from the raspery pi's hardware
## From there it will will report it back to main, keeping it in one class

## Create the class of all the hardware data if
## If we can connect to the system then we are good

## Imports

import subprocess
import datetime
import sys

## variables

pi_user = "hayden"
pi_pass = "password"
pi_ip = "10.42.0.167"

# functions

def check_pi_connection(windows):
    if windows:
        # Windows native SSH doesn't have sshpass.
        # We use a shell pipe to feed the password to stdin.
        # Note: This requires shell=True to work correctly on Windows.
        cmd = f"echo {pi_pass} | ssh -o StrictHostKeyChecking=no -o ConnectTimeout=3 {pi_user}@{pi_ip} \"echo Connection Successful\""
    else:
        # Your original Linux/macOS logic using sshpass
        cmd = [
            "sshpass", "-p", pi_pass, 
            "ssh", "-o", "StrictHostKeyChecking=no", 
            "-o", "ConnectTimeout=3",
            f"{pi_user}@{pi_ip}", 
            "echo 'Connection Successful'"
        ]

    try:
        # For Windows, we pass the string command and set shell=True
        # For Linux, we pass the list
        is_shell = True if windows else False
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True, 
            shell=is_shell
        )
        
        return "Connection Successful" in result.stdout
    except subprocess.CalledProcessError:
        return False
    
def collect_cpu_info():
    
    # The SSH command using sshpass for one-liner execution
    # -o ConnectTimeout=3 ensures the script doesn't hang forever if the cable is out
    cmd = [
        "sshpass", "-p", pi_pass, 
        "ssh", "-o", "StrictHostKeyChecking=no", 
        "-o", "ConnectTimeout=3",
        f"{pi_user}@{pi_ip}", 
        "cat /sys/class/hwmon/hwmon*/temp1_input"
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr

def collect_up_time():
    
    # The SSH command using sshpass for one-liner execution
    # -o ConnectTimeout=3 ensures the script doesn't hang forever if the cable is out
    cmd = [
        "sshpass", "-p", pi_pass, 
        "ssh", "-o", "StrictHostKeyChecking=no", 
        "-o", "ConnectTimeout=3",
        f"{pi_user}@{pi_ip}", 
        "cat /proc/uptime"
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr

# class for data collection

class raspberry_pi_data():
    def __init__(self):
        if sys.platform == "win32":
            self.windows = True
        else:
            self.windows = False
        self.connected = check_pi_connection(self.windows)
    
    def hw_data(self):
        ## get the cpu first
        cpu = float(collect_cpu_info())
        self.cpu_temp = round((cpu / 1000.0) , 1)
        ## now get the uptime
        uptime_seconds = float(collect_up_time().split()[0])
        uptime_duration = datetime.timedelta(seconds=uptime_seconds)
        days = uptime_duration.days
        hours, remainder = divmod(uptime_duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.uptime = f"{days} days, {hours} hours, {minutes} minutes"

