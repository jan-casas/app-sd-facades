CREATE SCHEMA city_simulations;

DROP TABLE IF EXISTS city_simulations.general_building_data;
CREATE TABLE city_simulations.general_building_data
(
    id_general_building_data SERIAL PRIMARY KEY,
    id                       INTEGER,
    city                     text,
    local_id                 text,
    facade_area              FLOAT(8),
    roof_area                FLOAT(8),
    batch_id                 INTEGER,
    CONSTRAINT unique_local_id_batch_id_city UNIQUE (local_id, batch_id, city, id)

);


CREATE TABLE city_simulations.simulation_facade_data
(
    local_id                  VARCHAR(255),
    avg_roof_radiation        NUMERIC,
    avg_facade_radiation      NUMERIC,
    floor_number              INTEGER,
    facade_area_per_floor     NUMERIC,
    main_normal_vector_facade NUMERIC,
    batch_id                  INTEGER,
    CONSTRAINT unique_local_id_batch_id UNIQUE (local_id, batch_id),
    FOREIGN KEY (local_id, batch_id) REFERENCES city_simulations.general_building_data (local_id, batch_id)
);


CREATE TABLE city_simulations.simulation_roof_data
(
    local_id           VARCHAR(255),
    roof_type          VARCHAR(255),
    roof_grade         VARCHAR(255),
    main_normal_vector NUMERIC,
    discarded_vectors  VARCHAR(255),
    batch_id           INTEGER,
    PRIMARY KEY (local_id, batch_id),
    FOREIGN KEY (local_id, batch_id) REFERENCES city_simulations.general_building_data (local_id, batch_id)
);


--------
CREATE TABLE city_simulations.city_district
(
    city_district_id SERIAL PRIMARY KEY,
    city_name        VARCHAR(255),
    district_name    VARCHAR(255)
);

CREATE TABLE city_simulations.city_statistics
(
    city_district_id       INTEGER,
    total_population       INTEGER,
    average_income         NUMERIC,
    average_age            NUMERIC,
    average_household_size NUMERIC,
    FOREIGN KEY (city_district_id) REFERENCES city_simulations.city_district (city_district_id)
);

CREATE TABLE city_simulations.weather_station
(
    city_district_id INTEGER,
    station_id       SERIAL PRIMARY KEY,
    latitude         NUMERIC,
    longitude        NUMERIC,
    weather_path     VARCHAR(255),
    north_vector_rad INTEGER,
    FOREIGN KEY (city_district_id) REFERENCES city_simulations.city_district (city_district_id)
);

CREATE TABLE city_simulations.building
(
    building_id      SERIAL PRIMARY KEY,
    name             VARCHAR(255),
    height           NUMERIC,
    age              INTEGER,
    location         VARCHAR(255),
    z_coordinate     NUMERIC,
    city_district_id INTEGER,
    FOREIGN KEY (city_district_id) REFERENCES city_simulations.city_district (city_district_id)
);

CREATE TABLE city_simulations.floor_window
(
    window_id    SERIAL PRIMARY KEY,
    building_id  INTEGER,
    floor_index  INTEGER,
    x_coordinate NUMERIC,
    y_coordinate NUMERIC,
    FOREIGN KEY (building_id) REFERENCES city_simulations.building (building_id)
);

CREATE TABLE city_simulations.window_simulation
(
    batch_id   SERIAL PRIMARY KEY,
    window_id  INTEGER,
    date       DATE,
    start_time TIME,
    end_time   TIME,
    FOREIGN KEY (window_id) REFERENCES city_simulations.floor_window (window_id)
);

CREATE TABLE city_simulations.window_simulation_results
(
    data_id           SERIAL PRIMARY KEY,
    batch_id          INTEGER,
    simulation_height NUMERIC,
    sun_exposure      NUMERIC,
    wind_exposure     NUMERIC,
    noise_level       NUMERIC,
    FOREIGN KEY (batch_id) REFERENCES city_simulations.window_simulation (batch_id)
);

CREATE TABLE city_simulations.simulation_duration
(
    batch_id   INTEGER PRIMARY KEY,
    total_time INTEGER,
    FOREIGN KEY (batch_id) REFERENCES city_simulations.window_simulation (batch_id)
);

CREATE TABLE city_simulations.landmarks
(
    landmark_id   SERIAL PRIMARY KEY,
    landmark_name VARCHAR(255),
    latitude      NUMERIC,
    longitude     NUMERIC
);

