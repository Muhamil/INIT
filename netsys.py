import click
import socket

@click.group(chain=True)
def netsys():
    pass

print("HAHAH")
@netsys.command('myip')
def myip():
    """This command retrieves and displays your local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print("Your IP address is:", s.getsockname()[0])
    except Exception as e:
        print("Error retrieving IP address:", e)
    finally:
        s.close()

@netsys.command('iptell')
@click.argument('hostname')
def iptell(hostname):
    """This command retrieves the IP address of the given hostname."""
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"The IP address of {hostname} is: {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve hostname: {hostname}")

if __name__ == '__main__':
    netsys()
