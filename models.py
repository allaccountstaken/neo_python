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
        self.diameter = kwargs.get("diameter")
        self.ishazardous = kwargs.get("ishazardous")
        

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """

        # TODO: How do we connect orbits back to the Near Earth Object?
        # Orbits stored in a set, hence the use of .add()
        self.orbits.add(orbit)


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
        self.name = kwargs.get("name")
        self.miss_distance = kwargs.get("miss_distance")
        self.orbit_date = kwargs.get("orbit_date")
