from enum import Enum
import random

from models import NearEarthObject, OrbitPath


class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        pass

    def print_to_file(self, data, csv_file, data_type):
        """Writes data to a csv file"""

        # check for empty data
        if not data: return False

        with open(csv_file, 'w') as f:

            # Customize outputs differently for NearEarthObjects and OrbitPaths
            if data_type == NearEarthObject:
                f.write("id,name,minimum_diameter_in_km,orbits\n")

                for datum in data:
                    out = "{},{},{},{}\n".format(
                        datum.id,
                        datum.name,
                        datum.diameter_min_km,
                        ";".join([orbit._repr_cust() for orbit in datum.orbits])
                    )
                    f.write(out)

            elif data_type == OrbitPath:
                f.write("neo_name,close_approach_date,miss_distance_kilometers\n")

                for datum in data:
                    out = "{},{},{}\n".format(
                        datum.neo_name,
                        datum.close_approach_date,
                        datum.miss_distance_kilometers
                    )
                    f.write(out)


        return True

    def print_to_terminal(self, data):
        """Prints data to the terminal"""

        if not data: 
            print("No data to print.")
            return False

        for index, datum in enumerate(data):
            index += 1
            print("- {} ----------------".format(index))
            print(datum)
            if index % 3 == 0:
                input("Press key to continue...")

        return True

    def write(self, format, data, return_object, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected calls the
        appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output e.g. filename
        :return: bool representing if write successful or not
        """
        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.

        if format==OutputFormat.display.value:
            return self.print_to_terminal(data)
        elif format==OutputFormat.csv_file.value:
            return self.print_to_file(data, 'output.csv', return_object)
