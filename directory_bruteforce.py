#!/usr/bin/env python3
import os
import sys
import logging
try:
    import threading
except:
    sys.exit("Install missing library: pip install threaded")
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")

if len(sys.argv) !=4:
    print("follow the example: ")
    print("")
    print("%s https://link.com /usr/share/wordlists/wfuzz/general/common.txt /home/user/Documents/directory.txt"%(sys.argv[0]))
    sys.exit()

LOG = sys.argv[3]
logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

def brute(url, wordlist):
    for word in wordlist:
        try:
            url_final = "{}/{}".format(url, word.strip())
            print(url_final)
            response = requests.get(url_final)
            code = response.status_code
            if code != 404:
                logging.info("{} [code {}]".format(url_final, code))
                print("{} [code {}]".format(url_final, code))
            else:
                logging.info("{} [code {}]".format(url_final, code))
                print("{} [code {}]".format(url_final, code))
        except KeyboardInterrupt:
            sys.exit()
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
            print("error")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        pass

try:
    if __name__ == "__main__":
        url = sys.argv[1]
        wordlist = sys.argv[2]
        with open(wordlist, "r") as file:
            wordlist = file.readlines()
            brute(url, wordlist)
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)
    pass

