import subprocess


def run_or_install_requirements()->None:
    try:
        subprocess.call(["python", "src/main.py"])
    except ImportError:
        subprocess.check_call(['pip', 'install', '-r', 'src/requirements.txt'])
        print("Restart the program")


run_or_install_requirements()
