import pandas as pd
import ghhops_server as hs
from flask import Flask
from utils_database import insert_dataframe
import math

app_hops = Flask(__name__)
hops = hs.Hops(app_hops)


def extract_values(input_dict):
    return [value[0] for value in input_dict.values()]


@hops.component(
    "/send_general_building_data", name="send_general_building_data",
    inputs=[
        # General building data
        hs.HopsString("id", "id", access=hs.HopsParamAccess.TREE),
        hs.HopsString("city", "city", access=hs.HopsParamAccess.TREE),
        hs.HopsString("local_id", "local_id", access=hs.HopsParamAccess.TREE),
        hs.HopsInteger("facade_area", "facade_area", access=hs.HopsParamAccess.TREE),
        hs.HopsInteger("roof_area", "roof_area", access=hs.HopsParamAccess.TREE),
        # Batch processing
        hs.HopsInteger("batch_id", "batch_id", access=hs.HopsParamAccess.TREE)
    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_general_building_data(id, city, local_id, facade_area, roof_area, batch_id):
    df = pd.DataFrame({
        'id': extract_values(id),
        'city': extract_values(city),
        'local_id': extract_values(local_id),
        'facade_area': extract_values(facade_area),
        'roof_area': extract_values(roof_area),
        'batch_id': extract_values(batch_id)
    })
    insert_dataframe(df, 'general_building_data', 'city_simulations')

    return 'STATUS: OK'


@hops.component(
    "/send_facade_simulation_data", name="send_facade_simulation_data",
    inputs=[
        # Facade simulation results
        hs.HopsString("local_id", "local_id", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("avg_roof_radiation", "avg_roof_radiation", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("avg_facade_radiation", "avg_facade_radiation", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("floor_number", "floor_number", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("facade_area_per_floor", "facade_area_per_floor", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("main_normal_vector_facade", "main_normal_vector_facade", access=hs.HopsParamAccess.LIST),
        # Batch processing
        hs.HopsInteger("batch_id", "batch_id", access=hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_facade_simulation_data(local_id, avg_roof_radiation, avg_facade_radiation, floor_number, facade_area_per_floor,
                                main_normal_vector_facade, batch_id):
    df = pd.DataFrame({
        'local_id': extract_values(local_id),
        'avg_roof_radiation': extract_values(avg_roof_radiation),
        'avg_facade_radiation': extract_values(avg_facade_radiation),
        'floor_number': extract_values(floor_number),
        'facade_area_per_floor': extract_values(facade_area_per_floor),
        'main_normal_vector_facade': extract_values(main_normal_vector_facade),
        'batch_id': extract_values(batch_id)
    })
    insert_dataframe(df, 'facade_simulation_results', 'city_simulations')

    return 'STATUS: OK'


@hops.component(
    "/send_roof_simulation_data", name="send_roof_simulation_data",
    inputs=[
        # Roof simulation results
        hs.HopsString("local_id", "local_id", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("roof_type", "roof_type", access=hs.HopsParamAccess.LIST),
        hs.HopsString("roof_grade", "roof_grade", access=hs.HopsParamAccess.LIST),
        hs.HopsString("main_normal_roof", "main_normal_roof", access=hs.HopsParamAccess.LIST),
        hs.HopsString("discarded_vectors", "discarded_vectors", access=hs.HopsParamAccess.LIST),
        # Batch processing
        hs.HopsInteger("batch_id", "batch_id", access=hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_general_building_data(local_id, roof_type, roof_grade, main_normal_roof, discarded_vectors, batch_id):
    df = pd.DataFrame({
        'local_id': extract_values(local_id),
        'roof_type': extract_values(roof_type),
        'roof_grade': extract_values(roof_grade),
        'main_normal_roof': extract_values(main_normal_roof),
        'discarded_vectors': extract_values(discarded_vectors),
        'batch_id': extract_values(batch_id)
    })
    insert_dataframe(df, 'roof_simulation_results', 'city_simulations')

    return 'STATUS: OK'


@hops.component(
    "/calculate_noise_intensity", name="calculate_noise_intensity",
    inputs=[
        hs.HopsNumber("source_noise_level_db", "Source noise level in dB", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("traffic_intensity", "Traffic intensity", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("distance", "Distance from the source", access=hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("noise_level_at_target_distance", "Noise level at target distance",
                      "Noise level at target distance in dB", access=hs.HopsParamAccess.LIST)
    ]
)
def calculate_noise_at_distance(source_noise_level_db, traffic_intensity, distance):
    DEFAULT_ADJUSTMENT_FACTOR_PER_VEHICLE = 0.03
    DEFAULT_ABSORPTION_COEFFICIENT = 0.001
    DEFAULT_GROUND_ABSORPTION = 0.5
    DEFAULT_BARRIER_INSERTION_LOSS = 5

    df = pd.DataFrame({
        'base_noise_level_db': source_noise_level_db,
        'traffic_intensity': traffic_intensity,
        'distance': distance,
        'absorption_coefficient': DEFAULT_ABSORPTION_COEFFICIENT,
        'ground_absorption': DEFAULT_GROUND_ABSORPTION,
        'barrier_insertion_loss': DEFAULT_BARRIER_INSERTION_LOSS,
    })

    # Calculate base noise level adjusted for traffic density
    df['adjusted_base_noise_level_db'] = df.apply(
        lambda row: row['base_noise_level_db'] + row['traffic_intensity'] * DEFAULT_ADJUSTMENT_FACTOR_PER_VEHICLE,
        axis=1)

    # Calculate atmospheric absorption
    df['atmospheric_absorption'] = df.apply(
        lambda row: row['absorption_coefficient'] * row['distance'], axis=1)

    # Then calculate the noise at distance considering all factors
    df['noise_level_at_target_distance'] = df.apply(
        lambda row: row['adjusted_base_noise_level_db'] - 20 * math.log10(row['distance']) - row[
            'atmospheric_absorption'] - row['ground_absorption'] - row['barrier_insertion_loss'],
        axis=1)

    return df['noise_level_at_target_distance'].tolist()


if __name__ == "__main__":
    app_hops.run(host='0.0.0.0', debug=False, port=5000)
