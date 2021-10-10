def median_function(var):
    median = df["var"].median()
    for i, var in enumerate(df["var"]):
        if var >= median:
            df.loc[i, "var"] = 'high'
        else:
            df.loc[i, "var"] = 'low'
    return df.groupby("var").quality.mean()


median_alcohol = median_function(alcohol)
median_pH = median_function(pH)
median_residual_sugar = median_function(residual_sugar)
median_citric_acid = median_function(citric_acid)