colors = ['\033[94m', '\033[92m', '\033[93m', '\033[91m', '\033[0m', '\033[1m']
try:
    from colorama import init
    init(convert=True)
except:
    colors = ['']*6

class col:
    OKBLUE = colors[0]
    OKGREEN = colors[1]
    WARNING = colors[2]
    FAIL = colors[3]
    ENDC = colors[4]
    BOLD = colors[5]
