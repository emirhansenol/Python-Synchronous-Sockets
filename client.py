import socket
import threading
import time


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Open the input file "in-proj.txt" located inside step-5 subdirectory
    # with open('step-5/in-proj.txt', 'r') as f:
    with open('test_cases2.txt', 'r') as f:
        # Read each line
        for line in f:
            # Send the line to the server
            cs.send(line.encode('utf-8'))

    # close the client socket
    cs.close()
    exit()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    time.sleep(5)

    print("Done.")
