def robust_nested_json_to_multi_df(data): 
    """
    Convert nested JSON to multi-index DataFrame with clean hierarchical columns
    """
    # First get the flattened data
    flattened_data = []

    if isinstance(data, dict):
        flattened_data.append(explore_nested_json(data))
    elif isinstance(data, list):
        for item in data:
            flattened_data.append(explore_nested_json(item))

    # Create initial DataFrame
    df = pd.DataFrame(flattened_data)

    # Convert flat column names to multi-index
    columns = df.columns
    index_tuples = [col.split('.') for col in columns]

    # Get the maximum depth
    max_depth = max(len(tup) for tup in index_tuples)

    # Pad shorter tuples with empty strings instead of NaN
    clean_tuples = [
        tuple(list(tup) + [''] * (max_depth - len(tup)))
        for tup in index_tuples
    ]

    # Create MultiIndex with cleaned tuples
    multi_index = pd.MultiIndex.from_tuples(
        clean_tuples,
        names=[f'level_{i}' for i in range(max_depth)]
    )

    df.columns = multi_index
    return df