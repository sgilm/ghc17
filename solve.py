from construct import greedy_construct
from filter import filter_solution
from output import output_solution
import datetime
import copy


if __name__ == "__main__":

    # Read data.
    #num_servers, num_endpoints, num_videos, latencies, fallback, connections, requests, video_sizes, capacity

    solution = solution, server_use, used_servers = greedy_construct(
            num_servers,
            num_endpoints,
            num_videos,
            latencies,
            fallback,
            connections,
            requests,
            video_sizes,
            capacity
        )

    previous_solution = None
    while previous_solution != solution:

        previous_solution = copy.deepcopy(solution)

        solution = filter_solution(
            solution,
            used_servers,
            server_use,
            num_endpoints,
            video_sizes
        )

        solution, server_use, used_servers = greedy_construct(
            num_servers,
            num_endpoints,
            num_videos,
            latencies,
            fallback,
            connections,
            requests,
            video_sizes,
            capacity,
            solution=solution,
            server_use=server_use,
            used_servers=used_servers
        )

    solution_name = str(datetime.date)
    output_solution(solution, solution_name)
