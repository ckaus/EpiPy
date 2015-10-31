# EpiPy
A Tool for fitting epidemic models. The supported models are:

 - [ ] SIR

This is tool is being developed under the [MIT license][1] for the course [Softwareprojekt Mobilkommunikation][2] at the [Freie Universität Berlin][3]. 

## Installation

 1. Download the project: 
    `$ git clone git@github.com:ckaus/EpiPy.git`
 2. Install the libraries:
    `$ sudo pip install -r requirements.txt`
    Note: you need `pip` on your computer
 3. Go to your terminal and open the pspql bash:
    `$ sudo -u postgres psql postgres`
 4. Create a new database
    `$ postgres=# CREATE DATABASE epiDB OWNER postgres;`
 5. Change the password for user postgres in psql bash:
    `$ ALTER USER Postgres WITH PASSWORD 'postgres';`
    Note: the user and password must be same like in the `config.cfg`

## Requirements
 * Python 2.7.9
 * psycopg2

## Introduction

## Examples

## What's new
 * 20151310: Project start

[1]: https://github.com/ckaus/EpiPy/blob/master/LICENSE 		"MIT license"         
[2]: http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html  "Course"
[3]: http://www.fu-berlin.de/en/index.html 						"FU Berlin"
