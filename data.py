import numpy as np
import pandas as pd

class Data():
    file = None
    acc = None
    df = pd.DataFrame()

    dt = ""
    n = ""
    fac = ""

    def Int_vel(self):
        vel = np.zeros(len(self.df["Acc"]))
        dis = np.zeros(len(self.df["Acc"]))
        d = 0
        vf = 0
        for i in range(1,len(self.df["Acc"])):
            vf = vf + (self.df["Acc"][i]+self.df["Acc"][i-1])/2*self.dt
            vel[i] = vf

            d = d + (vel[i]+vel[i-1])/2*self.dt
            dis[i] = d

        self.df["Vel"] = vel
        self.df["Dis"] = dis
    
