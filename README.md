# UhmegleSniffer

**UhmegleSniffer** is a Python-based tool designed to capture and analyze UDP traffic from Omegle/Uhmegle. It identifies external IPs and performs geolocation lookups to retrieve geographic information such as city, region, and ISP. This tool leverages network sniffing techniques to extract IP addresses of Omegle/Uhmegle.

---

## Features

- **Captures UDP traffic** from Omegle/Uhmegle.
- **Identifies external IP addresses**.
- **Performs geolocation lookups** to provide city, region, and ISP information.
- **Excludes IPs related to Cloudflare** to avoid false positives.
- **Displays errors or success** in geolocation results.

---

## Installation

To get started with **UhmegleSniffer**, you need to install the required dependencies. Follow the instructions below:

### Prerequisites

Ensure that you have Python 3.6+ installed on your machine. You can check your Python version by running the following command:

```bash
python --version
```
If you don't have Python installed, you can download it from [python.org](https://www.python.org/).

### Required Libraries

UhmegleSniffer requires the following Python libraries:

- **scapy**: A powerful Python library for network packet manipulation and sniffing.
- **requests**: A simple HTTP library for making requests, used for geolocating IPs.

To install the necessary libraries, run the following command:

```bash
pip install scapy requests
```

## Usage

Once you have installed the dependencies, follow these steps to use the tool:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/UhmegleSniffer.git
    cd UhmegleSniffer
    ```

2. Run the sniffer:

    ```bash
    python sniffer.py
    ```

This will start sniffing UDP packets on the specified network interface (default: `eth0`). It will capture IP addresses and perform geolocation lookups.

### Network Interface

Make sure to replace the `INTERFACE` variable in the code with the correct network interface for your system (e.g., `wlan0` for Wi-Fi on Linux systems, or `en0` on macOS). If you're unsure of your network interface, you can find it by running:

- **Linux/macOS**: `ifconfig` or `ip a`
- **Windows**: `ipconfig`
