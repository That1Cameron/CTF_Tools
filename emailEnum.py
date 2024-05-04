import socket
import sys
address = ""
port = 25

def parseResults():
    with open("enumResults.txt", "r") as file:
        for line in file:
            if "Could not VRFY" not in line:
                print(line, end="")

def main():
    filename = "names2.txt"
    with open(filename) as f:
        users = [line.strip().lower() for line in f.readlines() if line]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    fn = s.makefile('rwb')

    fn.readline()
    fn.write(b'HELO testing.com \r\n')
    fn.flush()
    fn.readline()

    for user in users:
        string = ('VRFY %s\r\n' % user)
        fn.write(string.encode())
        fn.flush()
        print('%s: %s' % (user, fn.readline().strip()))

    fn.write(b'QUIT\r\n')
    fn.flush()
    s.close()

if __name__ == "__main__":
    main()
