import click
import socket 


@click.group(chain=True)
def netsys():
    pass


@netsys.command('myip')
def myip():
    """This commmand tells you your ip address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    s.close()    

if __name__ == '__main__':
    netsys()
