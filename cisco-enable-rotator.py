from pykeepass import PyKeePass
from netmiko import ConnectHandler

# Open KeePass database
kp = PyKeePass("C:\\your\\keepassFile\\path\\here", 
               password="your_keepass_passwordFile")

# Find group in keepass that contains the passwords wich you want to change
device_group = kp.find_groups(name="devices", first=True) #change devices with your group name

# Your SSH credentials (to connect into the APs)
ssh_user = "yourlogin"      # Replace with your login user
ssh_pass = "yourpass"  # Replace with your login password

# Open a file to log only the results in APPEND mode
result_log = open("results.txt", "a", encoding='utf-8')  # Changed to 'a'

def update_device_password(entry):
    device_ip = entry.username        # IP stored in KeePass "User Name"
    new_enable_pass = entry.password  # KeePass "Password" is the new enable secret

    device = {
        "device_type": "cisco_ios",
        "host": device_ip,
        "username": ssh_user,
        "password": ssh_pass,
    }

    try:
        print(f"[+] Connecting to {device_ip}...")
        net_connect = ConnectHandler(**device)

        # Configure new enable password
        commands = [
            f'enable secret "{new_enable_pass}"',
            "do write memory"
        ]
        output = net_connect.send_config_set(commands, read_timeout=40)
        print(output)

        net_connect.disconnect()
        success_message = f"[✔] Updated enable password on {device_ip}"
        print(success_message)
        # Write and IMMEDIATELY flush the success message to the file
        result_log.write(success_message + "\n")
        result_log.flush()  # <-- This forces the write to disk now

    except Exception as e:
        error_message = f"[✘] Failed to update {device_ip}: {e}"
        print(error_message)
        # Write and IMMEDIATELY flush the error message to the file
        result_log.write(error_message + "\n")
        result_log.flush()  # <-- This forces the write to disk now

# Iterate through all device entries (including subgroups)
for group in device_group.subgroups:
    for entry in group.entries:
        update_device_password(entry)

# Close the results log file
result_log.close()
print("\nScript finished. Results were live-saved to 'results.txt'")