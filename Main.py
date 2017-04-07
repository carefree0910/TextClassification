import os

from SkRun import run

print("Running Naive Bayes written by myself...")
os.system("python _NB.py")

print("Running Naive Bayes in sklearn...")
run("Naive Bayes")

print("Running LinearSVM in sklearn")
run("SVM")
