#!/usr/bin/env python
import os
import py_compile as pyc
import subprocess as sb
import time






def tool1():
    os.system("apt-get install figlet")
    os.system("clear")
    sb.call("ifconfig")
    time.sleep(3.0)
    os.system("clear")
    os.system("figlet -f banner FirstHelper")
    print("""
    -MacChanger-
    1-) Randomize Mac Address
    2-) Enter your mac address manually
    3-) Revert Mac Address to Original
    4-) Main Menu
    """)
    macchoice = input("Enter transaction number : ")
    if macchoice == "1":
        interfacename =input("Enter your interface name : ")
        os.system("sudo ifconfig {} down" .format(interfacename))
        os.system("sudo macchanger -r {}" .format(interfacename))
        os.system("sudo ifconfig {} up" .format(interfacename))
        print("\033[92mNew mac address random determined!]")
        macchoice1 = input("Do you want to go back to the main menu? (y/n) :")
        if macchoice1 == "y":
            main()
        else:
            mc0choice = input("Top menu or exit (y/n) : ")
            if mc0choice == "y":
                tool1()
            else:
                quit()


    elif (macchoice == "2"):
        interfacename1 = input("Enter your interface name : ")
        macaddress = input("Enter New Mac Address : ")
        os.system("sudo ifconfig {}} down" .format(interfacename1))
        os.system("sudo macchanger --mac " + macaddress + "{}" .format(interfacename1))
        os.system("sudo ifconfig {} up" .format(interfacename1))
        print("\033[92mNew mac address set manually!]")
        mcchoice = input("Do you want to go back to the main menu? (y/n) : ")
        if mcchoice == "y":
            main()
        else:
            mcchoice1 = input("Top menu or exit (y/n) : ")
            if mcchoice1 == "y":
                tool1()
            else:
                quit()


    elif (macchoice == "3"):
        interfacename2 = input("Enter your interface name : ")
        os.system("sudoifconfig {} down" .format(interfacename2))
        os.system("sudo macchanger -p {}" .format(interfacename2))
        os.system("sudo ifconfig {} up" .format(interfacename2))
        print("\033[92mMac Address Returned to Original!]")
        mc1choice = input("Do you want to go back to the main menu? (y/n) : ")
        if mc1choice == "y":
            main()
        else:
            mc1choice1 = input("Top menu or exit (y/n) : ")
            if mc1choice1 == "y":
                tool1()
            else:
                quit()
    elif macchoice == "4":
        main()

    else:
        print("Hatalı Seçim Yaptınız")
        macprocess = input("Do you want to go back to the main menu? (y/n) : ")
        if macprocess == "y":
            main()
        elif macprocess == "n":
            quit()


def tool2():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")
    sb.call("ifconfig")
    time.sleep(3.0)
    sb.call("clear")

    print('''
        Mode : Monitor and increase TX-Power (30mBm Fixleme) Welcome to MyTool

        1-) Mode Monitor and Does the adapter support injection
        2-) increase TX-Power(30dBm fixed)
        3-) increase TX-Power(default)
        4-) Main menu

        	''')


    mainchoice = input("Please choose : ")

    if mainchoice == "1":
        ifacename = input("Please enter the interface name : ")
        print("""

        1-) Mode Monitor
        2-) Does the adapter support sql injection
        3-) Top menu
        4-) Main menu
        """)
        choice = input("Please choose : ")
        if choice == "1":
            os.system("sudo airmon-ng check kill")
            os.system("clear")
            os.system("sudo airmon-ng start "+ifacename)
            sb.call("clear")
            os.system("sudo service NetworkManager restart")
            time.sleep(3.0)
            sb.call("clear")
            sb.call("iwconfig")
            modechoice = input("Do you want to go back to the main menu? (y/n) : ")
            if modechoice == "y":
                main()
            else:
                modechoice1 = input("Top menu or exit (y/e) : ")
                if modechoice1 == "y":
                    tool2()
                else:
                    quit()

        elif choice == "2":
            os.system("iwconfig")
            time.sleep(3.0)
            os.system("clear")
            ifacename2 = input("Please enter the interface name : ")
            os.system("sudo aireplay-ng -9 "+ifacename2)
            time.sleep(2.0)
            os.system("clear")
            choice1 = input("Top menu or exit (y/n) : ")
            if choice1 =="y":
                tool2()
            else:
                quit()
        elif choice == "3":
            tool2()

        else:
            main()




    elif mainchoice == "2":
        os.system("iwconfig")
        time.sleep(3.0)
        print("Please write the full name of the interface name bro !!")
        adp = input("Please enter the interface name : ")

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
        os.system("sudo ip link set {} down" .format(adp))
        os.system("clear")
        os.system("sudo iw dev {} set txpower fixed 30dBm" .format(adp))
        os.system("clear")
        os.system("sudo ip link set {} up" .format(adp))
        os.system("clear")
        os.system("sudo iw dev")
        time.sleep(3.0)
        mainchoice = input("Do you want to go back to the main menu? (y/n) : ")
        if mainchoice == "y":
            main()
        else:
            upchoice =input("Top menu or exit (y/n) : ")
            if upchoice == "y":
                tool2()
            else:
                quit()

    elif mainchoice == "3":
        ifacename3 = input("Please enter the interface name : ")
        os.system("sudo ifconfig {} down" .format(ifacename3))
        os.system("sudo iw reg set 00")
        os.system("sudo wconfig {} txpower 20" .format(ifacename3))
        os.system("sudo ifconfig {} up" .format(ifacename3))
        os.system("sudo iw dev")
        print("Tx-Power returned to default!!")
        mchoice = input("Main menu or exit (m/e) : ")
        if mchoice=="m":
            main()
        else:
            exit()


    else:
        main()




def tool3():
    os.system("sudo git clone https://github.com/TheKoba-dev/afteranon.git")
    os.system("clear")
    os.system("sudo chown root:root afteranon && sudo chmod 755 afteranon && sudo cp -p afteranon /usr/local/sbin")
    os.system("clear")
    os.system("sudo afteranon")
    print("""
    What is Afteranon? Afteranon is a script written for ParrotOs.
    It is used to fix network settings that are corrupted after anonsurf.


    Afteranon developers :
    1-) @setpassunlock
    2-) @LightsOfNorthern


    """)
    afterchoice = input("Main menu or exit (m/e) : ")
    if afterchoice == "m" or "M":
        main()
    else:
        quit()


def tool4():
    print("""
    Developer : @Professore_1
    Telegram name : https://t.me/Professore_1
    Contributors to the project :
    1. @sacriphanius
    2. @setpassunlock
    3. @LightsOfNorthern
    """)

    mainchoice = input("Main menu or exit (y/n) : ")
    if mainchoice == "y":
        main()
    else:
        quit()

def tool96():
    os.system("cd $HOME/Hack-Tools/ && sudo git clone https://gitlab.com/kalilinux/packages/hash-identifier.git $HOME/Hack-Tools/hash_identifer")
    os.system("clear")
    os.system("sudo python3 $HOME/Hack-Tools/hash_identifer/hash-id.py")
    hashchoice = input("Main menu ır exit (y/n) : ")
    if hashchoice == "y":
        main()
    else:
        quit()



def tool97():
    os.system("figlet -f banner FirstHelper")
    print("""
    This action is permanent please enter the confirmation text...!

    Onaylıyor musunuz?

    1-) Yes
    2-) No (Main menu)
    3-) Exit
    """)
    logconfirm = input("Please enter arguments : ")
    if logconfirm == "1":
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

    elif logconfirm == "2":
        main()

    else:
        quit()

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
    os.system("sudo apt-get install figlet")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")

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
