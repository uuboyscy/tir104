df["OnBoard"] = np.where(
    df["OnBoard"].str.upper() == "V",
    True,
    False,
    test,
)
