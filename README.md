Travis CI Testing status:
![alt text](https://travis-ci.org/RcdFdz/secrets-manager-3.svg?branch=master "Test status")

### Password Manager
The aim to the present project is to solve the shared secrets problem in small teams.

### How to install
It is necessary to install GPG Suite version 2016.07 (https://gpgtools.org/) or greater. And import a key pair sec/pub keys to GPG Keychain or generate them with the GPG Suite.

Once the previus requirements are satisfied will be necessary to copy a public key into the `pub-keys` folder, otherwise the application cannot work.

If your team is allready working with secrets-manager someone from the team will have to update the `secrets` file with your key.

### How it works
The Secrets Manager can be run in two modes, by using an interactive mode or by using the command line.

The first time that Secrets Manager there are only two options available, _Add a key/Value Pair_ by interactive mode or by command line arguments.

Once there is at least one secret, the application allows to work with an small CRUD in interactive mode.

The menu accepts:
* Add Key/Value Pair
* Modify/Delete Key/Value Pair
* Decrypt Key/Value Pair
* Show Keys
* Update public keys
* Exit

Command line outputs first time it runs:
```
➜  secrets-manager-3 git:(master) ✗ python3 main.py -h
usage: main.py [-h] [-i] [-ak identifier {"user":"<user>", ...}]

Manager for sensible information under PGP. Use -i/--interactive or
-ak/--addkey to introduce your first key and for more option will be
displayed.

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     display the interactive menu for pwd-manager
  -ak identifier {"user":"<user>", ...}, --addkey identifier {"user":"<user>", ...}
                        add element to secrets, second argument must be a
                        valid json string. Allowed keys user, password, url
                        and other
```
Command line outputs when keys exist:
```
➜  secrets-manager-3 git:(master) ✗ ./main.py -h
usage: main.py [-h] [-i] [-l] [-u identifier] [-p identifier] [-ur identifier]
               [-o identifier] [-a identifier]
               [-ak identifier {"user":"<user>", ...}]
               [-mk identifier {"user":"<new_user>", ...}]
               [-mi old_identifier new_identifier] [-d identifier]

Manager for sensible information under PGP

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     display the interactive menu for pwd-manager
  -l, --list            list all the stored identifiers
  -u identifier, --user identifier
                        return the username for the given identifier
  -p identifier, --password identifier
                        return the password for the given identifier
  -ur identifier, --url identifier
                        return the URL for the given identifier
  -o identifier, --other identifier
                        return the other for the given identifier
  -a identifier, --all identifier
                        display all values for the given identifier
  -ak identifier {"user":"<user>", ...}, --addkey identifier {"user":"<user>", ...}
                        add element to secrets, second argument must be a
                        valid json string. Allowed keys user, password, url
                        and other
  -mk identifier {"user":"<new_user>", ...}, --modkey identifier {"user":"<new_user>", ...}
                        modify element to secrets, second argument must be a
                        valid json string. Allowed keys user, password, url
                        and other
  -mi old_identifier new_identifier, --modid old_identifier new_identifier
                        modify id from an element
  -d identifier, --delete identifier
                        modify element to secrets, second argument must be a
                        valid json string
```
### Requirements
This projects requires python3 and GPG Suite version 2016.07 (https://gpgtools.org/) or greater.

Also will be required to run `pip3 install -r requirements.txt`.

### TODO

* Add option to modify Identifier
* Add option to add directly from command a key/value/note
* Modify ONLY identifier/key/value/note should be an option
