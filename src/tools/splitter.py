import pandas as pd
import os

outDir = '../../res'

def run():
    training    = input("Input the percentage of training data: ")
    filePath    = input("Input filename of the file to be split (ex. fileName.csv): ")

    print("Splitting data with ", training, "/", 100-int(training), "split")

    train_percentage = int(training) / 100

    data = pd.read_csv("../../res/" + filePath)
    training_split = data.sample(frac = train_percentage)
    test_split = data.drop(training_split.index)

    print("Training size: ", len(training_split))
    print("Test size: ", len(test_split))

    outName = filePath.replace(".csv", "")
    fullPath = os.path.join(outDir, outName)    

    if not os.path.exists(fullPath):
        os.mkdir(fullPath)

    training_split.reset_index(drop=True, inplace=True)
    test_split.reset_index(drop=True, inplace=True)
    training_split.to_csv(fullPath + "/training.csv", encoding="utf8", index=False)
    test_split.to_csv(fullPath + "/test.csv", encoding="utf8",index=False)

if __name__ == "__main__":
    run()