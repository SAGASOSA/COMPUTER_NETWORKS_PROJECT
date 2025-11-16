# Network Addressing & Subnet Calculator

import streamlit as st
import ipaddress

# Set the page title and a fun icon
st.set_page_config(page_title="Subnet Calculator", page_icon="🌐")

# --- Page Title ---
st.title("🌐 IPv4 Subnet Calculator")
st.caption("A tool to analyze IPv4 networks (IT3501 Project)")

# --- Input Form ---
# We use a form so the page only reruns when the button is clicked
with st.form("subnet_form"):
    st.subheader("Enter Network Address")
    
    # Text input for the IP address in CIDR or IP/Mask format
    ip_input = st.text_input(
        "Enter an IP Address in CIDR notation (e.g., 192.168.1.10/24)",
        placeholder="192.168.1.10/24"
    )
    
    # Submit button
    submitted = st.form_submit_button("Calculate")

# --- Calculation and Results ---
if submitted and ip_input:
    try:
        # This is the core logic. 
        # ipaddress.ip_network() is the perfect tool for this.
        # strict=False allows host addresses (like 192.168.1.10)
        # instead of just network addresses (like 192.168.1.0).
        network = ipaddress.ip_network(ip_input, strict=False)
        
        st.subheader("Analysis Results")
        
        # Display results in two clean columns
        col1, col2 = st.columns(2)

        # --- Column 1 ---
        with col1:
            st.metric(label="Network Address", value=f"{network.network_address}")
            st.metric(label="Broadcast Address", value=f"{network.broadcast_address}")
            
            # Get the host range
            hosts = list(network.hosts())
            if len(hosts) >= 2:
                st.metric(label="Valid Host Range", value=f"{hosts[0]}  to  {hosts[-1]}")
            else:
                st.metric(label="Valid Host Range", value="N/A (too small)")

        # --- Column 2 ---
        with col2:
            st.metric(label="Subnet Mask", value=f"{network.netmask}")
            st.metric(label="Total Addresses", value=f"{network.num_addresses}")
            
            # Usable hosts = Total - 2 (for network and broadcast)
            # Handle small subnets like /31 and /32
            usable_hosts = max(0, network.num_addresses - 2)
            st.metric(label="Usable Host IPs", value=f"{usable_hosts}")

        # --- Additional Info ---
        st.divider() # A horizontal rule
        
        info_col1, info_col2 = st.columns(2)
        info_col1.info(f"**CIDR Prefix:** `/{network.prefixlen}`")
        info_col2.info(f"**Is Private IP?** `{'Yes' if network.is_private else 'No'}`")

        # Use st.code to show the binary representation
        st.subheader("Binary Representation")
        ip_binary = f"{int(network.network_address):032b}"
        mask_binary = f"{int(network.netmask):032b}"
        
        # Add spacing for readability
        ip_binary_spaced = ".".join([ip_binary[i:i+8] for i in range(0, 32, 8)])
        mask_binary_spaced = ".".join([mask_binary[i:i+8] for i in range(0, 32, 8)])
        
        st.code(f"IP Address:  {ip_binary_spaced}\nSubnet Mask: {mask_binary_spaced}", language=None)

    except ValueError as e:
        # Show an error if the input is invalid
        st.error(f"Invalid Input: Please enter a valid IPv4 address with a prefix (e.g., 192.168.1.10/24)")
        st.warning(f"Details: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

else:
    st.info("Please enter an IP address and click 'Calculate'.")
