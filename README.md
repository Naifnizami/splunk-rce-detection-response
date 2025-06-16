# 🔐 Splunk + SOAR Lab: Real-Time Reverse Shell Detection and Auto-Response

This lab simulates a full cybersecurity workflow: from web app exploitation to automated threat detection, IP blocking, and real-time alerting using open-source tools.

---

## 📸 Screenshots

| Step | Description | Screenshot |
|------|-------------|------------|
| 1 | Kali setup with Splunk Enterprise | ![Kali Splunk](images/01-kali-splunk.png) |
| 2 | Vulnubuntu stack (Apache, MySQL, PHP, UF) | ![Ubuntu stack](images/02-ubuntu-stack.png) |
| 3 | Vulnerable login + upload form (`index.php`) | ![Login](images/03-login-page.png) |
| 4 | Web shell uploaded and accessed | ![Upload](images/04-shell-upload.png) |
| 5 | Reverse shell via netcat | ![Shell](images/05-reverse-shell.png) |
| 6 | Apache logs in Splunk | ![Logs](images/06-splunk-apache-logs.png) |
| 7 | Splunk alert configured | ![Alert](images/07-alert-config.png) |
| 8 | Script logging alert + webhook | ![Log](images/08-alert-log.png) |
| 9 | Discord alert received | ![Discord](images/09-discord-alert.png) |
| 10 | Attacker IP blocked via iptables | ![Block](images/10-iptables-block.png) |
| 11 | Kali ping blocked by vulnubuntu | ![Fail](images/11-ping-fail.png) |

---

## 🎥 Demo Videos

- 🎬 [Full Attack & Response Demo](recordings/full-attack-demo.mp4)
- 🧠 [Creating Splunk Alert](recordings/01-create-alert.mp4)
- 🔥 [Triggering Reverse Shell](recordings/02-reverse-shell.mp4)
- 🔎 [Testing SQL Injection](recordings/03-login-test.mp4)

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `index.php` | Vulnerable app with login & upload |
| `shell.php` | Web shell endpoint |
| `alert_handler.py` | Splunk script → sends webhook + Discord alert |
| `blocker.py` | Flask listener → triggers `iptables` block |
| `vulnapp_schema.sql` | DB schema dump |

---

## 💡 What This Project Shows

- Red Team exploitation using RCE
- Log ingestion and parsing with Splunk
- Blue Team detection via Apache log monitoring
- Custom scripted SOAR-style response:
  - Webhook
  - IP block
  - Discord alert
- Real-time containment simulation

---

## 🧠 Author

**Naif Nizami**  
Cybersecurity Lab Project | June 2025  
🔗 [LinkedIn](#) • 🌐 [Portfolio](#)

---

## 📜 License

MIT License  
[View LICENSE](LICENSE)

