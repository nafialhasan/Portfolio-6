from mrjob.job import MRJob

class sort_athletes_ascending_order(MRJob):
    
    def mapper(self, _, line):
        athlete_data = line.split(", ")
        athlete_id = int(athlete_data[0])
        event = f"{athlete_data[3]}, {athlete_data[4]}"
        data_without_id = [athlete_data[1], athlete_data[2], event, athlete_data[4]]
        yield athlete_id, data_without_id

    def reducer(self, athlete_id, values):
        for value in values:
            yield athlete_id, value

if __name__ == "__main__":
    sort_athletes_ascending_order.run()