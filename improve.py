from itertools import product


def improve_solution(solution, num_servers, latencies, connections, requests, video_sizes, capacity, used_servers, server_use):
    """Takes a solution and performs next descent to improve it."""

    keep_improving = True
    while keep_improving:

        for server_i, server_j in product(range(num_servers), range(num_servers)):
            for i, j in product(range(len(solution[server_i])), range(len(solution[server_j]))):

                video_i, video_j = solution[server_i][i], solution[server_j][j]

                savings = 0
                for video, endpoint, quantity in requests:
                    if (video == video_i) and (server_i == used_servers[endpoint][video]):
                        savings -= latencies[server_i][endpoint] * quantity

                    if server_i in connections[endpoint]:
                        best = float('inf')
                        best_server = None
                        for server in connections[endpoint]:
                            if latencies[server][endpoint] < best:
                                best = latencies[server][endpoint]
                                best_server = server

                        if best_server == server_i:
                            savings += latencies[server_i][endpoint] * quantity

                    if (video == video_j) and (server_j == used_servers[endpoint][video]):
                        savings -= latencies[server_j][endpoint] * quantity

                    if server_j in connections[endpoint]:
                        best = float('inf')
                        best_server = None
                        for server in connections[endpoint]:
                            if latencies[server][endpoint] < best:
                                best = latencies[server][endpoint]
                                best_server = server

                        if best_server == server_j:
                            savings += latencies[server_i][endpoint] * quantity

                if savings > 0 and (server_use[server_i] - video_sizes[i] + video_sizes[j] < capacity) and (server_use[server_j] - video_sizes[j] + video_sizes[i] < capacity):
                    solution[server_i].remove(video_i)
                    solution[server_i].append(video_j)
                    solution[server_j].remove(video_j)
                    solution[server_j].append(video_i)


if __name__ == "__main__":

    num_servers = 2
    num_endpoints = 2
    num_videos = 3
    latencies = [[1, 1], [4, 2]]
    fallback = [7, 9]
    connections = [[0, 1], [1]]
    requests = [(0, 0, 10), (1, 1, 100), (2, 1, 10)]
    video_sizes = [4, 8, 11]
    capacity = 12

    from construct import greedy_construct

    solution, server_use, used_servers = greedy_construct(num_servers, num_endpoints, num_videos, latencies, fallback, connections, requests, video_sizes, capacity)
    improve_solution(solution, num_servers, latencies, connections, requests, video_sizes, capacity, used_servers, server_use)

    print(solution)
