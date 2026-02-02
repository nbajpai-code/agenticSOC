# Open Source Network Stress & DDoS Simulation Tools

This document contains a comprehensive list of open-source tools often used for network stress testing, denial-of-service simulations, and red team engagements. These tools are similar in nature or function to LOIC (Low Orbit Ion Cannon).

> [!WARNING]
> **Legal Disclaimer**: These tools are intended for **authorized security testing and educational purposes only**. Using these tools to attack targets without explicit permission is **illegal** and punishable by law. The maintainers of this repository assume no liability for misuse.

## Classic Packet Flooding / Stressers

### 1. LOIC (Low Orbit Ion Cannon)
The classic network stress testing tool. Originally developed by Praetox, it allows for TCP, UDP, and HTTP flooding.
- **Language**: C# / C# (Mono) / JS
- **Key Features**: Easy GUI, HIVEMIND mode (IRC botnet control).
- **Repo**: [NewEraCracker/LOIC](https://github.com/NewEraCracker/LOIC) (and many forks)

### 2. HOIC (High Orbit Ion Cannon)
Designed as a replacement for LOIC, focused on high-speed HTTP flooding with "booster" scripts to randomize counter-measures.
- **Language**: BASIC / C# (Ports)
- **Key Features**: High concurrency, custom booster scripts for varying user agents/headers.
- **Repo**: *Various forks available on GitHub searched under "HOIC"*

### 3. UDP Unicorn
A lightweight Win32 DoS tool focused on UDP flooding attacks.
- **Language**: C / C++
- **Key Features**: Multi-threaded UDP flooding.
- **Repo**: [SourceForge / GitHub Mirrors]

## Layer 7 / Application Layer Stressers

### 4. Slowloris
A tool that exhausts a web server's concurrent connections by holding them open as long as possible (Layer 7 attack).
- **Language**: Python / Perl
- **Key Features**: Low bandwidth requirement, highly effective against Apache 1.x/2.x.
- **Repo**: [gkbrk/slowloris](https://github.com/gkbrk/slowloris)

### 5. HULK (HTTP Unbearable Load King)
Generates a massive amount of unique traffic to obscure traffic patterns and bypass caching engines.
- **Language**: Python / Go
- **Key Features**: User Agent randomization, unique URL generation.
- **Repo**: [grafov/hulk](https://github.com/grafov/hulk) (Go port)

### 6. GoldenEye
A Python app designed for testing HTTP Denial of Service, utilizing Keep-Alive and Cache-Control headers to exhaust server resources.
- **Language**: Python
- **Key Features**: Layer 7 stress testing, robust against basic mitigations.
- **Repo**: [jseidl/GoldenEye](https://github.com/jseidl/GoldenEye)

## Modern & Multi-Vector Suites

### 7. Raven-Storm
A powerful, modular DDoS framework written in Python. It includes tools for minimizing footprints and maximizing effectiveness.
- **Language**: Python
- **Key Features**: Modular, Layer 3/4/7 support, Bluetooth/WiFi jamming modules.
- **Repo**: [Taguar258/Raven-Storm](https://github.com/Taguar258/Raven-Storm)

### 8. MikuMikuBeam
A modern, Docker-ready network stresser capable of multiple attack vectors.
- **Language**: Node.js / Python
- **Key Features**: HTTP Flood, Slowloris, TCP Flood, visual interface.
- **Repo**: [skiddou/MikuMikuBeam](https://github.com/skiddou/MikuMikuBeam)

### 9. MHDDoS
A highly popular script supporting 50+ attack methods (Layer 4 & 7).
- **Language**: Python
- **Key Features**: Proxy support, huge variety of attack modes (Cloudflare bypass, Google shield bypass simulation).
- **Repo**: [MatrixTM/MHDDoS](https://github.com/MatrixTM/MHDDoS)

## Professional Load Testing (Dual Use)

These tools are designed for legitimate load testing but are powerful enough to simulate DDoS conditions.

### 10. Locust
An open-source load testing tool that allows you to define user behavior with Python code.
- **Repo**: [locustio/locust](https://github.com/locustio/locust)

### 11. Yandex.Tank
An extensible open-source load testing tool for advanced linux-based environments.
- **Repo**: [yandex/yandex-tank](https://github.com/yandex/yandex-tank)

### 12. Tsunami
While primarily a security scanner, "Tsunami" is also the name of an older UDP flooder (Tsunami-UDP). Ensure you are looking at the correct tool context.
