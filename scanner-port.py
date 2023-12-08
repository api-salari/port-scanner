from os import system
try:
    from sys import argv
except:
    system('pip install sys')
try:
    import socket 
except:
    system("pip install socket")
class Fore:
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;34m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"
    nc = "\033[00m"
try:
    system("cls")
except:
    system("clear")
print(Fore.green,
        """
                                                    ..::^^~!!7??JJYY
                                    ...::^^~!!7??JJYYY555555555555Y
                        ..::^^~~!!7~  ~YYY555555555555555555555555555Y
            :^^~!!77?JJJYYY55555555?  !555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            55555555555555555555555?  !5555555555555555555555555555555
            YYYYYYYYYYYYYYJJYYJJJJY7  ~YJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?
            ........................                                  
            JJJJJJJJJJJJJJJJJJJJJJJ7  ~J??????????????????????????????
            55555555555555555555555?  !5555555555555555555555555555555
            55555555555555555555555?  !555555555555555555555555555555Y
            55555555555555555555555?  !555555555555555555555555555555Y
            55555555555555555555555?  !555555555555555555555555555555Y
            55555555555555555555555?  !555555555555555555555555555555Y
            55555555555555555555555?  !555555555555555555555555555555Y
            55555555555555555555555?  !555555555555555555555555555555Y
            55555555555555555555555?  ~555555555555555555555555555555Y
            ^^~!!77??JJYYY555555555?  !555555555555555555555555555555Y
                    ...::^^~!!7?!  ~YYY555555555555555555555555555Y
                                    ...::^^~!!77??JJYYY55555555555Y
                                                    ...::^~~!77?JJYY
""",
    )
def scan(target, start_port, end_port):
    print('\n\n')
    listtrue = []
    for port in range(int(start_port), int(end_port) + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(Fore.white, "--" * 10)
            print(Fore.green, f"Port {port} is open")
            listtrue.append(port)
            sock.close()
        else:
            print(Fore.white, "--" * 10)
            print(Fore.red, f"Port {port} not open")
    if listtrue != []:
        print(Fore.blue, "--" * 10, "\n\n\n")
        for x in listtrue:
            print(Fore.green, f"port in {x} open")
    print(Fore.white)
if argv[1] == '-i':
    try:
        scan(target=argv[2], start_port=argv[3], end_port=argv[4])
    except:
        target = input(f"{Fore.green}[+]{Fore.white} Enter ip target : ")
        start_port = int(input(f"{Fore.green}[+]{Fore.white} Enter Yor start port : "))
        end_port= int(input(f"{Fore.green}[+]{Fore.white} Enter Yor end port : "))
        scan(target=target, start_port=start_port, end_port=end_port)
elif argv[1] == '-s':
    try:
        ip_addr = socket.gethostbyname(argv[2])
        print(Fore.green+"[+]"+Fore.white+" ip "+argv[2]+' : '+ip_addr)
        scan(target=ip_addr, start_port=argv[3], end_port=argv[4])
    except:
        target = input(f"{Fore.green}[+]{Fore.white} Enter ip target : ")
        start_port = int(input(f"{Fore.green}[+]{Fore.white} Enter Yor start port : "))
        end_port = int(input(f"{Fore.green}[+]{Fore.white} Enter Yor end port : "))
        scan(target=target, start_port=start_port, end_port=end_port)
