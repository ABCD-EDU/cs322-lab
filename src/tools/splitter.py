import pandas as pd
import os

outDir = '../../res'

def run():
    training    = input("Input the percentage of training data: ")
    test        = input("Input the percentage of test data: ")
    unseen      = input("Input the percentage of unseen data: ")
    filePath    = input("Input filename of the file to be split (ex. fileName.csv): ")

    print("Splitting data with ", training, "/", test, "/", unseen, "split")

    train_percentage = int(training) / 100
    test_percentage = int(test) / 100
    unseen_percentage = int(unseen) / 100

    totalPercentage = int(training) + int(test) + int(unseen)
    if totalPercentage != 100:
        print("\nValues inputted must be equal to 100. Input instead got a sum of", totalPercentage)
        os._exit(0)

    data = pd.read_csv("../../res/" + filePath)
    training_split = data.sample(frac=train_percentage)
    test_split = data.drop(training_split.index).sample(frac=test_percentage)
    unseen_split = data.drop(training_split.index).drop(test_split.index).sample(frac=unseen_percentage)

    print("Training size: ", len(training_split))
    print("Test size: ", len(test_split))
    print("Unseen size: ", len(unseen_split))

    outName = filePath.replace(".csv", "")
    fullPath = os.path.join(outDir, outName)    

    if not os.path.exists(fullPath):
        os.mkdir(fullPath)

    training_split.reset_index(drop=True, inplace=True)
    test_split.reset_index(drop=True, inplace=True)
    unseen_split.reset_index(drop=True, inplace=True)
    training_split.to_csv(fullPath + "/training.csv", encoding="utf8", index=False)
    test_split.to_csv(fullPath + "/test.csv", encoding="utf8",index=False)
    unseen_split.to_csv(fullPath + "/unseen.csv", encoding="utf8",index=False)

if __name__ == "__main__":
    run()