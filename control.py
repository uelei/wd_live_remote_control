import requests
# import keybord


"""curl 'http://192.168.0.13/cgi-bin/toServerValue.cgi' -H 'Cookie: keepSign=1; user_pw=admin; PHPSESSID=b5b5c97d665826c7bef3e63d290d9daf; online=0' -H 'Origin: http://192.168.0.13' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: pt,en-US;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://192.168.0.13/Main.php' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data '{"remote":"n"}' --compressed

"""


# def run():
#     while True:
#         key = input()


# import sys, termios, tty, os, time
# import fcntl


# def getch():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)

#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch


# button_delay = 0.2

# fd = sys.stdin.fileno()
# fl = fcntl.fcntl(fd, fcntl.F_GETFL)
# fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# while True:
#     char = getch()

#     if char == "p":
#         print("Stop!")
#         exit(0)

#     elif not char:
#         print("No char")
#     elif char == "a":
#         print("Left pressed")
#         time.sleep(button_delay)

#     elif char == "d":
#         print("Right pressed")
#         time.sleep(button_delay)

#     elif char == "w":
#         print("Up pressed")
#         time.sleep(button_delay)

#     elif char == "s":
#         print("Down pressed")
#         time.sleep(button_delay)

#     elif char == "1":
#         print("Number 1 pressed")
#         time.sleep(button_delay)
import sys, termios, tty, os, time


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


button_delay = 0.2


values ={"up":"n",
         "ok": "n",
         "down": "d",
         "left": "l",
         "right": "r",
         }



def request_action(action):
    header ={
        "Cookie": "keepSign=1; user_pw=admin; PHPSESSID=b5b5c97d665826c7bef3e63d290d9daf; online=0",
        "Origin": "http://192.168.0.13",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "pt,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Referer": "http://192.168.0.13/Main.php",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-aliv",
    }
    r = requests.get("http://192.168.0.13/cgi-bin/toServerValue.cgi",headers=header,data='{"remote":"'+action+'"}')



while True:
    char = getch().encode()
    str_c = char.decode("ASCII")
    if char == b"q":
        print("Stop!")
        exit(0)

    print(char,str_c)
    if b"A" in char:
        request_action("u")
    elif b"B" in char:
        request_action("d")
    elif b"C" in char:
        request_action("r")
    elif b"D" in char:
        request_action("l")

    elif char==b"e" or char ==b"\r":
        request_action("n")

    elif char==b"b":
        request_action("T")
    # b'\x1b'
    # if char == "a":
    #     print("Left pressed")
    #     time.sleep(button_delay)

    # elif char == "d":
    #     print("Right pressed")
    #     time.sleep(button_delay)

    # elif char == "w":
    #     print("Up pressed")
    #     time.sleep(button_delay)

    # elif char == "s":
    #     print("Down pressed")
    #     time.sleep(button_delay)

    # elif char == b"f":
    #     print("f")
    #     request_action("a")
    #     time.sleep(button_delay)

    # elif char == "1":
    #     print("Number 1 pressed")
    #     time.sleep(button_delay)
    # elif char == b"\x1b[A":
    #     print("up")
    # elif char == "\x1b[B":
    #     print("down")
    # elif char == "\x1b[C":
    #     print("right")
    # elif char == "\x1b[D":
    #     print("left")
