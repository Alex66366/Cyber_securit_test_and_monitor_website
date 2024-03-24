import argparse
from scapy.sendrecv import AsyncSniffer
#from .flow_session import generate_session_class
from flow_session import generate_session_class

def create_sniffer(input_file, input_interface, output_mode, output_file, url_model=None):
    assert (input_file is None) ^ (input_interface is None)
    NewFlowSession = generate_session_class(output_mode, output_file, url_model)
    return AsyncSniffer(
        iface=input_interface,
        filter="ip and (tcp or udp)",
        prn=None,
        session=NewFlowSession,
        store=False,
    )

# def main():
#     input_interface = "Intel(R) Wi-Fi 6E AX211 160MHz"
#     output_file = "output.csv"
#     output_mode = "flow"
#     url_model = None
#
#     sniffer = create_sniffer(None, input_interface, output_mode, output_file, url_model)
#     sniffer.start()
#
#     try:
#         sniffer.join()
#         captured_packets = sniffer.results
#         if captured_packets:
#             last_packet = captured_packets[-1]
#             last_packet.show()
#     except KeyboardInterrupt:
#         sniffer.stop()
#     finally:
#         sniffer.join()

# if __name__ == "__main__":
#     main()
