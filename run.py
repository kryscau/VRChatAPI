import os
from dotenv import load_dotenv
load_dotenv()
import sys
import subprocess
import venv

VENV_DIR = os.getenv("VENV_DIR", "venv")
REQ_FILE = os.getenv("REQ_FILE", "requirements.txt")
IS_PUFFERPANEL = os.getenv("IS_PUFFERPANEL", "0") == "1"

# INFORMATIONS : This file does not require “venv” to run, but make sure you have Python installed globally (py run.py on Windows, for example).
# INFORMATIONS : This file does not require “venv” to run, but make sure you have Python installed globally (py run.py on Windows, for example).
# INFORMATIONS : This file does not require “venv” to run, but make sure you have Python installed globally (py run.py on Windows, for example).
# INFORMATIONS : This file does not require “venv” to run, but make sure you have Python installed globally (py run.py on Windows, for example).
# INFORMATIONS : This file does not require “venv” to run, but make sure you have Python installed globally (py run.py on Windows, for example).

def create_venv():
    print("Creating virtual environment...")
    venv.create(VENV_DIR, with_pip=True)

def run_in_venv(cmd):
    if os.name == "nt":
        # Windows
        python_bin = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        # Unix
        python_bin = os.path.join(VENV_DIR, "bin", "python")
    full_cmd = [python_bin] + cmd
    result = subprocess.run(full_cmd)
    if result.returncode != 0:
        print(f"Command {cmd} failed.")
        sys.exit(result.returncode)

def install_requirements():
    print("Installing dependencies...")
    run_in_venv(["-m", "pip", "install", "--upgrade", "pip"])
    run_in_venv(["-m", "pip", "install", "-r", REQ_FILE])

def main():
    if not os.path.exists(VENV_DIR):
        create_venv()
        install_requirements()
    else:
        print("Virtual environment found.")

    print("Running VRChat authentication script...")
    run_in_venv(["app/prelaunch/vrchat_auth.py"])

    print("Starting FastAPI server...")

    host = "0.0.0.0" if IS_PUFFERPANEL else "127.0.0.1"
    reload_flag = "--reload" if not IS_PUFFERPANEL else ""

    run_in_venv(["-m", "uvicorn", "app.main:app", "--host", host, "--port", "8000"] + ([reload_flag] if reload_flag else []))

if __name__ == "__main__":
    main()
