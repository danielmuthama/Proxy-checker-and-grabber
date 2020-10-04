from proxy_grabber import ProxyGrabber
grabber = ProxyGrabber()

# --- For Grabbing proxies ---

# Parsing proxy from different sources
grabber.grab_proxies(proxy_limit=90)

# --- Adding proxies ---
# Also: you can add proxies without grabbing
# You can add some proxies from the file
grabber.load('./data/proxy.list')

# adding proxy manually
grabber.add_proxies(['ip:port', 'ip:port', ...])

# --- Checking proxies ---

# You can specify proxy countries
grabber.set_countries(['US', 'RU', 'CA', ...])

grabber.check_proxies()

# --- Results ---
# Random checked proxy
grabber.get_proxy() 
 # All checked proxies
grabber.get_checked_proxies()
 # Save checked proxies to the file
grabber.save('./data/checked_proxies.list')
