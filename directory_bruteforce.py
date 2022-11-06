#!/usr/bin/env python3
import os
import sys
import time
import logging
try:
    import threading
except:
    sys.exit("Install missing library: pip install threaded")
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")

def helplk():
    print("follow the example: ")
    print("")
    print("%s -h"%(sys.argv[0]))
    print("%s --help"%(sys.argv[0]))
    print("%s -u https://link.com -w /usr/share/wordlists/wfuzz/general/common.txt --save /home/ghost/Documents/directory.txt"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    helplk()
    sys.exit()

elif len(sys.argv) ==2:
    choice = str(sys.argv[1])
    if choice == "-u":
        print("insert valid url")
        sys.exit()
    elif choice == "-h":
        helplk()
        sys.exit()
    elif choice == "--help":
        helplk()
        sys.exit()
    else:
        sys.exit()

elif len(sys.argv) ==2:
    choice = str(sys.argv[3])
    if choice == "-w":
        print("insert valid wordlist")
        sys.exit()
    else:
        sys.exit()

elif len(sys.argv) ==3:
    print("insert valid wordlist")
    sys.exit()

elif len(sys.argv) ==4:
    print("insert valid wordlist")
    sys.exit()

elif len(sys.argv) ==5:
    print("[alert] insert file output save \n \n")

elif len(sys.argv) ==6:
    print("[alert] insert file output save \n \n")

else:
    pass

try:
    LOG = sys.argv[6]
    logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")
except Exception as error:
    print(error)
    pass

def brute(url, wordlist):
    for word in wordlist:
        url_final = "{}/{}".format(url, word.strip())
        print(url_final)
        try:
            response = requests.get(url_final)
            code = response.status_code
            if code != 404:
                logging.info("{} [code {}]".format(url_final, code))
                print("{} [code {}]".format(url_final, code))
            else:
                logging.info("{} [code {}]".format(url_final, code))
                print("{} [code {}]".format(url_final, code))
        except requests.exceptions.Timeout:
            print("requests timeout")
            time.sleep(10)
            pass
        except requests.exceptions.TooManyRedirects:
            print("requests error")
            pass
        except requests.exceptions.RequestException as error:
            print(error)
            pass
        except Exception as error:
            print(error)
            pass
    else:
        pass

    try:
        while True:
            if _ in range(4):
                threading.Thread(target=brute).join.start()
            else:
                print("threading error")
                pass
        else:
            print("loop error")
            pass
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        pass

try:
    if __name__ == "__main__":
        url = sys.argv[2]
        wordlist = sys.argv[4]
        with open(wordlist, "r") as file:
            wordlist = file.readlines()
            brute(url, wordlist)
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)
    pass
