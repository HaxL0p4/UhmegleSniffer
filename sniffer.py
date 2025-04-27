# By L0pa ;) 
from scapy.all import sniff, IP, UDP
import requests

seen_ips = set()

def geolocate_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,query", timeout=3)
        data = r.json()
        if data["status"] == "success":
            if "Google" in data["isp"] or "Cloudflare" in data["isp"]:
                return
            print(f"[📍] {ip} → {data['city']}, {data['regionName']}, {data['country']} ({data['isp']})\n")
        else:
            print(f"[!] Error geolocating {ip}: {data.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"[!] Error in HTTP request: {e}")

def packet_callback(packet):
    if IP in packet and UDP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        for ip in (src_ip, dst_ip):
            if ip.startswith(("192.168.", "10.", "172.", "127.")) or ip in seen_ips:
                continue
            seen_ips.add(ip)
            print(f"[+] External IP detected: {ip}")
            geolocate_ip(ip)

if __name__ == '__main__':
    INTERFACE = input("Interface (es. wlan0) : )

    print(f"\n[*] Starting sniffer on {INTERFACE} (only UDP traffic)")
    print("[*] Press CTRL+C to stop.\n")

    try:
        sniff(iface=INTERFACE, filter="udp", prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\n[!] Sniffing interrupted manually. Exiting...")
