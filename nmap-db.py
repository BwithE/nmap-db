import xml.etree.ElementTree as ET
import sqlite3
import os
from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)

# Get ready to fetch Nmap results from the database, duh! 🤷
def get_nmap_results(search_query=None):
    connection = sqlite3.connect('nmap.db')  # Like, where our database lives, dude!
    cursor = connection.cursor()

    # Update the SQL query based on the search query - Cowabunga SQL magic!
    if search_query:
        cursor.execute('SELECT * FROM nmap_results WHERE ip LIKE ? OR service LIKE ?',
                       ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute('SELECT * FROM nmap_results')

    nmap_results = cursor.fetchall()
    connection.close()
    return nmap_results

# Time to render the HTML template, bro! 🤘
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    nmap_results = get_nmap_results(search_query)
    return render_template('index.html', nmap_results=nmap_results, search_query=search_query)

def run_nmap_scan(ip_list):
    # Path to SQLite database file - Let's stash our data, dude!
    db_path = 'nmap.db'

    # Check if the database file already exists - Like, cleanup the old stuff!
    if os.path.exists(db_path):
        os.remove(db_path)

    # Connect to SQLite database - Time to chill with some SQL action!
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table for Nmap results - Let's party with a new table!
    cursor.execute('''
        CREATE TABLE nmap_results (
            id INTEGER PRIMARY KEY,
            ip TEXT,
            port INTEGER,
            service TEXT,
            protocol TEXT,
            version TEXT
        );
    ''')

    # Commit changes to create the table - Database is ready to roll!
    conn.commit()

    # Iterate through the specified IPs and run Nmap - Surfing the network waves, dude!
    for ip in ip_list:
        # Run Nmap command and save results to XML file - Time for some digital exploration!
        nmap_command = f'nmap -p- -n -Pn -sV {ip} -oX scan.xml'
        os.system(nmap_command)

        # Parse the Nmap XML file - Unleash the power of XML, dude!
        tree = ET.parse('scan.xml')
        root = tree.getroot()

        # Iterate through the XML and insert data into the SQLite database - Data, get in my database!
        for host in root.findall('.//host'):
            ip = host.find('address').get('addr')
            for port in host.findall('.//port'):
                port_number = port.get('portid')
                service = port.find('.//service').get('name')
                protocol = port.get('protocol')
                version = port.find('.//service').get('version')

                # Insert data into the SQLite database - SQL party time!
                cursor.execute("INSERT INTO nmap_results (ip, port, service, protocol, version) VALUES (?, ?, ?, ?, ?)",
                               (ip, port_number, service, protocol, version))

    # Commit changes and close the connection - Database, drop the mic!
    conn.commit()
    conn.close()

    print(f"Nmap results imported into {db_path}")

# Run Nmap scan for user-provided IPs - Asking the user for a digital treasure hunt!
ip_list_str = input("Enter the IPs to scan (comma-separated): ")
ip_list = ip_list_str.split(',')
run_nmap_scan(ip_list)

# Clearing terminal - Making space for some digital awesomeness!
def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

# Usage - Like, clean slate, dude!
clear_terminal()

# Run Flask web application - It's web-slinging time, Spidey style!
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
#    webbrowser.open_new('http://127.0.0.1:5000/')  # Open default web browser

# After the browser is closed, remove the created files - Cleanup time, digital janitor!
os.remove('scan.xml')
os.remove('nmap.db')
