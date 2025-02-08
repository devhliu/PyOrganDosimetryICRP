def verify_svalue_data(svalue_dir: str) -> Dict[str, bool]:
    """
    Verify the integrity of S-value data files.
    
    Args:
        svalue_dir: Directory containing S-value files
        
    Returns:
        Dictionary with radionuclide names as keys and verification status as values
    """
    verification_results = {}
    
    for radionuclide in SUPPORTED_RADIONUCLIDES:
        file_path = os.path.join(svalue_dir, f"{radionuclide}.csv")
        try:
            df = pd.read_csv(file_path, index_col=0)
            
            # Check matrix symmetry where applicable
            symmetrical = all(
                abs(df.loc[organ1, organ2] - df.loc[organ2, organ1]) < 1e-10
                for organ1 in df.index
                for organ2 in df.columns
                if organ1 in df.columns and organ2 in df.index
            )
            
            # Check for required organs
            has_all_organs = (
                set(ORGAN_NAMES).issubset(set(df.columns)) and
                set(ORGAN_NAMES).issubset(set(df.index))
            )
            
            # Check for positive values
            all_positive = (df.values >= 0).all()
            
            verification_results[radionuclide] = (
                symmetrical and has_all_organs and all_positive
            )
            
        except Exception as e:
            verification_results[radionuclide] = False
            
    return verification_results