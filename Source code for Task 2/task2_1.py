from mrjob.job import MRJob
from mrjob.step import MRStep

class top_three_athletes(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_1),
            MRStep(reducer=self.reducer_2)
        ]

    def mapper(self, _, line):
        athlete_data = line.split(", ") 
        athlete_id = int(athlete_data[0])
        medals = ["Gold", "Silver", "Bronze"]
        if athlete_data[5] in medals:
            medal = athlete_data[5]
            yield (athlete_id, medal), 1

    def reducer_1(self, key, values):
        athlete_id, medal = key
        yield medal, (sum(values), athlete_id)

    def reducer_2(self, medal, values):
        sorted_athletes = sorted(values, reverse=True, key=lambda x: x[0])
        top_three_athletes = sorted_athletes[:3]
        for count, athlete_id in top_three_athletes:
            yield medal, [athlete_id, count]

if __name__ == "__main__":
    top_three_athletes.run()