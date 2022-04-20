from statistics import mean
from scipy import stats
Estimates = [100,150,210,185,360,800,450,650,700,400,260,150]'
def CrowdComputting():
    Estimates.sort()
    trim=int(0.1*len(Estimates))
    Estimates=Estimates[trim-1:]
    Estimates=Estimates[:len(Estimates)-trim]
    print(mean(Estimates))
def TrimMean():
    m=starts.trim_mean()