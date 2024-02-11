import os
import requests
from bs4 import BeautifulSoup

from logging import getLogger

logger = getLogger(__name__)

class sdn():
    """ SDN List class
    """
    def __init__(self, url="https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml"):
      # Initialize the SDN class with default or provided URL
      self.url = url
      self.soup = self.__get_xml_soup()
      self.party_sub_type_id = {"3": "Entity", "4": "Individual"}
      self.date_of_issue = {'date_of_issue': self.__parse_issue_date()}

    def __get_xml_soup(self):
        # Get the XML data as a BeautifulSoup object
        if os.path.exists(self.url):
            return self.__load_xml(self.url)
        else:
            return self.__download_xml(self.url)

    def __load_xml(self, file_path):
        # Load XML from a file
        try:
            with open(file_path, 'r') as file:
                contents = file.read()
            return BeautifulSoup(contents, "xml")
        except Exception as e:
            logger.error(f"Error occurred while loading XML file: {e}")
            raise SystemExit(f"Failed to load XML file: {file_path}") from e

    def __download_xml(self, url):
        # Download XML from a URL
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, "xml")
        except requests.exceptions.RequestException as exp:
            logger.error(f"Request to {url} failed: {exp}")
            raise SystemExit(f"Request to {url} has been failure") from exp

    def __parse_issue_date(self):
        # Parse the issue date from the XML
        date_of_issue = self.soup.find('DateOfIssue')
        return f"{date_of_issue.find('Year').text}-{date_of_issue.find('Month').text.zfill(2)}-{date_of_issue.find('Day').text.zfill(2)}"
    
    def __get_profiles(self, party_sub_type_id):
        # Get profiles matching the specified party_sub_type_id
        return self.soup.select(f'Profile[PartySubTypeID="{party_sub_type_id}"]')

    def individual_list(self):
        # Generate a list of individuals
        temp_list = []
        for profile in self.__get_profiles("4"):
            profile_id = profile.get('ID')
            for names in profile.select('Alias DocumentedName'):
                name_parts = names.select('DocumentedNamePart NamePartValue[ScriptID="215"]')
                if len(name_parts) >= 2:
                    first_name = name_parts[0].text
                    last_names = ' '.join(part.text for part in name_parts[1:])
                    temp_list.append({"profile_id": profile_id,"first_name": first_name, "last_name": last_names})
        return temp_list

    def organization_list(self):
        # Generate a list of organizations
        temp_list = []
        for profile in self.__get_profiles("3"):
            profile_id = profile.get('ID')
            for name in profile.select('Alias DocumentedName DocumentedNamePart NamePartValue[ScriptID="215"]'):
                organization_name = name.text
                temp_list.append({"profile_id": profile_id, "organization_name": organization_name})
        return temp_list