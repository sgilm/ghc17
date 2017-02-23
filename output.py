def output_solution(solution, filename):

    with open(filename, 'w') as file:
        file.write(str(len(solution)))
        file.write('\n')

        for i, videos in enumerate(solution):
            file.write(str(i) + ' ' + ' '.join(map(str, videos)))
            file.write('\n')


if __name__ == "__main__":

    solution = [[0, 1], [1]]
    output_solution(solution, 'test.txt')
