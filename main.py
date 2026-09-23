import platform
import os
import sys

def get_linux_distro():
    """Rileva il nome della distribuzione Linux corrente."""
    try:
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("NAME="):
                        return line.split("=")[1].replace('"', '').strip()
    except Exception:
        pass
    return platform.system()

def show_fastfetch_art():
    """Stampa il logo ASCII personalizzato per Pymario."""
    art = """
  _____  __   __
 |  __ \\ \\ \\ / /

 | |__) | \\ V /
 |  ___/   \\ /

 | |       | |
 |_|       |_|
    """
    print('\033[92m' + art + '\033[0m') # Stampa l'arte in verde

def main():
    # Raccoglie i dati reali dal tuo sistema Manjaro
    distro = get_linux_distro()
    kernel = platform.release()
    python_version = platform.python_version()
    shell = os.environ.get("SHELL", "Unknown")
    user = os.environ.get("USER", "pymario")

    # Intestazione del terminale
    print(f"\n\033[1;92m{user}@manjaro-workspace\033[0m")
    print("\033[94m-------------------------\033[0m")

    # Mostra l'ASCII Art
    show_fastfetch_art()

    # Tabella delle specifiche (Stile Fastfetch)
    print(f"\033[1;36mOS:\033[0m       {distro}")
    print(f"\033[1;36mKernel:\033[0m   {kernel}")
    print(f"\033[1;36mShell:\033[0m    {shell}")
    print(f"\033[1;36mPython:\033[0m   {python_version}")
    print(f"\033[1;36mProject:\033[0m  GitHub / Pymario22")
    print(f"\033[1;36mStatus:\033[0m   Ambiente di sviluppo pronto su Manjaro 🚀\n")

if __name__ == "__main__":
    main()
