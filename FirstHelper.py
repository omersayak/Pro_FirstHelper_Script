#!/usr/bin/env python
import os
import py_compile as pyc
import subprocess as sb
import time


def clear_screen():
    sb.call("clear")

def install_figlet():
    try:
        os.system("apt-get install figlet")
    except Exception as e:
        print("An error occurred:", e)

def banner(text):
    try:
        os.system("figlet -f banner {}".format(text))
    except Exception as e:
        print("An error occurred:", e)

def show_ifconfig():
    try:
        sb.call("ifconfig")
        time.sleep(3.0)
        clear_screen()
    except Exception as e:
        print("An error occurred:", e)

def show_iwconfig():
    try:
        sb.call("iwconfig")
        time.sleep(3.0)
        clear_screen()
    except Exception as e:
        print("An error occurred:", e)

def tool1():
    try:
        install_figlet()
        clear_screen()
        show_ifconfig()
        banner("FirstHelper")
        print("""
        
         -MacChanger-
        1-) Randomize Mac Address
        2-) Enter your mac address manually
        3-) Revert Mac Address to Original
        4-) Main Menu
        
        """)

        def change_mac(mac_type):
            interfacename = input("Enter your interface name: ")
            os.system(f"sudo ifconfig {interfacename} down")
            os.system(f"sudo macchanger {mac_type} {interfacename}")
            os.system(f"sudo ifconfig {interfacename} up")
            print("\033[92mNew mac address set successfully!")
            return main()

        def tool1_main():
            macchoice = input("Enter transaction number: ")
            if macchoice == "1":
                change_mac("-r")
                macchoice1 = input("Do you want to go back to the main menu? (y/n) :")
                if macchoice1 == "y":
                    return tool1_main()
                else:
                    return main()
            elif macchoice == "2":
                macaddress = input("Enter New Mac Address: ")
                change_mac(f"--mac {macaddress}")
            elif macchoice == "3":
                change_mac("-p")
            elif macchoice == "4":
                return main()
            else:
                print("Invalid choice.")
                return tool1_main()

        return tool_main()
    except Exception as e:
        print("An error occurred:", e)

def mode_monitor(interface_name):
    try:
        os.system("sudo airmon-ng check kill && clear && sudo airmon-ng start " + interface_name)
        os.system("sudo service NetworkManager restart")
        time.sleep(3.0)
        show_iwconfig()
        modechoice = input("Do you want to go back to the main menu? (y/n) : ")
        if modechoice == "y":
            main()
        else:
            return tool2()
    except Exception as e:
        print("An error occurred:", e)

def adapter_sql_injection(interface_name):
    try:
        os.system("sudo aireplay-ng -9 " + interface_name)
        time.sleep(2.0)
        clear_screen()
        modechoice = input("Do you want to go back to the main menu? (y/n) : ")
        if modechoice == "y":
            main()
        else:
            return quit()
            clear_screen()
    except Exception as e:
        print("An error occurred:", e)

def increase_txpower(interface_name):
    try:
        show_iwconfig()
        time.sleep(3.0)
        print("Please write the full name of the interface name bro !!")
        # adp = input("Please enter the interface name : ")

        os.system("sudo iw list")
        time.sleep(2.0)
        os.system("clear")
        os.system("sudo iw reg get")
        time.sleep(3.0)
        os.system("clear")
        os.system("sudo iw reg set BZ")
        os.system("clear")
        os.system("sudo iw reg get")
        time.sleep(3.0)
        os.system("clear")
        os.system("sudo iw list")
        time.sleep(4.0)
        os.system("clear")
        os.system("sudo iw dev")
        time.sleep(3.0)
        os.system("clear")
        os.system("sudo ip link set {} down".format(interface_name))
        os.system("clear")
        os.system("sudo iw dev {} set txpower fixed 30dBm".format(interface_name))
        os.system("clear")
        os.system("sudo ip link set {} up".format(interface_name))
        os.system("clear")
        os.system("sudo iw dev")
        time.sleep(3.0)
    except Exception as e:
        print("An error occurred:", e)

def txpower_default(interface_name):
    try:
        os.system("sudo ifconfig {} down" .format(interface_name))
        os.system("sudo iw reg set 00")
        os.system("sudo iwconfig {} txpower 20" .format(interface_name))
        os.system("sudo ifconfig {} up" .format(interface_name))
        os.system("sudo iw dev")
        print("Tx-Power returned to default!!")
    except Exception as e:
        print("An error occurred:", e)

