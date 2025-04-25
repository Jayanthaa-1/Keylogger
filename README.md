#  Keylogger with Tor – Educational Lab Simulation

This project demonstrates stealthy keylogging with anonymized data exfiltration via the Tor network. Built for controlled red-team labs and malware analysis VMs.

## 🔐 Components
- `core.py` → Keylogger, logs to %APPDATA%
- `send_via_tor.py` → Sends logs to .onion receiver using SOCKS5
- `pyinstaller` + `UPX` for EXE compilation and stealth

## ⚠️ DISCLAIMER
**This project is for ethical hacking labs and malware research only.** Unauthorized use is strictly prohibited.


Referencetaken from existing project for educational use by a cybersecurity student.
