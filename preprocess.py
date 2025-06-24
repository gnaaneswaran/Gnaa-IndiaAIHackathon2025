import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def preprocess_data(input_file='data/sample_data.csv', output_file='data/preprocessed_mineral_data.csv'):
    # Load data
    data = pd.read_csv(input_file)

    # Handle missing numeric values
    numeric_columns = ['magnetic_anomaly', 'REE_concentration', 'rock_density']
    for col in numeric_columns:
        if col in data.columns:
            data[col].fillna(data[col].mean(), inplace=True)

    # Identify categorical columns (e.g., lithology)
    categorical_columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    if categorical_columns:
        encoder = OneHotEncoder(sparse=False, drop='first')
        encoded_array = encoder.fit_transform(data[categorical_columns])
        encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(categorical_columns))
        data = pd.concat([data.drop(columns=categorical_columns), encoded_df], axis=1)

    # Save preprocessed data
    data.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data()
