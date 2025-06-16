#!/usr/bin/env python3
import sys
import time
import requests

# Config
ATTACKER_IP = "192.168.1.86"
WEBHOOK_URL = "http://192.168.1.47:8080/block"  # your vulnubuntu webhook
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1383398853990023239/19TgGBbPurtYMJrG80xOK1DxkVWS9QZ3BtKp8itYoUYoLN3Q1EN37KP3jqUbTFtWzoQz"

# Read Splunk alert payload
payload = sys.stdin.read()
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

# Log locally
with open("/opt/splunk/alert_log.txt", "a") as f:
    f.write(f"[{timestamp}] ALERT TRIGGERED!\n{payload}\n\n")

# Send IP block to victim machine
try:
    r = requests.post(WEBHOOK_URL, json={"attacker_ip": ATTACKER_IP})
    with open("/opt/splunk/alert_log.txt", "a") as f:
        f.write(f"[{timestamp}] Webhook sent. Response: {r.text}\n")
except Exception as e:
    with open("/opt/splunk/alert_log.txt", "a") as f:
        f.write(f"[{timestamp}] Webhook error: {str(e)}\n")

# Send Discord alert
try:
    discord_payload = {
        "content": f":rotating_light: **ALERT**: Reverse shell detected from `{ATTACKER_IP}`\nAuto-blocked on vulnubuntu at `{timestamp}`"
    }
    dr = requests.post(DISCORD_WEBHOOK, json=discord_payload)
    with open("/opt/splunk/alert_log.txt", "a") as f:
        f.write(f"[{timestamp}] Discord notification sent. Status: {dr.status_code}\n")
except Exception as e:
    with open("/opt/splunk/alert_log.txt", "a") as f:
        f.write(f"[{timestamp}] Discord webhook error: {str(e)}\n")
