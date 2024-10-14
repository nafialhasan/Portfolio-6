from mrjob.job import MRJob
from mrjob.step import MRStep

class top_three_countries(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_1,
                   combiner=self.combiner_1,
                   reducer=self.reducer_1),
            MRStep(reducer=self.reducer_2)
        ]

    def mapper_1(self, _, line):
        athlete_data = line.split(", ")
        country = athlete_data[1]
        medal = athlete_data[5]
        yield (country, medal), 1

    def combiner_1(self, key, values):
        country, medal = key
        yield country, (medal, sum(values))

    def reducer_1(self, country, values):
        medal_counts = {"Gold": 0, "Silver": 0, "Bronze": 0}
        for medal, count in values:
            if medal in medal_counts:
                medal_counts[medal] += count
        gold_count = medal_counts["Gold"]
        silver_count = medal_counts["Silver"]
        bronze_count = medal_counts["Bronze"]
        yield None, (country, gold_count, silver_count, bronze_count)

    def reducer_2(self, _, medal_counts):
        sorted_countries = sorted(medal_counts, reverse=True, key=lambda x: x[1])
        top_three_countries = sorted_countries[:3]
        for country, gold_count, silver_count, bronze_count in top_three_countries:
            yield country, {"Gold": gold_count, "Silver": silver_count, "Bronze": bronze_count}

if __name__ == "__main__":
    top_three_countries.run()
