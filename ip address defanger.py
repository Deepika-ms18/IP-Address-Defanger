def defang_ip_address(ip_address):
    defanged_address = '[.]'.join(ip_address.split('.'))
    return defanged_address
ip_address = input("Enter the IP Address: ")
defanged_ip = defang_ip_address(ip_address)
print(f"Original IP Address: {ip_address}")
print(f"Defanged IP Address: {defanged_ip}")