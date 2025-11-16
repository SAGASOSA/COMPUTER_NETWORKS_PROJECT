import streamlit as st
import ipaddress
import pandas as pd

# Page configuration
st.set_page_config(page_title="Subnet Visualizer", page_icon="🧮")
st.title("🧮 Subnetting Visualizer")
st.caption("This tool takes a large network and divides it into smaller, equal-sized subnets.")

# --- Input Fields ---
base_network_input = st.text_input(
    "Enter a base network to divide",
    placeholder="e.g., 10.0.0.0/8"
)

if not base_network_input:
    st.info("Please enter a base network to begin.")
    st.stop() # Stop executing the rest of the script

# --- Calculation Logic ---
try:
    # 1. Parse the base network
    base_network = ipaddress.ip_network(base_network_input, strict=False)
    
    st.success(f"Base network: **{base_network}**")
    
    # 2. Create a slider for the new prefix
    # The new prefix must be larger than the base prefix and at most 30
    # (A /31 or /32 isn't useful for "networks of hosts")
    new_prefix = st.slider(
        "Select the new prefix length for your subnets",
        min_value=base_network.prefixlen + 1, # Can't be smaller than the base
        max_value=30,
        value=base_network.prefixlen + 2 # A sensible default
    )
    
    # 3. Calculate the subnets
    # This is the core function from the ipaddress library
    subnet_generator = base_network.subnets(new_prefix=new_prefix)
    
    # 4. Prepare data for the table
    subnet_list = []
    for subnet in subnet_generator:
        usable_hosts = max(0, subnet.num_addresses - 2)
        subnet_list.append({
            "Network ID": str(subnet.network_address),
            "CIDR Notation": str(subnet.with_prefixlen),
            "Subnet Mask": str(subnet.netmask),
            "First Host": str(list(subnet.hosts())[0]) if usable_hosts > 0 else "N/A",
            "Last Host": str(list(subnet.hosts())[-1]) if usable_hosts > 0 else "N/A",
            "Broadcast": str(subnet.broadcast_address),
            "Usable Hosts": usable_hosts
        })

    # 5. Display the summary
    st.subheader(f"Results: `{base_network}` divided into `/{new_prefix}` networks")
    st.metric(
        label="Total Subnets Created",
        value=f"{len(subnet_list):,}" # Format number with commas
    )
    st.metric(
        label="Usable Hosts per Subnet",
        value=f"{subnet_list[0]['Usable Hosts']:,}"
    )
    
    # 6. Display the data in a table
    st.subheader("Subnet Table")
    # Use pandas DataFrame for a rich, sortable table
    df = pd.DataFrame(subnet_list)
    st.dataframe(df, use_container_width=True)

except ValueError as e:
    st.error(f"Invalid Network: {e}. Please use CIDR notation (e.g., 192.168.0.0/16).")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")