def greedy_construct(num_servers, num_endpoints, num_videos, latencies, fallback, connections, requests, video_sizes, capacity, server_use=None, used_servers=None, solution=None):
    """Constructs an initial greedy solution, starting from scratch."""

    if solution is None:
        solution = [[] for i in range(num_servers)]
    if server_use is None:
        server_use = [0] * num_servers

    if used_servers is None:
        # observed_latencies[endpoint][video] is the indexing used.
        used_servers = [[None for j in range(num_videos)] for i in range(num_endpoints)]

    keep_adding = True
    while keep_adding:

        improvement = -1 * float('inf')
        video_improvement = None
        server_improvement = None

        # Loop over each request to choose next addition to servers.
        for video, endpoint, quantity in requests:

            # Find best server for current endpoint and video.
            used_server = used_servers[endpoint][video]
            if used_server is not None:
                current = latencies[used_server][endpoint]
            else:
                current = fallback[endpoint]

                server_current = None
                for server in connections[endpoint]:
                    if video in solution[server] and latencies[server][endpoint] < current:
                        current = latencies[server][endpoint]
                        server_current = server

                # Record for next time.
                used_servers[endpoint][video] = server_current

            # Calculate savings.
            for server in connections[endpoint]:
                savings = (current - latencies[server][endpoint]) * quantity

                if savings > improvement and (server_use[server] + video_sizes[video]) <= capacity and not video in solution[server]:
                    improvement = savings
                    video_improvement = video
                    server_improvement = server

        # Check whether to stop.
        if improvement == -1 * float('inf'):
            keep_adding = False

        # If not, add to the solution.
        else:
            solution[server_improvement].append(video_improvement)
            server_use[server_improvement] += video_sizes[video_improvement]

    return solution, server_use, used_servers


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

    solution = greedy_construct(num_servers, num_endpoints, num_videos, latencies, fallback, connections, requests, video_sizes, capacity)

    print(solution)
