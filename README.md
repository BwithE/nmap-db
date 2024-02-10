# Nmap injected into SQLite3 database that's shown in an HTML format
!!! This is a running project !!!!

![image](https://github.com/BwithE/nmap-db/assets/144924113/5ebe5cbe-ebda-4008-baaa-790b490a00b2)

Tools needed:
```sudo apt install python3 python3-pip nmap git -y ```
DONT FORGET FLASK
```pip install Flask```

Then, we need to clone the repo.

```git clone https://github.com/bwithe/nmap-db```

Once you've done that, make sure you see the script ```nmap-db.py``` and the ```/templates``` directory.

Run the ```nmap-db.py``` with the following command ```python3 nmap-db.py```.

This will prompt for user input on which IP/s you'd like to scan.

The nmap.xml results will be placed into the SQLite3 nmap.database.

Then, Flask will pull the information from the SQLite3 database and host it in HTML format.

The ```/templates``` directory has an index.html that gets called and is needed by default for Flask.

After, you can go to the following address ```http://127.0.0.1:5000```

Like I said before, this is a running project. I plan on building my own type of dashboard using SQLite3's database.

This Python script integrates the Nmap network scanning tool with a Flask web application to facilitate the scanning and visualization of network service information. The script performs the following tasks:

# Nmap Scanning and Database Population:

It defines a function run_nmap_scan(ip_list) that takes a list of IP addresses as input.
For each IP address in the provided list, it runs an Nmap scan (nmap -p- -n -Pn -sV {ip} -oX scan.xml), which scans all ports (-p-), performs host discovery without DNS resolution (-n -Pn), and performs version detection (-sV), saving the results to an XML file (scan.xml).
The script then parses the XML file to extract information about discovered hosts, ports, services, and versions.
It creates or connects to a SQLite database (nmap.db) and creates a table (nmap_results) to store the extracted information.
For each host and its associated ports and services, it inserts the information into the SQLite database.
Web Interface:

It defines a Flask web application with a single route (/) that renders an HTML template (index.html) to display the Nmap scan results.
The route handler allows searching within the Nmap results based on IP address or service name.
The search functionality is implemented by passing a search query via the URL parameter search.
The web application dynamically updates the displayed results based on the search query.
User Interaction:

After defining the functions and setting up the web application, the script prompts the user to input a comma-separated list of IP addresses to scan.
It then initiates the Nmap scan and database population process using the provided IP addresses.
Cleanup:

Once the Flask web application is stopped (usually by closing the browser), the script removes the temporary files (scan.xml and nmap.db) created during the scanning and database population process.

# Usage:

Execute the script in a Python environment.
Input a comma-separated list of IP addresses to scan when prompted.
The script will perform Nmap scans on the specified IP addresses, store the results in a SQLite database, and launch a Flask web application.
Open a web browser and navigate to http://127.0.0.1:5000/ to view the scan results.
Optionally, search for specific IP addresses or service names using the search functionality provided in the web interface.
Once done, close the browser to stop the Flask application.
The script will automatically clean up temporary files generated during the scanning process.


