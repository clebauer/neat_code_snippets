# THIS IS SO COOL and I want to save it.
def swap_level_at_col(df, col_name, col_level = 0):
    # Regardless whether the user inputs one column name or more, we need to
    # place the column name(s) into a list to iterate through.
    if type(col_name) == str:
        col_name = [col_name]
    else:
        col_name = list(col_name)
    
    # We want to grab out the current list of columns
    cols = df.columns.tolist()
    
    # For each column we want to swap levels for, we swap the tuple that 
    # represents the column in the MultiIndex, find where it exists in the
    # current dataframe and overwrite it.
    for dist_col in col_name:
        new_elem = ('', dist_col) if col_level==0 else (dist_col, '')
        ix_to_change = [x for x, y in enumerate(df.columns.tolist()) if y[col_level] == dist_col][0]
        cols[ix_to_change] = new_elem
    
    # Once we've fixed all of the columns needed to be swapper,
    # we reassign the new set of columns back into the MultiIndex.
    df.columns = pd.MultiIndex.from_tuples(cols)
    
    return df
