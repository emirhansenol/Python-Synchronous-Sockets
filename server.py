import socket
import threading
import time


def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    # Open the output files
    with open('outr-proj.txt', 'w') as f1, open('outup-proj.txt', 'w') as f2:
        while True:
            # Receive data from the client
            # Receive only 1 character from the client until a newline character is encountered
            data = ''
            while '\n' not in data:
                chunk = csockid.recv(1).decode('utf-8')
                if not chunk:
                    break
                data += chunk
            if not data:
                break

            # Split the received data into lines, and write them to file after reversing
            for line in data.splitlines():
                f1.write(line[::-1].encode('utf-8') + '\n')

            # Write received data in uppercase to the file
            f2.write(data.upper().encode('utf-8'))

    # Close the server socket and the files
    ss.close()
    f1.close()
    f2.close()
    exit()


if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
    time.sleep(5)

    print("Done.")
