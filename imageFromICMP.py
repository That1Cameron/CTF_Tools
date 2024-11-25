import os
from scapy.all import *


def chunkData(data, chunk_size):
	return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def sendImageOverIcmp(file_path, target_ip):
	try:
		# Read the image file as binary data
		with open(file_path, 'rb') as f:
			file_data = f.read()

		chunk_size = 1400  # ICMP payload size limit (excluding headers)
		chunks = chunkData(file_data, chunk_size)

		for idx, chunk in enumerate(chunks):
			print(f"chunk {idx + 1}/{len(chunks)}")
			icmp_packet = IP(dst=target_ip)/ICMP()/Raw(load=chunk)
			send(icmp_packet, verbose=False)

		print("Image sent successfully.")
	except Exception as e:
		print(f"Error: {e}")


def processPcap(pcap_file, src_ip, output_file):
	packets = rdpcap(pcap_file)

	with open(output_file, "wb") as f:
		for pkt in packets:
			if IP in pkt and pkt[IP].src == src_ip:
				if Raw in pkt:
					f.write(pkt[Raw].load)


# Usage
if __name__ == "__main__":
	"""
	target_ip = "127.0.0.1"
	file_path = "C:\\Users\\*\\Documents\\ICMP\\image.png"

	if not os.path.isfile(file_path):
		print("Invalid file path. Please try again.")
	else:
		sendImageOverIcmp(file_path, target_ip)"""

	pcap_file = "imageTransfer.pcapng"
	src_ip = "127.0.0.1"
	output_file = "data_section.png"
	processPcap(pcap_file, src_ip, output_file)