CREATE TABLE city_simulations.zoning_data
(
    data_id             SERIAL PRIMARY KEY,
    batch_id            INTEGER,
    landmark_id         INTEGER,
    permitted_uses      VARCHAR(255),
    density_limit       NUMERIC,
    height_limit        NUMERIC,
    setback_requirement NUMERIC,
    FOREIGN KEY (batch_id) REFERENCES city_simulations.window_simulation (batch_id),
    FOREIGN KEY (landmark_id) REFERENCES city_simulations.landmarks (landmark_id)
);

CREATE TABLE city_simulations.destination_simulation_results
(
    data_id                SERIAL PRIMARY KEY,
    batch_id               INTEGER,
    landmark_id            INTEGER,
    destination_name       VARCHAR(255),
    distance_from_entrance NUMERIC,
    travel_time            NUMERIC,
    closeness_centrality   NUMERIC,
    betweenness_centrality NUMERIC,
    eigenvector_centrality NUMERIC,
    distance_from_landmark NUMERIC,
    FOREIGN KEY (batch_id) REFERENCES city_simulations.window_simulation (batch_id),
    FOREIGN KEY (landmark_id) REFERENCES city_simulations.landmarks (landmark_id)
);

CREATE TABLE city_simulations.view_percentage_simulation_results
(
    data_id                        SERIAL PRIMARY KEY,
    batch_id                       INTEGER,
    window_id                      INTEGER,
    park_view_percentage           NUMERIC,
    sky_view_percentage            NUMERIC,
    north_building_view_percentage NUMERIC,
    south_building_view_percentage NUMERIC,
    road_view_percentage           NUMERIC,
    sea_view_percentage            NUMERIC,
    FOREIGN KEY (batch_id) REFERENCES city_simulations.window_simulation (batch_id),
    FOREIGN KEY (window_id) REFERENCES city_simulations.floor_window (window_id)
);

CREATE TABLE city_simulations.grid_data
(
    grid_id      SERIAL PRIMARY KEY,
    x_coordinate NUMERIC,
    y_coordinate NUMERIC
);

CREATE TABLE city_simulations.public_space_simulation_results
(
    data_id           SERIAL PRIMARY KEY,
    batch_id          INTEGER,
    zoning_id         INTEGER,
    grid_id           INTEGER,
    wind_comfort      NUMERIC,
    sun_exposure      NUMERIC,
    noise_level       NUMERIC,
    shadow_percentage NUMERIC,
    FOREIGN KEY (batch_id) REFERENCES city_simulations.window_simulation (batch_id),
    FOREIGN KEY (zoning_id) REFERENCES city_simulations.zoning_data (data_id),
    FOREIGN KEY (grid_id) REFERENCES city_simulations.grid_data (grid_id)
);

CREATE TABLE city_simulations.training_data
(
    training_id   SERIAL PRIMARY KEY,
    building_id   INTEGER,
    window_id     INTEGER,
    sample_date   DATE,
    current_price NUMERIC,
    FOREIGN KEY (building_id) REFERENCES city_simulations.building (building_id),
    FOREIGN KEY (window_id) REFERENCES city_simulations.floor_window (window_id)
);

CREATE TABLE city_simulations.predicted_values
(
    prediction_id                        SERIAL PRIMARY KEY,
    building_id                          INTEGER,
    window_simulation_result_id          INTEGER,
    destination_simulation_result_id     INTEGER,
    view_percentage_simulation_result_id INTEGER,
    public_space_simulation_result_id    INTEGER,
    predicted_current_value              NUMERIC,
    modified_value                       NUMERIC,
    prediction_date                      DATE,
    FOREIGN KEY (building_id) REFERENCES city_simulations.building (building_id),
    FOREIGN KEY (window_simulation_result_id) REFERENCES city_simulations.window_simulation_results (data_id),
    FOREIGN KEY (destination_simulation_result_id) REFERENCES city_simulations.destination_simulation_results (data_id),
    FOREIGN KEY (view_percentage_simulation_result_id) REFERENCES city_simulations.view_percentage_simulation_results (data_id),
    FOREIGN KEY (public_space_simulation_result_id) REFERENCES city_simulations.public_space_simulation_results (data_id)
);

DROP TABLE IF EXISTS city_simulations.price_comparison;
CREATE TABLE city_simulations.price_comparison
(
    PRIMARY KEY (building_id, prediction_id),
    prediction_id           INTEGER,
    training_id             INTEGER,
    building_id             INTEGER,
    current_price           NUMERIC,
    predicted_current_value NUMERIC,
    is_overpriced           BOOLEAN,
    FOREIGN KEY (building_id) REFERENCES city_simulations.building (building_id),
    FOREIGN KEY (prediction_id) REFERENCES city_simulations.predicted_values (prediction_id),
    FOREIGN KEY (training_id) REFERENCES city_simulations.training_data (training_id)

);

