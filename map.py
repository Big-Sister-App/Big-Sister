# Will eventually split this into more classes for the sake of SOLID, but right now just keeping it simple <3
from datetime import datetime
import os
import googlemaps
import pandas as pd
import sqlite3

class LocationCuration:
    """
    A tool to use and geocode report data to be used in a Google Map

    Attrs:
        db_dir (str): the location of the directory where databases should be stored or accessed from
    """
    db_dir = "databases/"


    def __init__(self, gmaps_key: str, db_name: str = "reports.db", table_name: str = "reports") -> None:
        """
        Initializes a LocationCuration that will gather report data from the given
        database's table, and geocode using the given GoogleMaps API key.

        Args:
            gmaps_key (str): GoogleMaps API Key (passed in as .env variable)
            db_name (str): the name of the database holding the report data
            table_name (str): the name of the table within the database that has the report data
        """
        self.gmaps_api = googlemaps.Client(key=gmaps_key)
        self.db_name = LocationCuration.db_dir + db_name
        self.table_name = table_name

        self.df = None
        self.conn = None
        self.cursor = None
        self.load_table()

        self.marker_locations = []


    def load_table(self) -> None:
        """
        Loads the database and gets the table with report data. If the table does not
        already exist, it will be created.
        """
        # config
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

        # make table
        create_table = f"""CREATE TABLE IF NOT EXISTS
        {self.table_name}(id INTEGER PRIMARY KEY autoincrement, date TEXT, typeOfReport TEXT, 
        reportDesc TEXT, location TEXT)"""
        self.cursor.execute(create_table)
        self.conn.commit()


    def add_to_table(self, report_info: dict[str, str]) -> None:
        """
        Adds the given report information to the report table in the database. The report's
        date is automatically set to the time this function is ran.

        Args:
            report_info (dict): The report information to be added. Should include typeOfReport,
                                 reportDesc, and location
        """
        report_type = report_info['typeOfReport']
        report_desc = report_info['reportDesc']
        report_location = report_info['location']
        report_date = datetime.now()
        report = (report_date, report_type, report_desc, report_location)

        self.cursor.execute(
            f"""INSERT INTO {self.table_name} (date, typeOfReport, reportDesc, location) VALUES(?, ?, ?, ?)""", report
        )
        self.conn.commit()


    def convert_db_to_df(self, show_head: bool = False) -> pd.DataFrame:
        """
        Converts this curation tool's database into a pandas dataframe.

        Args:
            show_head (bool): whether or not to show the first 10 rows of the dataframe 
                              when it has been made
        Returns:
            df (pd.DataFrame): the database as a pandas dataframe
        """
        query = f"SELECT * from {self.table_name}"
        df = pd.read_sql_query(query, self.conn)
        if show_head:
            print(df.head(10))
        return df
    

    def geocode_location(self, location: str, show_result: bool = False) -> str:
        """
        Generates a latitude longitude pair using the given street address.

        Args:
            location (str): a street address e.g. 350 Huntington Ave, Boston, MA
            show_result (bool): whether or not to show the final, geocoded, result
        Returns:
            lat_long (tuple): the lat long pair in the order (latitude, longitude)
        """
        # TODO: what should we do in the case that an address cannot be located? Do we go with
        # the closest alternative or prompt for new response? Or prompt but give suggestion
        full_location = self.gmaps_api.geocode(location)
        geo_location = full_location[0]["geometry"]["location"]
        lat_long = f"{geo_location['lat']}, {geo_location['lng']}"
        return lat_long
    

    def geocode_locations(self, show_result: bool = False) -> None:
        """
        Generates latitude and longitude pairs for all locations in the report data, and adds them to
        a generated dataframe.

        Args:
            show_result (bool): whether or not to show the first 10 results after all the report location
            data hasbeen geocoded.
        """
        self.df = self.convert_db_to_df()
        self.df['gcAddress'] = self.df['location'].apply(self.geocode_location)
        print(self.df.head(10))
        if show_result:
            print(self.df.head(10))


    def convert_df_to_json(self, json_filename: str = "geocoded_data.json") -> None:
        """
        Converts this tool's dataframe into a JSON file.

        Args:
            json_filename (str): the name of the outputted json file
        """
        self.df.to_json(LocationCuration.db_dir + json_filename, orient='records')


    def geocode_and_export(self, show_result: bool = False):
        """
        Geocodes the database data and exports it as a json file
        """
        self.geocode_locations(show_result=show_result)
        try:
            self.convert_df_to_json()
            print("JSON File created successfully.")
        except:
            print("JSON File could not be created.")



def run():
    """
    Runs the LocationCuration tool
    """
    geocoder = LocationCuration(os.getenv('GMAPS_API_KEY'))
    geocoder.geocode_and_export()

