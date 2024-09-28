import ghhops_server as hs
import pandas as pd
from flask import Flask

from utils_database import insert_dataframe

app_hops = Flask(__name__)
hops = hs.Hops(app_hops)


def extract_values(input_dict: dict) -> list:
    return [value[0] for value in input_dict.values()]


def round_decimal(df: pd.DataFrame, decimals: int = 2) -> pd.DataFrame:
    # if column is number round to 2 decimals
    for column in df.columns:
        if df[column].dtype == 'float64':
            df[column] = df[column].round(decimals)

    return df


@hops.component(
    "/send_simulation_results", name="send_simulation_results",
    description="Send data from grasshopper to postgres database",
    inputs=[
        hs.HopsString("local_id", "local_id",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("avg_sun_exposure", "avg_sun_exposure",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("winter_exposure", "winter_exposure",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("summer_exposure", "summer_exposure",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("visibility", "visibility",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("orientation", "orientation",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("height", "height",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("distance", "distance",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("distance_clamp", "distance_clamp",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("noise", "noise",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("density", "density",
                      access=hs.HopsParamAccess.TREE),
        hs.HopsNumber("batch_id", "batch_id",
                      access=hs.HopsParamAccess.TREE)

    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_simulation_results(local_id, avg_sun_exposure, winter_exposure, summer_exposure,
                            visibility, orientation, height, distance, distance_clamp, noise,
                            density, batch_id):
    df = pd.DataFrame({
        'local_id': extract_values(local_id),
        'avg_sun_exposure': extract_values(avg_sun_exposure),
        'winter_exposure': extract_values(winter_exposure),
        'summer_exposure': extract_values(summer_exposure),
        'visibility': extract_values(visibility),
        'orientation': extract_values(orientation),
        'height': extract_values(height),
        'distance': extract_values(distance),
        'distance_clamp': extract_values(distance_clamp),
        'noise': extract_values(noise),
        'density': extract_values(density),
        'batch_id': extract_values(batch_id)
    })
    df = round_decimal(df)
    insert_dataframe(df, 'simulation_results', 'city_simulations')

    return 'STATUS: OK'


if __name__ == "__main__":
    app_hops.run(host='0.0.0.0', debug=False, port=5000)
