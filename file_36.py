# This Program by m.mahadi 
import os
def shatdown():
    os.system("shutdown /s /t 0")
def restart():
    os.system("shutdown /r /t 0")
def main():
    while True:
        Start = int(input('1. Shatdown\n2. Restart\n3. Exit\n'))
        if Start ==1:
            shatdown()
        elif Start ==2:
            restart()
        elif Start ==3:
            ask = input('Do you close this program? [Y/N]')
            if ask == 'Y' or ask == 'y':
                break
            elif ask == 'N' or ask == 'n':
                main()
            else:
                print('Error')

if __name__ == '__main__':
    main()


