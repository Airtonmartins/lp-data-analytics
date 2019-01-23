import pandas as pd
from pykrige.ok import OrdinaryKriging
from sklearn.preprocessing import MinMaxScaler



# ----- Filtering -----

def before2018(df):
    mask = (df['Date'] >= '01/01/2000') & (df['Date'] < '01/01/2018')
    return df.loc[mask]

def buildDataFrameCleaned(df):
    df_cleaned = df[df.Hora != 0]
    df_leftover = df[df.Hora == 0]
    df_cleaned = df_cleaned[["Estacao", "Data", "Precipitacao"]]
    df_cleaned['Date'] = df_cleaned['Data'].astype('str')
    df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], format='%d/%m/%Y', errors='coerce')
    df_cleaned['year'] = df_cleaned.Date.dt.year
    df_cleaned['month'] = df_cleaned.Date.dt.month
    df_cleaned['day'] = df_cleaned.Date.dt.day
    df_cleaned["Precipitacao"].fillna(0, inplace=True)
    return before2018(df_cleaned)

def setLongLat(df, lat, long):
    df["long"] = long
    df["lat"] = lat


#----- Interpolation -----

def build_df_predict(df_predict_cities, df_fit, z_predict):
    try:
        df_predict_cities["predict"] = z_predict.tolist()
    except:
        df_predict_cities["predict"] = 0
    df_predict_cities = df_predict_cities[["Estacao","predict"]]
    return pd.concat([df_predict_cities, df_fit])

def clean_df_fit(df_fit):
    estacao = df_fit["Estacao"]
    d_fit = {'Estacao': estacao, 'predict': df_fit["Precipitacao"]}
    return pd.DataFrame(data=d_fit)

def interp_precipitation(df_fit):
    fit_cities = df_fit["Estacao"].tolist()
    df_coordinates_cities = pd.read_csv('original_data/coordinates_cities.csv', delimiter=',', encoding='utf-8')
    df_predict_cities = df_coordinates_cities.loc[~df_coordinates_cities.Estacao.isin(fit_cities)]
    lon_fit = df_fit["long"]
    lat_fit = df_fit["lat"]
    if not(df_fit['Precipitacao'] == 0).all():
        z_fit = df_fit["Precipitacao"]
        OK = OrdinaryKriging(lon_fit, lat_fit, z_fit, variogram_model='linear', verbose=False,
                     enable_plotting=False, coordinates_type='geographic')
        lon_predict = df_predict_cities["long"]
        lat_predict = df_predict_cities["lat"]
        z_predict, ss_predict = OK.execute('points', lon_predict, lat_predict)
    else:
        z_predict = None
    df_fit_cleaned = clean_df_fit(df_fit)
    return build_df_predict(df_predict_cities, df_fit_cleaned, z_predict)

def get_df_interpolation_sum_monthy(df, year_month):
    df_year_month = df[df["concat"] == year_month]
    df_interp = interp_precipitation(df_year_month)
    df_interp["year"] = df_year_month["year"].unique()[0]
    df_interp["month"] = df_year_month["month"].unique()[0]
    df_interp["long"] = df_year_month["long"].unique()[0]
    df_interp["lat"] = df_year_month["lat"].unique()[0]
    df_interp["year-month"] = df_year_month["concat"].unique()[0]

    if (df_interp['predict'].min() < 0):
        difference = 1 + df_interp['predict'].min()
        scale = MinMaxScaler(feature_range=(0, df_interp['predict'].max() + difference ))
        df_interp["predict"] = scale.fit_transform(df_interp[['predict']].values.astype(float))
    df_interp.rename(columns={'predict':'predict_precipitation_normalized'}, inplace=True)
    return df_interp

def get_df_interpolation_day(df, day):
    df_day = df[df["Date"] == day]
    df_day_interp = interp_precipitation(df_day)
    df_day_interp["Data"] = df_day["Data"].unique()[0]
    df_day_interp["Date"] = df_day["Date"].unique()[0]
    df_day_interp["year"] = df_day["year"].unique()[0]
    df_day_interp["month"] = df_day["month"].unique()[0]
    df_day_interp["day"] = df_day["day"].unique()[0]
    df_day_interp["long"] = df_day["long"].unique()[0]
    df_day_interp["lat"] = df_day["lat"].unique()[0]
    #df_day_interp.rename(columns={'predict':'predict_precipitacao'}, inplace=True)
    if (df_day_interp['predict'].min() < 0):
        difference = 1 + df_day_interp['predict'].min()
        scale = MinMaxScaler(feature_range=(0, df_day_interp['predict'].max() + difference ))
        df_day_interp["predict"] = scale.fit_transform(df_day_interp[['predict']].values.astype(float))
    df_day_interp.rename(columns={'predict':'predict_precipitation_normalized'}, inplace=True)
    return df_day_interp







