from enum import Enum
from random import choice


class Technology(Enum):
    SOFTWARE = "Software"
    HARDWARE = "Hardware"
    AI = "Artificial Intelligence"
    BIG_DATA = "Big Data"
    CLOUD_COMPUTING = "Cloud Computing"
    CYBERSECURITY = "Cybersecurity"

class Finance(Enum):
    BANKING = "Banking"
    INVESTMENT = "Investment"
    INSURANCE = "Insurance"
    CRYPTOCURRENCY = "Cryptocurrency"

class Healthcare(Enum):
    PHARMACEUTICALS = "Pharmaceuticals"
    BIOTECHNOLOGY = "Biotechnology"
    MEDICAL_DEVICES = "Medical Devices"
    TELEMEDICINE = "Telemedicine"

class Industry(Enum):
    MANUFACTURING = "Manufacturing"
    AUTOMOTIVE = "Automotive"
    AEROSPACE = "Aerospace"
    ENERGY = "Energy"
    RENEWABLES = "Renewable Energy"
    MINING = "Mining"

class Retail(Enum):
    ECOMMERCE = "E-Commerce"
    FASHION = "Fashion"
    FOOD_BEVERAGE = "Food & Beverage"

class Media(Enum):
    GAMING = "Gaming"
    FILM_TV = "Film & TV"
    MUSIC = "Music"

class PublicSector(Enum):
    EDUCATION = "Education"
    GOVERNMENT = "Government"
    NON_PROFIT = "Non-Profit Organizations"
    MILITARY_DEFENSE = "Military & Defense"

class Transportation(Enum):
    LOGISTICS = "Logistics"
    SHIPPING = "Shipping"
    AIRLINES = "Airlines"
    RAILWAYS = "Railways"

class RealEstate(Enum):
    CONSTRUCTION = "Construction"
    URBAN_PLANNING = "Urban Planning"

class CompanySize(Enum):
    MICRO = "Micro"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    ENTERPRISE = "Enterprise"

class MarketSectors(Enum): 
    TECHNOLOGY = Technology
    FINANCE = Finance
    HEALTHCARE = Healthcare
    INDUSTRY = Industry
    RETAIL = Retail
    MEDIA = Media
    PUBLIC_SECTOR = PublicSector
    TRANSPORTATION = Transportation
    REAL_ESTATE = RealEstate

class Sector():
    """contains the sector of the action"""

    def __init__(self, major_sector=None,minor_sector = None ,company_size=None):
        self.major_sector = major_sector
        self.minor_sector = minor_sector
        self.company_size = company_size
        self.generate_random_sector()
        
    
    def generate_random_sector(self):
        """generate random sector for the action"""
        if self.major_sector is None or  type(self.major_sector) is not MarketSectors:
            self.major_sector = choice(list(MarketSectors))
        if self.minor_sector is None or type(self.minor_sector) is not MarketSectors:
            self.minor_sector = choice(list(MarketSectors))
        if self.company_size is None or type(self.company_size) is not CompanySize:
            self.company_size = choice(list(CompanySize))

    