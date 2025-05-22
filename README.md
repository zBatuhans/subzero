# SubZero 🔎

**SubZero** is a fast and lightweight Python-based subdomain scanner. It checks for alive subdomains using a wordlist and displays the HTTP status codes with color-coded output.

## 🧪 Features

- Subdomain discovery using HTTPS requests
- Colored output based on HTTP status codes
- Custom `User-Agent` headers
- Timeout handling for slow or unresponsive hosts
- Easy setup via `setup.sh` (virtualenv included)
- Global execution via `subzero` command

---

## ⚙️ Installation

To install and run SubZero, simply use:

```bash
git clone https://github.com/yourusername/subzero.git
cd subzero
chmod +x setup.sh
./setup.sh
After setup, you can run the tool globally using the "subzero" command.

🚀 Usage
subzero -u <target-domain> -w <wordlist-file>

📌 Example:
subzero -u example.com -w wordlist.txt

💡 Sample Output:
https://admin.example.com   200
https://ftp.example.com     X
https://dev.example.com     403

✅ Green: Status codes 100–399 (alive)
❌ Red: Unreachable (timeout, DNS error, etc.)
🔴 Other status codes shown in red

📁 Wordlist
The tool requires a wordlist for subdomain generation. Example:
admin
ftp
dev
test
mail


📦 Requirements
Python 3.7 or higher
argparse
colorama
requests
validators
All dependencies are installed automatically via setup.sh.

👨‍💻 Author
Batuhan Korkmaz
Github: @zBatuhans

⚠️ Disclaimer
This tool is intended for educational purposes and authorized security testing only. Unauthorized scanning of systems you do not own or have permission to test is illegal and unethical. Use responsibly.


📌 License
This project is licensed under the [GNU GPLv3 License](LICENSE).
