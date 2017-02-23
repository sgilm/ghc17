def filter_solution(solution, used_servers, server_use, num_endpoints, video_sizes):

    for server, server_videos in enumerate(solution):
        for video in server_videos:

            server_used = False
            for endpoint in range(num_endpoints):
                server_used = server_used or (used_servers[endpoint][video] == server)

            if not server_used:
                server_videos.remove(video)
                server_use[server] -= video_sizes[video]


if __name__ == "__main__":

    solution = [[1], [0]]
    video_sizes = [10, 11]
    used_servers = [[1, 1], [1, 1]]
    server_use = [11, 10]
    num_endpoints = 2

    filter_solution(solution, used_servers, server_use, num_endpoints, video_sizes)

    print(solution)
