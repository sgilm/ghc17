def greedy_construct(num_servers, num_endpoints, num_videos, latencies, fallback, connections, requests, video_sizes, capacity):
    """Constructs an initial greedy solution, starting from scratch."""

    solution = [[] for i in range(num_servers)]
    server_use = [0] * num_servers

    # observed_latencies[endpoint][video] is the indexing used.
    observed_latencies = [[None for j in range(num_videos)] for i in range(num_endpoints)]

    keep_adding = True
    while keep_adding:

        improvement = -1 * float('inf')
        video_improvement = None
        server_improvement = None

        # Loop over each request to choose next addition to servers.
        for video, endpoint, quantity in requests:

            # Find best server for current endpoint and video.
            current = observed_latencies[endpoint][video]

            # If not previously calculated...
            if current is None:
                current = fallback[endpoint]

                for server in connections[endpoint]:
                    if video in solution[server] and latencies[server][endpoint] < current:
                        current = latencies[server][endpoint]

                # Record for next time.
                observed_latencies[endpoint][video] = current

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

    return solution


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
