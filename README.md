# Nmap injected into SQLite3 database that's shown in an HTML format
!!! This is a running project. !!!!

(I'm running this inside of a Ubuntu VM)

Tools needed:
```sudo apt install python3 python3-pip nmap git -y ```
DONT FORGET FLASK
```pip install Flask```

Then, we need to clone the repo.

```git clone https://github.com/bwithe/nmap-db```

Once you've done that, make sure you see the script ```nmap-db.py``` and the ```/templates``` directory.

Run the ```nmap-db.py``` with the following command ```python3 nmap-db.py```.

This will prompt for user input on which IP/s you'd like to scan.

Once it's finished, a Flask server will pull the information from the SQLite3 database and host it in HTML format.

Go to the following address when it says ```http://127.0.0.1:5000```

Like I said before, this is a running project. I plan on building my own type of dashboard using SQLite3's database.


