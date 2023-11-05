import pandas as pd

data = {
    'Name': [
        'Giovanni',
        'Marti',
        'David',
        'Alice',
        'Bob'
    ],
    'Age': [
        18,
        25,
        38,
        22,
        30
    ]
}

df = pd.DataFrame(data)  # Create a DataFrame from the data dictionary
print(df)

names = df['Name'] 

youngs = df[df['Age'] < 25]  

print("\nYoungs:")
print(youngs)
