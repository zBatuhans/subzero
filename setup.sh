#!/bin/bash

echo "[*] Checking for python3..."
if ! command -v python3 &> /dev/null; then
    echo "[!] python3 not found. Please install it first."
    exit 1
fi

echo "[*] Creating virtual environment..."
python3 -m venv venv || { echo "[!] Failed to create virtualenv"; exit 1; }

echo "[*] Activating virtual environment..."
source venv/bin/activate

echo "[*] Upgrading pip..."
pip install --upgrade pip

echo "[*] Installing requirements..."
pip install -r requirements.txt || { echo "[!] Failed to install requirements"; exit 1; }

echo "[*] Giving execution permission to main file..."
chmod +x subzero.py

echo "[*] Creating executable wrapper..."
echo -e '#!/bin/bash\nsource '"$(pwd)/venv/bin/activate"'\npython3 '"$(pwd)/subzero.py"' "$@"' > subzero
chmod +x subzero

echo "[*] Moving launcher to /usr/local/bin (requires sudo)..."
sudo cp subzero /usr/local/bin/subzero

echo "[✓] Installed successfully! Now you can run the tool like this:"
echo ""
echo "    subzero -u example.com -w wordlist.txt"
echo ""
