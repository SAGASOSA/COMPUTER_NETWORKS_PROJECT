import streamlit as st
import socket
import concurrent.futures

st.set_page_config(page_title="Port Scanner", page_icon="📡")

st.title("📡 Simple Network Port Scanner")
st.caption("A tool to check for open TCP ports (Unit 5)")

def check_port(host_ip, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host_ip, port))
            if result == 0:
                return (port, True) 
            else:
                return (port, False) 
    except socket.error as e:
        return (port, False)

target_host = st.text_input(
    "Enter Target Hostname or IP", 
    placeholder="e.g., google.com or 142.250.196.110"
)

port_input = st.text_area(
    "Enter Ports (comma-separated)",
    placeholder="e.g., 80, 443, 22, 8080"
)

scan_button = st.button("Start Scan")

if scan_button:
    if not target_host or not port_input:
        st.warning("Please fill in both the host and the port fields.")
    else:
        try:
            target_ip = socket.gethostbyname(target_host)
            st.info(f"Scanning target: **{target_host}** (IP: `{target_ip}`)")
        except socket.gaierror:
            st.error(f"Error: Could not resolve hostname '{target_host}'")
            st.stop() 
            
        ports_to_scan = []
        try:
            for port_str in port_input.split(','):
                port = int(port_str.strip())
                if 1 <= port <= 65535:
                    ports_to_scan.append(port)
                else:
                    st.warning(f"Invalid port number: {port} (skipping)")
            
            if not ports_to_scan:
                st.error("No valid ports to scan.")
                st.stop()
                
            ports_to_scan = sorted(list(set(ports_to_scan))) 
            
        except ValueError:
            st.error("Error: Invalid port list. Please use comma-separated numbers.")
            st.stop()

        st.subheader("Scan Results:")
        
        with st.spinner(f"Scanning {len(ports_to_scan)} port(s)..."):
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                futures = {executor.submit(check_port, target_ip, port): port for port in ports_to_scan}
                results = []
                for future in concurrent.futures.as_completed(futures):
                    results.append(future.result())

        results.sort() 
        for port, is_open in results:
            if is_open:
                st.success(f"Port **{port}** is **OPEN**")
            else:
                st.error(f"Port **{port}** is **CLOSED**")
        
        st.success("Scan complete.")