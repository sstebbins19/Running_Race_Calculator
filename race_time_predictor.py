# Import Modules
from datetime import time
from time import strftime
from time import gmtime
import pandas as pd

def predict_times(dist1, time1, dist2):
    """
    Predict the times of race distance given a time and distance of a
    previous race.

    Args:
        dist1 (string): Distance of previous race
                        (5km, 10km, 21.1km or 42.2km)
        time1   (time): Time of previous race
                        (hh:mm:ss format)
        dist2 (string): Distance of race which is being predicted
                        (5km, 10km, 21.1km or 42.2km)

    Formula:
        T2 = T1 * (D2 / D1) ** 1.06

    Returns:
        time: Predicted time for race distance
    """
    try:
        secs1 = (time1.hour * 60 + time1.minute) * 60 + time1.second
        d1 = float(dist1.strip('km'))
        d2 = float(dist2.strip('km'))
        pred_secs = round(secs1 * (d2 / d1) ** 1.06)
        pred_time = strftime("%H:%M:%S", gmtime(pred_secs))
        return pred_time
    except:
        return None

def predict_table(dist1, time1):
    distances = ['5km', '10km', '21.1km', '42.2km']
    df = pd.DataFrame(columns = headers)
        
