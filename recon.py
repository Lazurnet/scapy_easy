from scapy.all import sniff, wrpcap

 """
    Capture du trafic réseau sur une interface donnée.

    interface : nom de l'interface (ex: 'eth0', 'br-internal')
    count     : nombre de paquets à capturer (0 = illimité jusqu'à CTRL-C)
    flt       : filtre BPF (ex: 'icmp', 'tcp', 'port 80')
    savefile  : nom du fichier .pcap pour sauvegarder la capture
    """

def sniff_interface(interface, count, filter):

    
    sniff(iface=interface, count=count, filter=filter)
    sniff(filter="tcp", count=5)
