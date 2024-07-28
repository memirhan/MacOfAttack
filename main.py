from scapy.all import *

secim = input("Kaç paket göndericeksin: ")

for i in range(int(secim)):

    sourceMac = RandMAC() # Rastegele MAC adresi oluşturdu
    destinationMac = RandMAC() # Rastegele MAC adresi oluşturdu
    sourceIp = RandIP() # Rastegele IP adresi oluşturdu
    destinationIp = RandIP() # Rastegele IP adresi oluşturdu

    ether = Ether(src=sourceMac,dst=destinationMac)
    ip = IP(src=sourceIp,dst=destinationIp)

    packet = ether/ip # ether ile ip yi tek paket içerisinde birleştirdik. Hem Ip hemde Mac değerileri oluyor gönderilen paketlerin

    print("Giden Mac = ", sourceMac, " : Giden Ip = ", sourceIp)
    print("Varış Mac = ", destinationMac, " : Varış Ip = ", destinationIp)

    sendp(packet,iface="eth0", verbose = False) # verbose=False ile gönderilen paketlerin bildirimlerini terminalde görünmesin dedik
