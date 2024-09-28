-- Show all tables in the city_simulations database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'city_simulations';

DROP SCHEMA city_simulations CASCADE;
CREATE SCHEMA IF NOT EXISTS city_simulations;
CREATE TABLE IF NOT EXISTS city_simulations.simulation_results
(
    id               SERIAL PRIMARY KEY,
    local_id         TEXT,
    avg_sun_exposure FLOAT,
    winter_exposure  FLOAT,
    summer_exposure  FLOAT,
    visibility       FLOAT,
    orientation      FLOAT,
    height           FLOAT,
    distance         FLOAT,
    distance_clamp   FLOAT,
    noise            FLOAT,
    density          FLOAT,
    batch_id         FLOAT,
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT simulation_results_local_id_uindex UNIQUE (local_id, orientation, height)
);
