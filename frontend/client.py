import threading

#ofc we need a separate class for client, but that's just a skeleton for now

def startClient():
  print("started")
  

def startClicked():
  threading.Thread(target = startClient).start()


def main():
  start()

if __name__ == "__main__":
  main()
