from enum import Enum
from market_sector import MarketSectors
from random import choice, randint


class NameGenerator:
    def __new__(cls):
        raise TypeError("NameGenerator is a utility class and cannot be instantiated directly.")

    pre_names = [
    "Global", "Omni", "Neo", "Prime", "NextGen", "Hyper", "Ultra", "Apex", "Core", "Meta",
    "Infinity", "Quantum", "Vertex", "Pioneer", "Synergy", "Vision", "Elite", "True", "Smart", "Future",
    "Everest", "Titan", "Dynamic", "Epic", "Vanguard", "Nova", "Integral", "Evolve", "Stellar", "Peak",
    "Bold", "Summit", "Trust", "Nexus", "Horizon", "Legacy", "Endeavor", "Momentum", "Astral", "Unity"
    ]

    sector_names = {
    MarketSectors.TECHNOLOGY: {
        "first_names": ["Cyber", "Quantum", "Nano", "Info", "Data", "Code", "Tech", "AI", "Neural", "Virtual"],
        "second_names": ["Systems", "Solutions", "Soft", "Logic", "Labs", "Cloud", "Security", "Network", "Dynamics", "Innovations"]
    },
    MarketSectors.FINANCE: {
        "first_names": ["Capital", "Wealth", "Trust", "Prime", "Gold", "Secure", "Invest", "Apex", "Ledger", "Equity"],
        "second_names": ["Bank", "Partners", "Advisors", "Holdings", "Funds", "Strategies", "Credit", "Ventures", "Assets", "Growth"]
    },
    MarketSectors.HEALTHCARE: {
        "first_names": ["Med", "Bio", "Pharma", "Health", "Care", "Life", "Neo", "Vital", "Gen", "Cure"],
        "second_names": ["Solutions", "Sciences", "Labs", "Biotech", "Research", "Clinics", "Innovations", "Genetics", "Therapy", "Diagnostics"]
    },
    MarketSectors.INDUSTRY: {
        "first_names": ["Steel", "Auto", "Power", "Titan", "Global", "Omni", "Construct", "Aero", "Heavy", "Forge"],
        "second_names": ["Manufacturing", "Works", "Energy", "Mechanics", "Engineering", "Dynamics", "Mining", "Metals", "Systems", "Builders"]
    },
    MarketSectors.RETAIL: {
        "first_names": ["Shop", "Trend", "Style", "Fresh", "Smart", "Quick", "Ezy", "Pure", "Happy", "Buy"],
        "second_names": ["Mart", "Store", "Outlet", "Bazaar", "Commerce", "Wear", "Goods", "Supplies", "Fashion", "Market"]
    },
    MarketSectors.MEDIA: {
        "first_names": ["Vision", "Sound", "Epic", "Pixel", "Mega", "Bright", "Creative", "Nova", "Bold", "Prime"],
        "second_names": ["Studios", "Films", "Records", "Games", "Media", "Network", "Productions", "Streaming", "Content", "Digital"]
    },
    MarketSectors.PUBLIC_SECTOR: {
        "first_names": ["Civic", "Nation", "Edu", "Gov", "Social", "Public", "Future", "Global", "Common", "Liberty"],
        "second_names": ["Trust", "Services", "Foundation", "Network", "Outreach", "Initiative", "Policy", "Alliance", "Program", "Support"]
    },
    MarketSectors.TRANSPORTATION: {
        "first_names": ["Aero", "Speed", "Move", "Glide", "Flow", "Rapid", "Sky", "Terra", "Hyper", "Metro"],
        "second_names": ["Logistics", "Transport", "Freight", "Lines", "Express", "Shipping", "Trucking", "Rail", "Airways", "Routes"]
    },
    MarketSectors.REAL_ESTATE: {
        "first_names": ["Urban", "Metro", "City", "Skyline", "Prime", "Home", "Elite", "Capital", "Brick", "Land"],
        "second_names": ["Developers", "Properties", "Realty", "Construction", "Estates", "Management", "Architecture", "Investments", "Rentals", "Projects"]
    }
    }

    sufixes = [
    "Corp", "Inc", "Ltd", "Group", "Co", "LLC", "PLC", "AG", "SA", "Pty"
    ]

    @staticmethod
    def generate_name(major_sector):
        """
        Generate a random company name based on the major and minor sectors.
        Args:
            major_sector (str): The major sector of the company.
        Returns:
            str: A randomly generated company name.
        """
        
        if major_sector not in NameGenerator.sector_names:
            raise ValueError(f"Unknown major sector: {major_sector}")

        first_name = choice(NameGenerator.sector_names[major_sector]["first_names"])
        second_name = choice(NameGenerator.sector_names[major_sector]["second_names"])

        # the pre name and sufix have a 20% chance to be added to the name
        if randint(1, 5) == 1:
            pre_name = choice(NameGenerator.pre_names)
        else: pre_name = ""
        
        if randint(1, 5) == 1:
            sufix = choice(NameGenerator.sufixes)
        else: sufix = ""

        name = f"{first_name} {second_name}"
        if pre_name:
            name = f"{pre_name} {name}"
        if sufix:
            name = f"{name} {sufix}"
        return name.strip()
    
    def action_ticker(name):
        """
        Creates a ticker value for the action name.
        This is used to create a unique ID for the action.
        Args:
            name (str): The name of the action.
        Returns:
            str: a 3 digit string representing the ticker value of the name.
        """

        ticker = ""

        # Get the first letter of each word in the name
        for word in name.split():
            if len(ticker) < 3:
                ticker += word[0].upper()
            else:
                break
        # If the ticker is less than 3 characters, add the second letter of the last word
        while len(ticker) < 3:
            ticker += word[1].upper()
        # if the ticker is more than 3 characters, truncate it
        if len(ticker) > 3:
            ticker = ticker[3:]

        # we now add a hash to the ticker to make it unique
        ticker += str((hash(name) % 900) + 100)

        return ticker




    
