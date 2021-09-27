def human_years_cat_years_dog_years(hy, dy = 15, cy = 15):
    if hy == 1:
        pass
    elif hy == 2:
        cy = dy = 24
    else:
        cy = (4 * hy) + 16
        dy = (5 * hy) + 14
    return [hy,cy,dy]
    return [0,0,0]