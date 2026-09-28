

def sniff_interface(interface, count, filter):
    sniff(iface=interface, count=count, filter=filter)
    sniff(filter="tcp", count=5)
