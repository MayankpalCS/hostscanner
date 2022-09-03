try:
    
    from queue import Queue
    import time
    from colorama import init, Fore
    import queue
    import threading
    
    from pythonping import ping
    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    reset = Fore.RESET
    def banner():
        print(f"""{green}
            |    | |----| |------ --------   ------- |------- |-----| ||     | ||     | |----- |-----|
            |    | |    | |           |      |       |        |     | | |    | | |    | |      |     |
            |----| |    | |-----|     |      |       |        |-----| |  |   | |  |   | |----- |-----|
            |    | |    |       |     |      |-----| |        |     | |   |  | |   |  | |      ||
            |    | |----| ------|     |            | |        |     | |    | | |    | | |      | |
                                        l       -----| |------- |     | |     || |     || |----- |  |
                    developer-@mayankpal                                                            |
                    github:github.com/mayankpalcs                                                   
                            
                            """)                                                                   


    banner()
    init()
    host=input('Enter three block of the subnet')
    threads=int(input('Number of threads recommended(50 or 100)'))
    q = queue.Queue()


    for i in range(1,226):
        ip=host+'.'+str(i)
        q.put(ip)
    def pinging(n,p):
        while not q.empty():
            ips=q.get()
            a=ping(ips, verbose=False,count=2)
            if a.packet_loss==0:
                print(f"[+]{green}{ips} host is up")
            else:
                pass

    for i in range(threads):
        t=threading.Thread(target=pinging,args=(i,q))
        t.start()
except Exception as e:
    print('install modules mentioned requirements.tx')
    print('Try giving root permission or visit https://pypi.org/project/pythonping/#files to install pythonping')
