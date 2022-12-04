import socket

# Define the list of domains to check
domains = ["example.com", "example.net", "example.org"]

# Iterate through the list of domains
for domain in domains:
    # Check if the domain is available
    try:
        # Attempt to resolve the domain
        socket.gethostbyname(domain)
    except socket.gaierror:
        # Domain is available if an error is raised
        print(f"{domain} is available")
    else:
        # Domain is not available if no error is raised
        print(f"{domain} is not available")
