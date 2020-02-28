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
        self.datepaths = {}
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
            features = [feature.split(",") for feature in f.readlines()[1:]]

            for feature in features:
                # Get relevant NEO information
                # Mapped names to feature indices for readability
                id, name, diameter, ishazardous, orbit_date, miss_distance = (
                    feature[0],
                    feature[2][1:-1],
                    feature[6],
                    feature[13],
                    feature[17],
                    feature[21]
                )

                # Set orbit data
                orbit_data = {
                    "name": name,
                    "orbit_date": orbit_date,
                    "miss_distance": miss_distance
                }

                # Initialize Orbit
                orbit = OrbitPath(**orbit_data)
                
                # Set Near Earth Object data
                neo_data = {
                    "id": id,
                    "name": name,
                    "diameter": diameter,
                    "ishazardous": ishazardous,
                    "orbits": set([orbit])
                }

                # Initialize Near Earth Object
                neo = NearEarthObject(**neo_data)

                if name in self.neos:
                    # If NEO already registered in database,
                    # update its orbits
                    self.neos[name].update_orbits(orbit)
                else:
                    # If NEO not already registered in database,
                    # add it to database
                    self.neos[name] = neo

                if orbit_date in self.datepaths:
                    # If orbit_date already registered in date database,
                    # add NEO
                    self.datepaths[orbit_date].add(neo)
                else:
                    # If orbit_date not already registered in database,
                    # register it to database
                    self.datepaths[orbit_date] = set([neo])             

        return None
