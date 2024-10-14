from mrjob.job import MRJob
from mrjob.step import MRStep

class top_three_events_decade(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_1,
                   combiner=self.combiner_1,
                   reducer=self.reducer_1),
            MRStep(reducer=self.reducer_2),
            MRStep(reducer=self.reducer_3)
        ]

    def mapper_1(self, _, line):
        athlete_data = line.split(", ")
        year = int(athlete_data[2])
        country = athlete_data[1]
        event = f"{athlete_data[3]}, {athlete_data[4]}"
        medal = athlete_data[5]
        decade = (year // 10) * 10
        yield (decade, country, event), 1

    def combiner_1(self, key, values):
        yield key, sum(values)

    def reducer_1(self, key, values):
        decade, country, event = key
        yield decade, (sum(values), country, event)

    def reducer_2(self, decade, medal_data):
        sorted_events = sorted(medal_data, reverse=True, key=lambda x: x[0])
        top_three_events = sorted_events[:3]
        decade_range = f"{decade}-{decade+9}"
        for medal_count, country, event in top_three_events:
            yield None, (decade_range, [country, event, medal_count])

    def reducer_3(self, _, decade_event_data):
        all_data = list(decade_event_data)
        all_data_sorted = sorted(all_data, reverse=True, key=lambda x: x[0])
        for decade_range, event_info in all_data_sorted:
            yield decade_range, event_info

if __name__ == "__main__":
    top_three_events_decade.run()