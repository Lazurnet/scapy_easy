# Scapy Easy

Petit outil pédagogique de reconnaissance active basé sur **Scapy**, réalisé dans le cadre du module Netacad *3.2 – Fabrication de paquets avec Scapy*.  
Il permet d’apprendre à manipuler, envoyer et analyser des paquets réseau.

##  Fonctionnalités

- **Sniffing réseau**
  - Capture de paquets sur une interface
  - Filtrage BPF (`icmp`, `tcp`, `port 80`)
  - Export en `.pcap`

- **ICMP personnalisé**
  - Création d’un paquet ICMP Echo Request
  - Payload custom
  - Affichage du paquet avec `.show()`

- **Scan TCP SYN**
  - Envoi d’un SYN
  - Analyse des flags TCP (SA = ouvert, RA = fermé)

- **Spoofing ICMP**
  - Envoi d’un ICMP avec adresse source falsifiée
