from colorama import Fore, Back

# configure colors in this class
class colors():
    FALERT   = Fore.RED
    FSUCCESS = Fore.GREEN
    FNORMAL  = Fore.WHITE
    FURGENT  = Fore.YELLOW
    FPROMPT    = Fore.BLUE

    # Background colors (still do not have any use)

    BALERT = Back.RED
    BSUCCESS = Back.GREEN
    BNORMAL = Back.BLACK
    BURGENT = Back.YELLOW

# provide defaults for all the options for a module
# These values will be overridden if user tends to unset the value
class variables():
    LHOST = ''
    LPORT = ''
    PROTOCOL = ''
    TIMEOUT = 1
    TRYCT = 1
    NMAP = 0
    VERBOSE = ''

# Aliases for the user's comfort
aliases = {
    'exec': 'run',
    'execute': 'run',
    'c': 'clear',
    'probe': 'use probe',
    'info': 'show info',
    'options': 'show options',
    'getstatus': 'show status'
}