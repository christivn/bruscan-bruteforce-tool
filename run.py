import os,sys,socket
import scanner

os.system('cls' if os.name == 'nt' else 'clear')
print("""\033[33m
▄▄▄▄· ▄▄▄  ▄• ▄▌.▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
▐█ ▀█▪▀▄ █·█▪██▌▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
▐█▀▀█▄▐▀▀▄ █▌▐█▌▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
██▄▪▐█▐█•█▌▐█▄█▌▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪
\033[35m░░░By: Christian Ramos (christivn)░░░\033[33m\033[0m\n""")

credentials = open('credentials.txt', 'r') 
credentials_lines = credentials.readlines()

ips = open('ip_list.txt', 'r') 
ips_lines = ips.readlines()

for p in range(len(ips_lines)):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip=ips_lines[p].rstrip()
    location=(ip, 22)
    result_of_check = a_socket.connect_ex(location)

    if result_of_check==0:
        header="[\033[32m+\033[0m]─── \033[01m"+location[0]+"\033[0m ───\033[32m[ Open Port ]\033[0m──────────┐"
        print(header)

        for x in range(len(credentials_lines)):
            cred=str(credentials_lines[x]).split(":")
            scan=scanner.check(location[0],cred[0],cred[1],header)

            if "✔" in scan:
                sucess=True
                if(x!=0):
                    scanner.separate(header)
                    print(scan)
                else:
                    print(scan)
                break
            else:
                sucess=False
                print(scan)

        if(sucess==False and x==len(credentials_lines)-1):
            scanner.not_found(header)
            
        scanner.close(header)

    else:
        print("\n[\033[31m-\033[0m]─── "+location[0]+" ───\033[31m[ Close Port ]\033[0m\n")

    a_socket.close()