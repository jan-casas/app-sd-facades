-- we don't know how to generate root <with-no-name> (class Root) :(

CREATE TABLE main.data_barrios
(
    type                                           text,
    "geometry.type"                                text,
    "geometry.coordinates"                         text,
    "properties.gml_id"                            text,
    "properties.beginLifes"                        text,
    "properties.conditionO"                        text,
    "properties.localId"                           text,
    "properties.namespace"                         text,
    "properties.horizontal"                        double,
    "properties.horizont"                          text,
    "properties.horizont_2"                        text,
    "properties.referenceG"                        integer,
    "properties.numberOfFl"                        integer,
    "properties.heightBelo"                        integer,
    "properties.heightBe"                          text,
    "properties.numberOf"                          integer,
    "properties.codbarrio"                         integer,
    "properties.nombre"                            text,
    "properties.coddistbar"                        integer,
    "properties.coddistrit"                        text,
    "properties.calculoFachadas_0320_sup_fachada"  text,
    "properties.calculoFachadas_0320_sup_cubierta" text
);

CREATE TABLE main.df_propiedades_entidaddes
(
    localid                           text,
    gml_id_x                          text,
    codbarrio                         text,
    nombre                            text,
    gml_id_join                       text,
    edad                              text,
    currentuse                        text,
    numberofdwellings                 text,
    cat_edad                          text,
    coste_fachada                     text,
    coste_cubierta                    text,
    calculofachadas_0320_sup_fachada  text,
    calculofachadas_0320_sup_cubierta text,
    coste_total                       text,
    orientacion_fachada               text,
    longitud_fachada                  text,
    Clase                             text,
    polar_coord                       text
);

CREATE TABLE main.geojson_data
(
    id      INTEGER
        PRIMARY KEY,
    name    TEXT,
    geojson TEXT
);

CREATE TABLE main.monoparte
(
    type                    text,
    "geometry.type"         text,
    "geometry.coordinates"  text,
    "properties.gml_id"     text,
    "properties.beginLifes" text,
    "properties.conditionO" text,
    "properties.localId"    text,
    "properties.namespace"  text,
    "properties.horizontal" text,
    "properties.horizont"   text,
    "properties.horizont_2" text,
    "properties.referenceG" text,
    "properties.numberOfFl" text,
    "properties.heightBelo" text,
    "properties.heightBe"   text,
    "properties.numberOf"   text,
    "properties.RE_id"      text,
    "properties.RE_left"    text,
    "properties.RE_top"     text,
    "properties.RE_right"   text,
    "properties.RE_bottom"  text,
    "properties.RE_NUMPOIN" text,
    "properties.RE_id_2"    text,
    "properties.RE_left_2"  text,
    "properties.RE_top_2"   text,
    "properties.RE_right_2" text,
    "properties.RE_bottom_" text,
    "properties.RE_NUMPO"   text
);

CREATE TABLE main.real_estate_data
(
    local_id          text,
    latitude          double,
    longitude         double,
    floor             double,
    number            double,
    street            text,
    local_use         text,
    unit_cost         double,
    mantainance_cost  double,
    year_construction double
);

CREATE TABLE main.real_estate_data_spain_updated
(
    local_id                                      text,
    latitude                                      double,
    longitude                                     double,
    floor                                         double,
    number                                        double,
    street                                        text,
    local_use                                     text,
    unit_cost                                     double,
    mantainance_cost                              double,
    year_construction                             double,
    "Facade Sun Radiation"                        double,
    "Shadow Overcast Time"                        double,
    "Morning/Afternoon Sun Radiation"             double,
    Density                                       double,
    "Views Availability"                          double,
    "Age of the Building"                         double,
    "Urban Noise"                                 double,
    "Close Distance to Green/Walking Areas"       double,
    "Potential Cost Reduction Using Solar Energy" double,
    "Social Life"                                 double,
    "Territorial Connection"                      double,
    "Air Pollution"                               double
);

CREATE TABLE main.simulation_results
(
    local_id         text,
    avg_sun_exposure double,
    winter_exposure  double,
    summer_exposure  double,
    visibility       double,
    orientation      double,
    height           double,
    distance         double,
    distance_clamp   double,
    noise            double,
    density          double,
    batch_id         double
);

CREATE TABLE main.simulation_results_complete
(
    local_id         text,
    avg_sun_exposure double,
    winter_exposure  double,
    summer_exposure  double,
    visibility       double,
    orientation      double,
    height           double,
    distance         double,
    distance_clamp   double,
    noise            double,
    density          double,
    batch_id         double
);

CREATE TABLE main.sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);