if __name__ == "__main__":

    dataset_recife = pd.read_csv('original_data/Recife(curado).txt', delimiter=';')
    dataset_arcoverde = pd.read_csv('original_data/arcoverde.txt', delimiter=';')
    dataset_cabrobo = pd.read_csv('original_data/cabrobo.txt', delimiter=';')
    dataset_ouricuri = pd.read_csv('original_data/ouricuri.txt', delimiter=';')
    dataset_petrolina = pd.read_csv('original_data/petrolina.txt', delimiter=';')
    dataset_surubim = pd.read_csv('original_data/surubim.txt', delimiter=';')
    dataset_triunfo = pd.read_csv('original_data/triunfo.txt', delimiter=';')

    df_recife_cleaned = buildDataFrameCleaned(dataset_recife)
    df_arcoverde_cleaned = buildDataFrameCleaned(dataset_arcoverde)
    df_cabrobo_cleaned = buildDataFrameCleaned(dataset_cabrobo)
    df_ouricuri_cleaned = buildDataFrameCleaned(dataset_ouricuri)
    df_petrolina_cleaned = buildDataFrameCleaned(dataset_petrolina)
    df_surubim_cleaned = buildDataFrameCleaned(dataset_surubim)
    df_triunfo_cleaned = buildDataFrameCleaned(dataset_triunfo)

    setLongLat(df_recife_cleaned, -8.05, -34.95)
    setLongLat(df_arcoverde_cleaned, -8.41, -37.08)
    setLongLat(df_cabrobo_cleaned, -8.51, -39.33)
    setLongLat(df_ouricuri_cleaned, -7.9, -40.04)
    setLongLat(df_petrolina_cleaned, -9.36, -40.46)
    setLongLat(df_surubim_cleaned, -7.83, -35.71)
    setLongLat(df_triunfo_cleaned, -7.81, -38.11)

    concat_cities = pd.concat(
        [df_recife_cleaned, df_arcoverde_cleaned, df_cabrobo_cleaned, df_ouricuri_cleaned, df_petrolina_cleaned,
         df_surubim_cleaned, df_triunfo_cleaned])
    concat_cities = concat_cities.replace({'Estacao': {82900: 'RECIFE', 82890: 'ARCOVERDE', 82886: 'CABROBÓ',
                                                       82753: 'OURICURI', 82983: 'PETROLINA', 82797: 'SURUBIM',
                                                       82789: 'TRIUNFO'}})

    df_drop_duplicates = concat_cities.drop_duplicates("Estacao")
    df_long_lat = df_drop_duplicates[["Estacao", "long", "lat"]]

    df_precipitation_grouby_year_month = pd.DataFrame({
        'Precipitacao': concat_cities.groupby(["Estacao", "year", "month"])["Precipitacao"].sum()}).reset_index()

    result_monthly_precipitation_sum = pd.merge(df_precipitation_grouby_year_month, df_long_lat, on='Estacao')

    result_monthly_precipitation_sum.to_csv("filtered_data/result_monthly_precipitation_sum.csv", sep=',', encoding='utf-8')
    concat_cities.to_csv("filtered_data/all_cities.csv", sep=',', encoding='utf-8')

    result_monthly_precipitation_sum['concat'] = result_monthly_precipitation_sum["year"].map(str) + "-" + result_monthly_precipitation_sum["month"].map(
        str)

    interpolation_sum_monthy_list = list(map(lambda x: get_df_interpolation_sum_monthy(result_monthly_precipitation_sum, x),
                                             result_monthly_precipitation_sum["concat"].unique().tolist()))

    df_interpolation_sum_monthy = pd.concat(interpolation_sum_monthy_list)
    df_interpolation_sum_monthy.to_csv("interpolation_data/interpolation_sum_monthy_2000_2017.csv", sep=',', encoding='utf-8')


    days_2015_2017 = concat_cities[concat_cities["year"] >= 2015]


    interpolation_days_2015_2017_list = list(map(lambda x: get_df_interpolation_day(days_2015_2017, x), days_2015_2017["Date"].unique()))

    df_interpolation_days_2015_2017 = pd.concat(interpolation_days_2015_2017_list)

    df_interpolation_days_2015_2017.to_csv("interpolation_data/interpolation_days_2015_2017.csv", sep=',', encoding='utf-8')


















