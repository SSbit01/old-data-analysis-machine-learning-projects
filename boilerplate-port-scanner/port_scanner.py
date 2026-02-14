import socket, common_ports, re


def get_open_ports(target, port_range, verbose=False):
  is_url = re.search("[a-zA-Z]", target)

  try:
    ip = socket.gethostbyname(target)
  except:
    if is_url:
      return "Error: Invalid hostname"
    return "Error: Invalid IP address"

  open_ports = []
  
  for i in range(port_range[0], port_range[1] + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if not s.connect_ex((ip, i)):
      open_ports.append(i)
    s.close()

  if verbose:
    t_ip = ""
    if is_url:
      t_ip = f"{target} ({ip})"
    else:
      try:
        t_ip = f"{socket.gethostbyaddr(target)[0]} ({target})"
      except:
        t_ip = target
    output = f"Open ports for {t_ip}\nPORT     SERVICE"
    for i in open_ports:
      spaces = " " * (9 - len(str(i)))
      output += f"\n{i}{spaces}{common_ports.ports_and_services[i]}"
    return output
    
  return open_ports