def tool2():
    try:
        install_figlet()
        clear_screen()
        banner("FirstHelper")
        sb.call("iwconfig")
        global interface_name
        interface_name = input("Please enter the interface name: ")

        print('''
                Mode : Monitor and increase TX-Power (30mBm Fixleme) Welcome to MyTool
                1-) Mode Monitor and Does the adapter support injection
                2-) increase TX-Power(30dBm fixed)
                3-) increase TX-Power(default)
                4-) Main menu
                    ''')
        mainchoice = input("Please Choice : ")
        if mainchoice == "1":
            print("""
                1-) Mode Monitor
                2-) Does the adapter support sql injection
                3-) Top menu
                4-) Main menu
                """)
            choice2 = input("Please Choice: ")
            if choice2 == "1":
                return mode_monitor(interface_name)
            elif choice2 == "2":
                return adapter_sql_injection(interface_name)
            elif choice2 == "3":
                return tool2()
            elif choice2 == "4":
                return main()


        elif mainchoice == "2":
            increase_txpower(interface_name)
            mainchoice = input("Do you want to go back to the main menu? (y/n) : ")
            if mainchoice == "y":
                main()
            else:
                quit()

        elif mainchoice =="3":
            txpower_default(interface_name)
            mchoice = input("Main menu or exit (m/e) : ")
            if mchoice == "m":
                main()
            else:
                exit()

        else:
            main()
    except Exception as e:
        print("An error occurred:", e)


def afteranon():
    try:
        os.system("sudo git clone https://github.com/TheKoba-dev/afteranon.git")
        os.system("clear")
        os.system("sudo chown root:root afteranon && sudo chmod 755 afteranon && sudo cp -p afteranon /usr/local/sbin")
        os.system("clear")
        os.system("cd afteranon && sudo chmod +x afteranon && sudo bash afteranon")
        print("Succesfull")
        print("""
        What is Afteranon? Afteranon is a script written for ParrotOs.
        It is used to fix network settings that are corrupted after anonsurf.
        Afteranon developers :
        1-) @setpassunlock
        2-) @LightsOfNorthern
        """)
    except Exception as e:
        print("An error occurred:", e)

def tool3():
    try:
        afteranon()
        afterchoice = input("Main menu or exit (m/e) : ")
        if afterchoice == "m" or "M":
            main()
        else:
            quit()
    except Exception as e:
        print("An error occurred:", e)

def tool4():
    try:
        print("""
           Developer : @Professore_1
           Telegram name : https://t.me/Professore_1
           Contributors to the project :
           1. @sacriphanius
           2. @setpassunlock
           3. @LightsOfNorthern
           """)

        mainchoice = input("Ana Menüye dönmek veya çıkmak istiyor musunuz (e/h) : ")
        if mainchoice == "e" or mainchoice=="E":
            main()
        else:
            quit()
    except Exception as e:
        print("An error occurred:", e)


def hash_identifier():
    try:
        os.system("cd $HOME/Hack-Tools/ && sudo git clone https://gitlab.com/kalilinux/packages/hash-identifier.git $HOME/Hack-Tools/hash_identifer")
        os.system("clear")
        os.system("sudo python3 $HOME/Hack-Tools/hash_identifer/hash-id.py")
        hashchoice = input("Main menu or exit (y/n) : ")
        if hashchoice == "y":
            main()
        else:
            quit()
    except Exception as e:
        print("An error occurred:", e)

def tool96():
    hash_identifier()


def delete_logs():
    try:
        clear_screen()
        banner("FirstHelper")
        print("""
        This action is permanent please enter the confirmation text...!
        Onaylıyor musunuz?
        1-) Yes
        2-) No (Main menu)
        3-) Exit
        """)
        logconfirm = input("Please enter arguments : ")
        if logconfirm == "1":
            try:
                os.system("sudo rm -rf $HOME/Hack-Tools/nmap/*")
                os.system("sudo rm -rf $HOME/Hack-Tools/msf/*")
                os.system("sudo rm -rf $HOME/Hack-Tools/tmp/*")
                os.system("sudo rm -rf $HOME/Hack-Tools/cupp/*")
                os.system("sudo rm -rf $HOME/Hack-Tools/hash-identifier/*")
                print("Loglar silindi")
                deletelog = input("Main menu or Top menu (m/t) : ")
                if deletelog == "m" or "M":
                    main()
                else:
                    quit()
            except Exception as e:
                print("An error occurred:", e)
        elif logconfirm == "2":
            main()

        else:
            quit()
    except Exception as e:
        print("An error occurred:", e)

def tool97():
    delete_logs()


def tool98():
    os.system("sudo apt install neofetch")
    os.system("clear")
    os.system("neofetch")
    systemchoice = input("Main menu or exit (y/n) : ")
    if systemchoice == "y":
        main()
    else:
        quit()


def tool99():
    print("See you latter, Broo")
    time.sleep(0.6)
    quit()

def main():
    install_figlet()
    clear_screen()
    banner("FirstHelper")

    print("""
->1-) Mac Address Change Tool                              ->96-) Hash detector
->2-) Mode : Monitor and increase TX-Power (30mBm Fix)     ->97-) Delete logs
->3-) Afteranon (Anonsurf editor)                          ->98-) System info
->4-) Producer and License Info                            ->99-) Exit
    """)

    profchoice = input("Choose : ")
    if profchoice == "1":
        tool1()
    if profchoice == "2":
        tool2()
    if profchoice == "3":
        tool3()
    if profchoice == "4":
        tool4()
    if profchoice == "96":
        tool96()
    if profchoice == "97":
        tool97()
    if profchoice == "98":
        tool98()
    if profchoice == "99":
        tool99()



if __name__ == '__main__':
    main()
