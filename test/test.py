import logging

import ghhops_server as hs
from flask import Flask
from utils.utils_database import execute_queries, execute_query

app_hops = Flask(__name__)
hops = hs.Hops(app_hops)


@hops.component(
    "/execute_query", name="execute_query", description="insert query for work with postgres databases",
    inputs=[
        hs.HopsString("query_sql", "query_sql", access=hs.HopsParamAccess.TREE)
    ],
)
def insert_query_local(query_sql):
    query_sql_execute = query_sql['InnerTree']['0'][0]['data']
    print(query_sql_execute)
    execute_query(query_sql_execute)

    return


@hops.component(
    "/send", name="send",
    inputs=[
        # General building data
        hs.HopsString("city", "city", access=hs.HopsParamAccess.TREE),
        hs.HopsString("local_id", "local_id", access=hs.HopsParamAccess.TREE),
        hs.HopsInteger("facade_area", "facade_area",
                       access=hs.HopsParamAccess.TREE),
        hs.HopsInteger("roof_area", "roof_area",
                       access=hs.HopsParamAccess.TREE),
        # Batch processing
        hs.HopsInteger("batch_id", "batch_id", access=hs.HopsParamAccess.TREE)
    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_general_building_data(city, local_id, facade_area, roof_area, batch_id):
    # General building data
    city = city['InnerTree']['0'][0]['data']
    local_id = local_id['InnerTree']['0'][0]['data']
    facade_area = facade_area['InnerTree']['0'][0]['data']
    roof_area = roof_area['InnerTree']['0'][0]['data']
    batch_id = batch_id['InnerTree']['0'][0]['data']

    print(city)
    # print(city, local_id, facade_area, roof_area, batch_id)
    vars_general_building_data = (
        city, local_id, facade_area, roof_area, batch_id)
    query_insert = f"""
        INSERT INTO city_simulations.general_building_data (city, local_id, facade_area, roof_area, batch_id)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (city, local_id, batch_id) DO NOTHING;
    """
    execute_query(query_insert, vars_general_building_data)

    return 'STATUS: OK'


@hops.component(
    "/send_facade_simulation_data", name="send_facade_simulation_data",
    description="Send data from grasshopper to postgres database",
    inputs=[
        # Facade simulation results
        hs.HopsString("local_id", "local_id", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("avg_roof_radiation", "avg_roof_radiation",
                       access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("avg_facade_radiation",
                       "avg_facade_radiation", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("floor_number", "floor_number",
                       access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("facade_area_per_floor",
                       "facade_area_per_floor", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("main_normal_vector_facade",
                       "main_normal_vector_facade", access=hs.HopsParamAccess.LIST),
        # Batch processing
        hs.HopsInteger("batch_id", "batch_id", access=hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_facade_simulation_data(local_id, avg_roof_radiation, avg_facade_radiation, floor_number, facade_area_per_floor,
                                main_normal_vector_facade, batch_id):
    # Facade simulation results
    vars_facade_simulation_results = zip(local_id, avg_roof_radiation, avg_facade_radiation, floor_number,
                                         facade_area_per_floor, main_normal_vector_facade, batch_id)
    query_insert_facade = f"""
        -- INSERT INTO city_simulations. ();
    """
    execute_queries(query_insert_facade, vars_facade_simulation_results)

    return 'STATUS: OK'


@hops.component(
    "/send_roof_simulation_data", name="send_roof_simulation_data",
    description="Send data from grasshopper to postgres database",
    inputs=[
        # Roof simulation results
        hs.HopsString("local_id", "local_id", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("roof_type", "roof_type",
                       access=hs.HopsParamAccess.LIST),
        hs.HopsString("roof_grade", "roof_grade",
                      access=hs.HopsParamAccess.LIST),
        hs.HopsString("main_normal_roof", "main_normal_roof",
                      access=hs.HopsParamAccess.LIST),
        hs.HopsString("discarded_vectors", "discarded_vectors",
                      access=hs.HopsParamAccess.LIST),
        # Batch processing
        hs.HopsInteger("batch_id", "batch_id", access=hs.HopsParamAccess.ITEM)
    ],
    outputs=[
        hs.HopsString("log", "log", "Log of the process")
    ]
)
def send_general_building_data(local_id, roof_type, roof_grade, main_normal_roof, discarded_vectors, batch_id):
    # Roof simulation results
    vars_roof_simulation_results = zip(
        local_id, roof_type, roof_grade, main_normal_roof, discarded_vectors, batch_id)
    query_insert_roof = f"""
        -- INSERT INTO city_simulations. ();
    """
    execute_queries(query_insert_roof, vars_roof_simulation_results)

    return 'STATUS: OK'


if __name__ == "__main__":
    app_hops.run(host='0.0.0.0', debug=False, port=5000)
