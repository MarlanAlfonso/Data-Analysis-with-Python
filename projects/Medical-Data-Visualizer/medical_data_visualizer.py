import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
df = pd.read_csv('medical_examination.csv')

# 2. Add overweight column
# BMI = weight(kg) / height(m)^2 — convert height from cm to m first
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3. Normalize cholesterol and gluc
# 1 = normal (good) → 0, anything above 1 (bad) → 1
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    # 4. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 5. Group and reformat — count occurrences of each value per cardio group
    df_cat = df_cat.groupby(
        ['cardio', 'variable', 'value']
    ).size().reset_index(name='total')

    # 6. Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    # 7. Save and return
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 8. Clean the data — filter out incorrect patient segments
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 9. Calculate the correlation matrix
    corr = df_heat.corr()

    # 10. Generate mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 11. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 12. Plot the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        vmin=-0.16,
        vmax=0.32,
        square=True,
        linewidths=0.5,
        ax=ax
    )

    # 13. Save and return
    fig.savefig('heatmap.png')
    return fig