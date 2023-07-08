<h1 align="center" id="title">ArprSpoofer</h1>

<p align="center"><img src="https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&amp;logo=python&amp;logoColor=white)](https://www.python.org" alt="project-image"> <img src="https://img.shields.io/badge/Scapy-2.4.5-3776AB.svg?style=flat&amp;logo=scapy&amp;logoColor=white" alt="project-image"></p>

<p align="center">
    <img src="img/arp.png" alt="Arp Spoofing">
</p>

<p id="description">arp-spoofer is a Python program that allows you to perform ARP spoofing on a local network. ARP spoofing is an attack technique where an attacker sends forged ARP packets on the network to manipulate the ARP table of target devices, creating a false association between IP addresses and MAC addresses. It allows an attacker to intercept and manipulate network traffic between a victim/target and the gateway/router by forging ARP packets.

  It is important to note that ARP spoofing is a potentially illegal and unethical activity if used without proper authorization. This tool should only be used for educational purposes or on authorized networks with the explicit permission of the network owner.

  Ensure that you have the necessary permissions to run the program and perform ARP spoofing on your network. </p>


<h2>🛠️ Installation Steps:</h2>

<p>Install the requirements:</p>

```
pip -r requirements.txt
```

<h2>🖥️ Usage: </h2>
<p>Manual:</p>


```
arp-spoofer.py [-h] -t TARGET -g GATEWAY -n FREQUENCY

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        IP address of the victim/target
  -g GATEWAY, --gateway GATEWAY
                        IP address of the gateway
  -n FREQUENCY, --frequency FREQUENCY
                        Number of seconds to wait before retrying the spoof operation
```

 
 <p>Examples: </p>

1. Spoof ARP between a target (192.168.1.100) and the gateway (192.168.1.1) with a frequency of 2 seconds:

```
python arp-spoofer.py -t 192.168.1.100 -g 192.168.1.1 -n 2
```

2. Spoof ARP between a target (10.0.0.5) and the gateway (10.0.0.1) with a frequency of 5 seconds:


```
python arp-spoofer.py --target 10.0.0.5 --gateway 10.0.0.1 --frequency 5
```


<h2>😉 Tip: </h2>

Use arp-spoofer together with my dns-spoofer for more complex attacks.

<h2>💖Like my work?</h2>

Contact me if you have any corrections or additional features to offer.
