import os

class base_configuration:
    '''Create an Object for API Calls
    
    Input/Attributes
    ----------------
    For ease of access, all the attributes are to be inserted during the input() Calls

    :type  user_name: str
    :param user_name: User Name of the User by which the API Key is Registered

    :type  location: list or tuple
    :param location: Location at which the Data is to be Fetched from, in the format (latitude, longitude)
    These are internally modified and are associated with the attribute lat and lon respectively

    :type  year: str
    :param year: Year of which the Data is Required to Fetch
    '''
    def __init__(self):
        self.user_name = input('Full Name: ').strip().replace(' ', '+') # get the user name, and remove trailing spaces
        self.lat, self.lon = [float(i) for i in input('Location: ').split()] # location in comma delimitted format
        self.year = int(input('Year: ').strip())

        # Getting API-KEY from File
        try:
            self.key = open(os.path.join('.', 'API-KEY'), 'rt').read()
        except FileNotFoundError: # if not available, ask user for API-KEY
            self.key = input('API Key: ').strip()

        self.attrib     = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'
        self.leap_year  = 'true'
        self.interval   = 30
        self.local_time = 'true' # i.e. utc = false

        # General Use-Case
        self.reason_for_use        = input('Reason for Use: ').strip().replace(' ', '+') or 'testing'
        self.your_affiliation      = input('Affiliation: ').strip().replace(' ', '+') or 'my+institute'
        self.your_registered_email = input('Email ID: ').strip().replace(' ', '+') or 'john.doe@example.com'

        self.mailing_list = 'false' # do not subscribe to mailing list

    @property
    def generate_url(self):
        '''Generate the Formatted URL that is required by NREL API to Fetch the Required Data'''
        return 'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?' \
            + f'wkt=POINT({self.lon}%20{self.lat})' \
            + f'&names={self.year}&leap_day={self.leap_year}&interval={self.interval}&utc={self.local_time}' \
            + f'&full_name={self.user_name}&email={self.your_registered_email}' \
            + f'&affiliation={self.your_affiliation}&mailing_list={self.mailing_list}' \
            + f'&reason={self.reason_for_use}&api_key={self.key}&attributes={self.attrib}'

    @property
    def location(self) -> tuple:
        '''Location from which the Data is to be Fetched
        
        Returns
        -------
        :param location: Location, which is as provided by the user in the format (lat, lon)
        '''
        return tuple([self.lat, self.lon])