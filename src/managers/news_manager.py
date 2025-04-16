from src.toolkit.market_sector import *
from random import choice, randint
from textwrap import wrap


class NewsManager:
    """
    This class manages the news in the game.
    It generates daily news 
    """

    minor_sector_news = {
    # Technology
    Technology.SOFTWARE: {
        "up": "New programming language boosts developer productivity worldwide.",
        "down": "Major security flaw discovered in popular software platforms."
    },
    Technology.HARDWARE: {
        "up": "Breakthrough in semiconductors reduces costs and boosts chip performance.",
        "down": "Global component shortage halts hardware production."
    },
    Technology.AI: {
        "up": "New AI model surpasses benchmarks in cognitive tasks.",
        "down": "Data breach raises concerns about enterprise AI adoption."
    },
    Technology.BIG_DATA: {
        "up": "Corporations embrace big data to streamline internal processes.",
        "down": "New privacy regulation limits mass data collection."
    },
    Technology.CLOUD_COMPUTING: {
        "up": "Remote work demand drives cloud computing growth.",
        "down": "Massive cloud outage causes global business disruption."
    },
    Technology.CYBERSECURITY: {
        "up": "Spike in cyberattacks boosts demand for security solutions.",
        "down": "Critical vulnerability discovered in top cybersecurity software."
    },

    # Finance
    Finance.BANKING: {
        "up": "Rising interest rates increase banking sector profits.",
        "down": "Money laundering scandal shakes public trust in banks."
    },
    Finance.INVESTMENT: {
        "up": "Foreign capital inflow energizes the investment market.",
        "down": "Market volatility hits mutual funds and investor confidence."
    },
    Finance.INSURANCE: {
        "up": "High demand for life and health insurance pushes sector growth.",
        "down": "Natural disasters overwhelm insurance companies with claims."
    },
    Finance.CRYPTOCURRENCY: {
        "up": "Friendly regulation accelerates institutional crypto adoption.",
        "down": "Major crypto exchange hack shatters investor confidence."
    },

    # Healthcare
    Healthcare.PHARMACEUTICALS: {
        "up": "FDA approval of new drug revolutionizes chronic disease treatment.",
        "down": "Drug recall hits pharmaceutical stock prices."
    },
    Healthcare.BIOTECHNOLOGY: {
        "up": "Genetic technology shows promising results in clinical trials.",
        "down": "Biotech startup struggles after failed clinical phase."
    },
    Healthcare.MEDICAL_DEVICES: {
        "up": "New wearable medical devices gain global approval.",
        "down": "Production flaws trigger mass recall of smart pacemakers."
    },
    Healthcare.TELEMEDICINE: {
        "up": "Telemedicine expands access to healthcare in remote areas.",
        "down": "Technical failures in telehealth platforms frustrate patients."
    },

    # Industry
    Industry.MANUFACTURING: {
        "up": "Smart automation slashes production costs.",
        "down": "Factory strikes delay deliveries and hurt productivity."
    },
    Industry.AUTOMOTIVE: {
        "up": "Electric vehicle boom drives automotive industry upward.",
        "down": "Chip shortage disrupts global car production."
    },
    Industry.AEROSPACE: {
        "up": "International partnerships fuel sustainable aviation innovation.",
        "down": "Aircraft crash raises safety concerns about new model."
    },
    Industry.ENERGY: {
        "up": "Global energy demand spikes, boosting traditional energy firms.",
        "down": "Oil price drop slashes energy sector revenue."
    },
    Industry.RENEWABLES: {
        "up": "Record investments in solar and wind power energize green sector.",
        "down": "Environmental concerns over wind turbines affect investor sentiment."
    },
    Industry.MINING: {
        "up": "Rare mineral demand soars, attracting major investors.",
        "down": "Environmental disasters in mines trigger government sanctions."
    },

    # Retail
    Retail.ECOMMERCE: {
        "up": "Online sales surpass expectations during holiday season.",
        "down": "Logistics issues delay shipments for top e-commerce players."
    },
    Retail.FASHION: {
        "up": "Sustainable fashion trend attracts Gen Z consumers.",
        "down": "Labor abuse allegations hit global clothing brands."
    },
    Retail.FOOD_BEVERAGE: {
        "up": "Vegan product demand drives food innovation.",
        "down": "Food contamination scandal damages brand reputations."
    },

    # Media
    Media.GAMING: {
        "up": "AAA game release breaks global sales records.",
        "down": "Game studio faces backlash over bugs and poor optimization."
    },
    Media.FILM_TV: {
        "up": "Streaming platforms soar with new original content.",
        "down": "Writers' strike halts major film and TV productions."
    },
    Media.MUSIC: {
        "up": "Digital royalties system boosts indie artist revenues.",
        "down": "Plagiarism scandal shakes confidence in music labels."
    },

    # Public Sector
    PublicSector.EDUCATION: {
        "up": "Public investment in digital education transforms schools.",
        "down": "Budget cuts lower quality in underfunded educational systems."
    },
    PublicSector.GOVERNMENT: {
        "up": "New fiscal policy attracts foreign investors.",
        "down": "Corruption scandal undermines government credibility."
    },
    PublicSector.NON_PROFIT: {
        "up": "Online campaigns hit record fundraising goals.",
        "down": "Fraud uncovered in major nonprofit damages sector reputation."
    },
    PublicSector.MILITARY_DEFENSE: {
        "up": "Defense tech partnership leads to innovation boom.",
        "down": "Military operation allegations spark international criticism."
    },

    # Transportation
    Transportation.LOGISTICS: {
        "up": "Smart tracking tech revolutionizes global supply chains.",
        "down": "Trucker strike disrupts major logistics networks."
    },
    Transportation.SHIPPING: {
        "up": "International trade growth boosts maritime shipping profits.",
        "down": "Major canal accident delays global shipping routes."
    },
    Transportation.AIRLINES: {
        "up": "Global travel rebound lifts airline stocks.",
        "down": "Mass flight cancellations hurt airline revenues."
    },
    Transportation.RAILWAYS: {
        "up": "Government investment modernizes railway infrastructure.",
        "down": "Train derailment sparks safety debate across regions."
    },

    # Real Estate
    RealEstate.CONSTRUCTION: {
        "up": "Real estate boom spikes demand for construction projects.",
        "down": "Material cost surge slows down active construction sites."
    },
    RealEstate.URBAN_PLANNING: {
        "up": "Smart cities set the new standard in urban planning.",
        "down": "Urban projects criticized for lack of social inclusion."
    }
}
    
    major_sector_news = {
    MarketSectors.TECHNOLOGY: {
        "up": [
            "Global conference on quantum computing reveals breakthrough applications.",
            "Record-breaking tech IPO attracts billions in global investment."
        ],
        "down": [
            "Massive data leak shakes trust in major tech firms.",
            "AI legislation introduces new compliance costs for tech companies."
        ]
    },
    MarketSectors.FINANCE: {
        "up": [
            "New fintech regulation boosts transparency and investor confidence.",
            "Global crypto adoption forces traditional finance to adapt."
        ],
        "down": [
            "Central banks coordinate global interest rate hike.",
            "Major global bank collapses, triggering financial panic."
        ]
    },
    MarketSectors.HEALTHCARE: {
        "up": [
            "WHO announces breakthrough in vaccine for a major global disease.",
            "Biotech index hits record highs on gene therapy advancements."
        ],
        "down": [
            "Healthcare systems overwhelmed due to new pandemic outbreak.",
            "Global pharma merger reshapes the entire healthcare landscape."
        ]
    },
    MarketSectors.INDUSTRY: {
        "up": [
            "Smart factory revolutionizes industrial productivity worldwide.",
            "Industrial robotics sector sees explosive investment."
        ],
        "down": [
            "Environmental restrictions force industry-wide adaptation.",
            "Global steel shortage impacts manufacturing and construction sectors."
        ]
    },
    MarketSectors.RETAIL: {
        "up": [
            "Global shift to e-commerce transforms retail landscape.",
            "Retail sector sees record growth during global holiday season."
        ],
        "down": [
            "Supply chain disruption raises costs across all retail segments.",
            "Consumer confidence drops following inflation surge."
        ]
    },
    MarketSectors.MEDIA: {
        "up": [
            "Streaming wars heat up with new global platform launch.",
            "Gaming surpasses film as top entertainment revenue source."
        ],
        "down": [
            "Major copyright law reform affects content distribution worldwide.",
            "AI-generated content sparks debate across all media industries."
        ]
    },
    MarketSectors.PUBLIC_SECTOR: {
        "up": [
            "Global education reform focuses on digital inclusion.",
            "International collaboration boosts investment in public infrastructure."
        ],
        "down": [
            "Government cybersecurity breach triggers worldwide audits.",
            "Mass protests pressure governments to increase transparency."
        ]
    },
    MarketSectors.TRANSPORTATION: {
        "up": [
            "Breakthrough in battery tech boosts electric transportation globally.",
            "Logistics sector digitized through blockchain innovation."
        ],
        "down": [
            "Oil price hike raises global transportation costs.",
            "Geopolitical tensions disrupt international shipping routes."
        ]
    },
    MarketSectors.REAL_ESTATE: {
        "up": [
            "Global housing demand surge boosts property markets.",
            "Smart city development accelerates in urban hubs."
        ],
        "down": [
            "Interest rate spike cools real estate investments worldwide.",
            "Construction material tariffs shake real estate planning."
        ]
    }
}


    def __init__(self):
        self.daily_news = []
    
    def update_news(self):
        """
        This function generates daily news for the game.
        the daily news contain a random major news and a random number of minor news between 1 and 5
        """

        daily_news = []
        news_sectors = []


        major_sector = choice(list(self.major_sector_news.keys()))
        up_or_down = choice(["up", "down"])
        news = choice(self.major_sector_news[major_sector][up_or_down])

        daily_news.append(news)
        news_sectors.append([major_sector, up_or_down])


        for _ in range(randint(1, 5)):
            minor_sector = choice(list(self.minor_sector_news.keys()))
            up_or_down = choice(["up", "down"])
            news = self.minor_sector_news[minor_sector][up_or_down]

            if news in daily_news: continue

            daily_news.append(news)
            news_sectors.append([minor_sector, up_or_down])

        self.daily_news = daily_news

        return news_sectors
    
    def display_news(self):
        """
        Prints the daily news styled like a newspaper.
        """
        width = 70
        border = "=" * width

        print("\n" + border)
        print("╔" + " THE DAILY NEWS ".center(width - 2, "═") + "╗")
        print(border)

        if self.daily_news:
            # Headline com destaque
            headline = self.daily_news[0].upper()
            print("\n" + "HEADLINE".center(width))
            print("-" * width)
            print(f"{headline}".center(width))
            print("-" * width + "\n")

            # Demais notícias como colunas
            print("OTHER STORIES".center(width))
            print("." * width)
            for news in self.daily_news[1:]:
                wrapped_lines = wrap(news, width)
                for line in wrapped_lines:
                    print(line)
                print("-" * width)

        print(border + "\n")






        
    
    