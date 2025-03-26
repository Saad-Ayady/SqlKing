from colorama import Fore, Style, init

init(autoreset=True)
class Panels:
    def __init__(self):
        self.name = "SQLKing"
    def panel(self):
        pan = (r"""
  {GREEN}{BOLD}        .-'''/.\
  {GREEN}{BOLD}       (_.--'  |
  {GREEN}{BOLD}        |  ==  |       {RED}   ____   __   __    __ _  __  __ _   ___ 
  {GREEN}{BOLD}   o-._ .--..--. _.-o  {RED}  / ___) /  \ (  )  (  / )(  )(  ( \ / __)
  {GREEN}{BOLD}       |   ||   |      {RED}  \___ \(  O )/ (_/\ )  (  )( /    /( (_ \
  {GREEN}{BOLD}        ;--|`--:       {RED}  (____/ \__\)\____/(__\_)(__)\_)__) \___/
  {GREEN}{BOLD}        |. |   |
  {GREEN}{BOLD}        |  ;_ .|        {WHITE} Tool Name {YELLOW}:{WHITE} SQLKing
  {GREEN}{BOLD}        |_____ |        {WHITE} Version   {YELLOW}:{WHITE} 1.0
  {GREEN}{BOLD}       /|     '|\       {WHITE} Author    {YELLOW}:{WHITE} D3 D00M
  {GREEN}{BOLD}       //`----'\\       {WHITE} Description: {YELLOW}*---------------------------------------------------------------------------------------------* 
  {GREEN}{BOLD}      ////|  |  \\                {YELLOW}   |{WHITE} A tool developed by Dr. Doom, specifically designed to assist attackers in conducting        {YELLOW} |
  {GREEN}{BOLD}      /   |  |    \               {YELLOW}   |{WHITE} cyberattacks against a targeted country or specific entities. The tool's primary role        {YELLOW} |
  {GREEN}{BOLD}         /|  |\                   {YELLOW}   |{WHITE} is to help these attackers identify multiple vulnerable targets within a specific region     {YELLOW} |
  {GREEN}{BOLD}        / \  / \                  {YELLOW}   |{WHITE} without having to manually test each one individually. We chose **SQL Injection (SQLi)       {YELLOW} |
  {GREEN}{BOLD}       /   \/   \                 {YELLOW}   |{WHITE} vulnerabilities** due to their ease of exploitation and significant potential impact, making {YELLOW} |
  {GREEN}{BOLD}      /          \                {YELLOW}   |{WHITE} them highly valuable for attackers. In future releases, we will add several new techniques   {YELLOW} |
  {GREEN}{BOLD}      |          |                {YELLOW}   |{WHITE} to make the tool more comprehensive and enhance its capabilities for executing such attacks. {YELLOW} |
  {GREEN}{BOLD}     ||    /\    ||               {YELLOW}    *---------------------------------------------------------------------------------------------*
  {GREEN}{BOLD}     ||   ,  .   || {RED}D3 D00M <3
  """).format(
            GREEN=Fore.GREEN, BOLD=Style.BRIGHT, RED=Fore.RED,
            WHITE=Fore.WHITE, YELLOW=Fore.YELLOW
        )
        return pan
    def get_name(self):
        return self.name
    def get_version(self):
        return "1.0"
    def get_author(self):
        return "Dr D3V1L"
    def get_description(self):
        return ("""
A tool developed by Dr. Doom, specifically designed to assist attackers in conducting cyberattacks against a targeted country or specific entities.  
The tool's primary role is to help these attackers identify multiple vulnerable targets within a specific region without having to manually test each one individually.  
We chose **SQL Injection (SQLi) vulnerabilities** due to their ease of exploitation and significant potential impact, making them highly valuable for attackers.  
In future releases, we will add several new techniques to make the tool more comprehensive and enhance its capabilities for executing such attacks.""")
    def get_license(self):
        return "MIT"
    def get_last_update(self):
        return "2025-03-26"
    def get_help(self):
        return """
Usage: python3 sqlking.py <DORK> (MAX PAGES)"
    ex : python3 sqlking.py 'inurl:".php?id=" site:".dz"' 200
    ex : python3 sqlking.py 'inurl:".php?id=" site:".dz"'
"""