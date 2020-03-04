
from collections import defaultdict

from models import OrbitPath, NearEarthObject


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.
        self.filename = filename
        self.datepaths = defaultdict(set)
        self.neos = {}

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?
        with open(filename, "r") as f:
            # store all lines except header
            features = [
                feature.split(",") for feature in f.readlines()[1:] if feature
            ]

            for feature in features:
                # Get relevant NEO information
                # Mapped names to feature indices for readability
                id, name, diameter_min_km, ishazardous, orbit_date, miss_distance = (
                    feature[0],
                    feature[2],
                    feature[5],
                    feature[13],
                    feature[17],
                    feature[21]
                )

                # Set orbit data
                orbit_data = {
                    "neo_name": name,
                    "close_approach_date": orbit_date,
                    "miss_distance_kilometers": miss_distance
                }

                # Initialize Orbit
                orbit = OrbitPath(**orbit_data)
                
                # Set Near Earth Object data
                neo_data = {
                    "id": id,
                    "name": name,
                    "diameter_min_km": diameter_min_km,
                    "is_potentially_hazardous_asteroid": ishazardous,
                    "orbits": set([orbit])
                }

                # Initialize Near Earth Object
                neo = NearEarthObject(**neo_data)

                # If NEO already registered in database update its orbits,
                # Else register NEO in database
                if name in self.neos:
                    self.neos[name].update_orbits(orbit)
                else:
                    self.neos[name] = neo


                # If orbit_date already registered in date database add NEO,
                # else register new date with NEO. 
                # NB: Using defaultdict
                self.datepaths[orbit_date].add(neo)
             

        return None
