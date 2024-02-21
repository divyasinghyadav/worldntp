import streamlit as st
import ntplib
import threading
import time
import matplotlib.pyplot as plt

# Function to query NTP server and return offset and delay


def get_offset_and_delay_from_otherntp(server2):
    ntp_client2 = ntplib.NTPClient()
    try:
        response2 = ntp_client2.request(server2)
        offset = response2.offset
        delay = response2.delay
        processing_time = response2.tx_time - response2.recv_time
        return offset, delay, processing_time
    except ntplib.NTPException as e:
        st.error(f"Error querying NTP server {server2}: {e}")
        return 0, 0, 0

def main():
    
    col1, col2, col3 = st.columns([1, 8, 1])  # Divide the row into three columns with different widths

    with col1:
        st.image("csir_logo.png", width=150)

    with col2:
        # Center the title horizontally
        #st.markdown("<h1 style='text-align: center;'>CSIR-NPL</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>Developed by CSIR-NPL<br>NTP Servers Status worldwide</h1>", unsafe_allow_html=True)

    with col3:
        st.image("npl_logo.png", width=150)
     
    # List of NTP servers
    other_ntp_servers = [
        'time.nplindia.org', 'time.nplindia.in',
          '14.139.60.103', '14.139.60.106', '14.139.60.107',
        'samay1.nic.in', 'samay2.nic.in', '103.165.30.244', 
        'time.nist.gov', 'time.google.com', 'uk.pool.ntp.org', 'time.windows.com',
        'ptbtime1.ptb.de',  
    ]

    # Create lists to store server data
    other_server_names = []
    offsets2 = []
    delays2 = []
    processing_time2 = []

    # Query each NTP server and store the results
    for server2 in other_ntp_servers:
        offset, delay, processing_time = get_offset_and_delay_from_otherntp(server2)
        other_server_names.append(server2)
        offsets2.append(offset)
        delays2.append(delay)
        processing_time2.append (processing_time)


    # Display results
    #st.write("Server Offset and Delay:")
    #results = list(zip(server_names, offsets, delays))
    #for server, offset, delay in results:
       # st.write(f"Server: {server}, Offset: {offset}, Delay: {delay}")
        

    # Plot server offset
    plt.figure(figsize=(12, 6))
    plt.bar(other_server_names, offsets2, color='green', alpha=0.7, label='Offset')
    plt.xlabel('Private IP of the NTP servers world wide', fontsize=16, fontweight='bold')
    plt.ylabel('Offset (seconds)',fontsize=16, fontweight='bold')
    plt.title('NTP Servers Offset worldwide',fontsize=20, fontweight='bold')
    plt.yticks(fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right',fontsize=14, fontweight='bold')
    st.pyplot(plt)

    # Plot server delay
    plt.figure(figsize=(12, 6))
    plt.bar(other_server_names, delays2, color='blue', alpha=0.7, label='Delay')
    plt.xlabel('private IP of the NTP Servers world wide', fontsize=16, fontweight='bold')
    plt.ylabel('Delay (seconds)',fontsize=16, fontweight='bold')
    plt.title('NTP Servers Delay',fontsize=20, fontweight='bold')
    plt.xticks(rotation=45, ha='right',fontsize=14, fontweight='bold')
    plt.yticks(fontsize=14, fontweight='bold')
    st.pyplot(plt)
    
    
    # Plot server processing time
    plt.figure(figsize=(12, 6))
    plt.bar(other_server_names, processing_time2, color='pink', alpha=0.7, label='Offset')
    plt.xlabel('Private IP of the NTP servers world wide', fontsize=16, fontweight='bold')
    plt.ylabel('processing time (seconds)',fontsize=16, fontweight='bold')
    plt.title('NTP Servers processing time worldwide',fontsize=20, fontweight='bold')
    plt.yticks(fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right',fontsize=14, fontweight='bold')
    st.pyplot(plt)

if __name__ == "__main__":
    main()
     #streamlit run ntp_app2.py 