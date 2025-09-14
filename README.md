# cisco-enable-rotator
# Cisco Enable Rotator

Automated Python tool to change and rotate enable passwords (enable secrets) on Cisco switches and access points.  
The script integrates with a KeePass database file (`.kdbx`) to fetch the new enable password, making the process secure and centralized.

## Features
- 🔐 Securely update enable secrets across Cisco APs and switches
- 🔑 Fetch new passwords directly from KeePass (.kdbx) database
- 💾 Backup running-configs before making changes
- ⚡ Parallel execution for multiple devices
- 📝 Inventory support via CSV/YAML
- 🧰 Easy to extend for different Cisco platforms

## Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment recommended

### Installation
```bash
git clone https://github.com/your-username/cisco-enable-rotator.git
cd cisco-enable-rotator
pip install -r requirements.txt
