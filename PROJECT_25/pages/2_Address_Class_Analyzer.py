import streamlit as st
import ipaddress

# Page configuration
st.set_page_config(page_title="Address Analyzer", page_icon="🧭")
st.title("🧭 Classful Address Analyzer")
st.caption("This tool analyzes an IPv4 address to determine its original class (A, B, C, D, or E).")

# --- Input Field ---
ip_input = st.text_input(
    "Enter a single IPv4 Address",
    placeholder="e.g., 172.16.10.5"
)

# --- Analysis Logic ---
if ip_input:
    try:
        # Parse the input as a single IP address
        ip_obj = ipaddress.ip_address(ip_input)
        
        # Get the first octet (the first number)
        first_octet = ip_obj.packed[0]
        
        result_class = ""
        default_mask = ""
        note = ""

        # --- Determine the Class based on the first octet ---
        if 0 <= first_octet <= 127:
            result_class = "A"
            default_mask = "255.0.0.0"
            if first_octet == 127:
                note = "This is a **Loopback Address**."
            elif first_octet == 0:
                 note = "This is part of the **'This Host'** network."
        elif 128 <= first_octet <= 191:
            result_class = "B"
            default_mask = "255.255.0.0"
        elif 192 <= first_octet <= 223:
            result_class = "C"
            default_mask = "255.255.255.0"
        elif 224 <= first_octet <= 239:
            result_class = "D"
            default_mask = "N/A (Multicast)"
            note = "This is a **Multicast Address**."
        elif 240 <= first_octet <= 255:
            result_class = "E"
            default_mask = "N/A (Reserved)"
            note = "This is a **Reserved Address** for future/experimental use."

        # --- Display the Results ---
        st.subheader(f"Analysis for: `{ip_input}`")
        
        col1, col2 = st.columns(2)
        col1.metric("Address Class", f"Class {result_class}")
        col2.metric("Default Mask", f"{default_mask}")

        if note:
            st.info(note)

    except ValueError:
        # Show an error if the input is not a valid IP
        st.error("Invalid Input: Please enter a single, valid IPv4 address (e.g., 192.168.1.1).")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")