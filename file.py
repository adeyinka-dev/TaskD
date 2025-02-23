def read_dataset():
    with open("dataset.csv", "r") as file:
        # Assumes the dataset is comma-separated
        dataset = file.read().split(",")
        dataset = [float(i) for i in dataset if i.strip() != ""]
    return dataset


def write_result(results):
    with open("result.csv", "w") as file:
        file.write("Iteration,Fitness,Solution\n")
        for i in range(len(results)):
            file.write(str(results[i][0]) + ",")
            file.write(str(results[i][1]) + ",")
            # Write the solution as a sequence of 0s and 1s
            for j in results[i][2]:
                file.write(str(j))
                file.write(" ")
            file.write("\n")
