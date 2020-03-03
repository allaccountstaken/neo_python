class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.orbits = kwargs.get("orbits")
        self.diameter_min_km = float(kwargs.get("diameter_min_km"))
        self.is_potentially_hazardous_asteroid = (
            True if kwargs.get("is_potentially_hazardous_asteroid").lower()=="true" else False
        )

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """

        # TODO: How do we connect orbits back to the Near Earth Object?
        # Orbits stored in a set, hence the use of .add()
        self.orbits.add(orbit)

    def __repr__(self):
        neo_info = (
            "\nNEAR EARTH OBJECT:\n"
            "id: {}\n"
            "name: {}\n"
            "minimum diameter(km): {}\n"
            "orbits: {}\n"
        ).format(self.id, self.name, self.diameter_min_km, self.orbits)

        return neo_info


class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.

    # TODO: You may be adding instance methods to OrbitPath to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.neo_name = kwargs.get("neo_name")
        self.miss_distance_kilometers = float(kwargs.get("miss_distance_kilometers"))
        self.close_approach_date = kwargs.get("close_approach_date")
 
    def __repr__(self):
        orbit_info = (
            "\n\tOrbit(Miss Distance(km): {}, Close Approach Date: {})"
        ).format(self.miss_distance_kilometers, self.close_approach_date)

        return orbit_info
