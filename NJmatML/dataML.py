
def smiles_csv_rdkit(name3):
    import pandas as pd
    global data3
    data3 = pd.read_csv(name3)

    print(data3.iloc[:,0])
    return data3



def rdkit_featurizer(path):
    import pandas as pd
    from rdkit import Chem
    from rdkit.Chem import Draw
    from rdkit.Chem import rdDepictor
    from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator
    # choose 200 molecular descriptors
    chosen_descriptors = ['BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n', 'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'EState_VSA1', 'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'ExactMolWt', 'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'FractionCSP3', 'HallKierAlpha', 'HeavyAtomCount', 'HeavyAtomMolWt', 'Ipc', 'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'MaxAbsEStateIndex', 'MaxAbsPartialCharge', 'MaxEStateIndex', 'MaxPartialCharge', 'MinAbsEStateIndex', 'MinAbsPartialCharge', 'MinEStateIndex', 'MinPartialCharge', 'MolLogP', 'MolMR', 'MolWt', 'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles', 'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms', 'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles', 'NumSaturatedRings', 'NumValenceElectrons', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7', 'PEOE_VSA8', 'PEOE_VSA9', 'RingCount', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 'SMR_VSA8', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'VSA_EState1', 'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5', 'VSA_EState6', 'VSA_EState7', 'VSA_EState8', 'VSA_EState9', 'fr_Al_COO', 'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde', 'fr_alkyl_carbamate', 'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole', 'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss', 'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile', 'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester', 'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan', 'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'qed']
    # create molecular descriptor calculator
    mol_descriptor_calculator = MolecularDescriptorCalculator(chosen_descriptors)
    data4 = data3.iloc[:,0].map(lambda x : mol_descriptor_calculator.CalcDescriptors(Chem.MolFromSmiles(x)))
    remain = pd.DataFrame(data3.iloc[:, 2:])
    data4 = pd.DataFrame(data4)
    data5 = pd.DataFrame()
    # split to 200 columns
    for i in range(0, 200):
        data5 = pd.concat([data5, data4.applymap(lambda x: x[i])], axis=1)
    data5.columns = chosen_descriptors
    print(data5)
    # 特征存入rdkit_featurizer.csv
    data5.to_csv(path+"/rdkit_featurizer_output.csv", index=False)
    return data5




def drawMolecule(smiles):
    import pandas as pd
    from rdkit import Chem
    from rdkit.Chem import Draw
    from rdkit.Chem import rdDepictor
    from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator
    m = Chem.MolFromSmiles(smiles)
    print(m)




def inorganic_csv(name4):
    import pandas as pd
    global data4
    data4 = pd.read_csv(name4)
    print(data4)
    return data4

def inorganic_magpie_csv(name20):
    import pandas as pd
    global data20
    data20 = pd.read_csv(name20)
    print(data20)
    return data20


def inorganic_featurizer(path):
    #one-hot
    import pandas as pd
    from matminer.featurizers.composition.element import ElementFraction
    from pymatgen.core import Composition

    ef = ElementFraction()
    list4 = list(map(lambda x: Composition(x), data4.iloc[:,0]))
    data7 = pd.DataFrame()
    for i in range(0, len(data4.index)):
        data7 = pd.concat([data7, pd.DataFrame(ef.featurize(list4[i])).T])
    data8 = data7.reset_index()
    data8 = data8.iloc[:, 1:]
    element_fraction_labels = ef.feature_labels()
    print(element_fraction_labels)
    data8.columns = element_fraction_labels
    print(data8)
    # 特征存入pydel_featurizer.csv
    data8.to_csv(path+"/inorganic_featurizer_output.csv",index=None)
    return data8,element_fraction_labels


def inorganic_magpie_featurizer(path):
    # Importing necessary libraries
    from matminer.featurizers.conversions import StrToComposition
    from matminer.featurizers.composition import ElementProperty
    import pandas as pd


    # Extracting columns with 'Formula' suffix
    formula_columns = [col for col in data20.columns if col.endswith('Formula')]

    # Extracting 'Formula' column and converting it to composition
    str_to_comp = StrToComposition(target_col_id='composition')
    df_comp = str_to_comp.featurize_dataframe(data20, col_id=formula_columns[0])

    # Extracting other columns
    unselected_columns = [col for col in data20.columns if col not in formula_columns]

    # Featurizing compositions
    features = ['Number', 'MendeleevNumber', 'AtomicWeight', 'MeltingT',
                'Column', 'Row', 'CovalentRadius', 'Electronegativity',
                'NsValence', 'NpValence', 'NdValence', 'NfValence', 'NValence',
                'NsUnfilled', 'NpUnfilled', 'NdUnfilled', 'NfUnfilled', 'NUnfilled',
                'GSvolume_pa', 'GSbandgap', 'GSmagmom', 'SpaceGroupNumber']

    stats = ['mean', 'minimum', 'maximum', 'range', 'avg_dev', 'mode']

    featurizer = ElementProperty(data_source='magpie',
                                  features=features,
                                  stats=stats)
    df_features = featurizer.featurize_dataframe(df_comp, col_id='composition')
    # df_features = df_features.iloc[:, 2:-1]

    # Saving features to csv
    df_features.to_csv(path + "/1_magpie_features.csv", index=None)

    # Saving unselected columns to csv
    df_unselected = data20[unselected_columns]
    df_unselected.to_csv(path + "/2_unselected.csv", index=None)

    # Merging features and unselected columns
    df_total = pd.concat([df_features.reset_index(drop=True), df_unselected.reset_index(drop=True)], axis=1)

    # Remove duplicate columns and keep the last occurrence
    df_total = df_total.loc[:,~df_total.columns.duplicated(keep='last')]

    # Remove 'Formula' and 'composition' columns
    df_total = df_total.drop(columns=['Formula', 'composition'], errors='ignore')

    # Saving total dataframe to csv
    df_total.to_csv(path + "/train-test.csv", index=None)

    return df_total




# multiple rdkit smiles columns
def featurize_Multicolumn_Smiles_RDKit(path,csvpath):
    #magpie (matminer) and rdkit, 2in1
    import pandas as pd
    import rdkit.Chem.Descriptors
    def select_columns_by_suffix(df, suffix):
        filtered_columns = df.filter(regex=f'{suffix}$')
        return filtered_columns

    def extract_and_store_columns(csv_file, suffixes):

        df = pd.read_csv(csv_file)

        selected_columns = {}
        for suffix in suffixes:
            selected_columns[suffix] = select_columns_by_suffix(df, suffix)
            print('********************************************************************************')
            print(f"Columns ending with '{suffix}':")
            print('********************************************************************************')
            print(selected_columns[suffix])

            #global df_selected
            df_selected = pd.concat(selected_columns, axis=1)
            # df_combined = pd.concat(selected_columns.values(), axis=1)
            # df_combined.to_csv('selected_columns.csv', index=False)
            selected_columns[suffix].to_csv(path+'/'+f'{suffix}_selected_columns.csv', index=False)

        unselected_columns = df.drop(columns=[col for cols in selected_columns.values() for col in cols.columns])

        unselected_columns.to_csv(path+'/'+'unselected_columns.csv', index=False)

        return selected_columns

    # 用法示例
    file_path = csvpath
    # suffixes = ['Formula', 'Smiles']
    suffixes = ['Smiles']
    selected_columns = extract_and_store_columns(file_path, suffixes)

    original_data = pd.DataFrame(pd.read_csv(path+'/Smiles_selected_columns.csv'))

    import pandas as pd


    new_datasets = {}


    for col_name in original_data.columns:
        new_dataset = pd.DataFrame({'Name': original_data[col_name]})
        new_datasets['data' + str(len(new_datasets) + 1)] = new_dataset


    for key, value in new_datasets.items():
        print(f"{key}:\n{value}\n")


    result_datasets = {}



    merged_result = result_datasets


    original_data2 = pd.DataFrame(pd.read_csv(path+'/Smiles_selected_columns.csv'))

    new_datasets2 = {}


    for col_name in original_data2.columns:

        new_dataset2 = pd.DataFrame({'Name': original_data2[col_name]})


        new_datasets2['organic_data' + str(len(new_datasets2) + 1)] = new_dataset2

    for key, value in new_datasets2.items():
        print(f"{key}:\n{value}\n")

    from rdkit import Chem
    from rdkit.Chem import Descriptors
    import pandas as pd

    rdkit_datasets = {}

    for key, dataset in new_datasets2.items():
        rdkit_features = dataset['Name'].apply(lambda x: Chem.MolFromSmiles(x))

        valid_mols = rdkit_features.dropna()

        if not valid_mols.empty:

                        rdkit_descriptors = valid_mols.apply(lambda x: [Descriptors.BalabanJ(x),
Descriptors.BertzCT(x),
Descriptors.Chi0(x),
Descriptors.Chi0n(x),
Descriptors.Chi0v(x),
Descriptors.Chi1(x),
Descriptors.Chi1n(x),
Descriptors.Chi1v(x),
Descriptors.Chi2n(x),
Descriptors.Chi2v(x),
Descriptors.Chi3n(x),
Descriptors.Chi3v(x),
Descriptors.Chi4n(x),
Descriptors.Chi4v(x),
Descriptors.EState_VSA1(x),
Descriptors.EState_VSA10(x),
Descriptors.EState_VSA11(x),
Descriptors.EState_VSA2(x),
Descriptors.EState_VSA3(x),
Descriptors.EState_VSA4(x),
Descriptors.EState_VSA5(x),
Descriptors.EState_VSA6(x),
Descriptors.EState_VSA7(x),
Descriptors.EState_VSA8(x),
Descriptors.EState_VSA9(x),
Descriptors.ExactMolWt(x),
Descriptors.FpDensityMorgan1(x),
Descriptors.FpDensityMorgan2(x),
Descriptors.FpDensityMorgan3(x),
Descriptors.FractionCSP3(x),
Descriptors.HallKierAlpha(x),
Descriptors.HeavyAtomCount(x),
Descriptors.HeavyAtomMolWt(x),
Descriptors.Ipc(x),
Descriptors.Kappa1(x),
Descriptors.Kappa2(x),
Descriptors.Kappa3(x),
Descriptors.LabuteASA(x),
Descriptors.MaxAbsEStateIndex(x),
Descriptors.MaxAbsPartialCharge(x),
Descriptors.MaxEStateIndex(x),
Descriptors.MaxPartialCharge(x),
Descriptors.MinAbsEStateIndex(x),
Descriptors.MinAbsPartialCharge(x),
Descriptors.MinEStateIndex(x),
Descriptors.MinPartialCharge(x),
Descriptors.MolLogP(x),
Descriptors.MolMR(x),
Descriptors.MolWt(x),
Descriptors.NHOHCount(x),
Descriptors.NOCount(x),
Descriptors.NumAliphaticCarbocycles(x),
Descriptors.NumAliphaticHeterocycles(x),
Descriptors.NumAliphaticRings(x),
Descriptors.NumAromaticCarbocycles(x),
Descriptors.NumAromaticHeterocycles(x),
Descriptors.NumAromaticRings(x),
Descriptors.NumHAcceptors(x),
Descriptors.NumHDonors(x),
Descriptors.NumHeteroatoms(x),
Descriptors.NumRadicalElectrons(x),
Descriptors.NumRotatableBonds(x),
Descriptors.NumSaturatedCarbocycles(x),
Descriptors.NumSaturatedHeterocycles(x),
Descriptors.NumSaturatedRings(x),
Descriptors.NumValenceElectrons(x),
Descriptors.PEOE_VSA1(x),
Descriptors.PEOE_VSA10(x),
Descriptors.PEOE_VSA11(x),
Descriptors.PEOE_VSA12(x),
Descriptors.PEOE_VSA13(x),
Descriptors.PEOE_VSA14(x),
Descriptors.PEOE_VSA2(x),
Descriptors.PEOE_VSA3(x),
Descriptors.PEOE_VSA4(x),
Descriptors.PEOE_VSA5(x),
Descriptors.PEOE_VSA6(x),
Descriptors.PEOE_VSA7(x),
Descriptors.PEOE_VSA8(x),
Descriptors.PEOE_VSA9(x),
Descriptors.RingCount(x),
Descriptors.SMR_VSA1(x),
Descriptors.SMR_VSA10(x),
Descriptors.SMR_VSA2(x),
Descriptors.SMR_VSA3(x),
Descriptors.SMR_VSA4(x),
Descriptors.SMR_VSA5(x),
Descriptors.SMR_VSA6(x),
Descriptors.SMR_VSA7(x),
Descriptors.SMR_VSA8(x),
Descriptors.SMR_VSA9(x),
Descriptors.SlogP_VSA1(x),
Descriptors.SlogP_VSA10(x),
Descriptors.SlogP_VSA11(x),
Descriptors.SlogP_VSA12(x),
Descriptors.SlogP_VSA2(x),
Descriptors.SlogP_VSA3(x),
Descriptors.SlogP_VSA4(x),
Descriptors.SlogP_VSA5(x),
Descriptors.SlogP_VSA6(x),
Descriptors.SlogP_VSA7(x),
Descriptors.SlogP_VSA8(x),
Descriptors.SlogP_VSA9(x),
Descriptors.TPSA(x),
Descriptors.VSA_EState1(x),
Descriptors.VSA_EState10(x),
Descriptors.VSA_EState2(x),
Descriptors.VSA_EState3(x),
Descriptors.VSA_EState4(x),
Descriptors.VSA_EState5(x),
Descriptors.VSA_EState6(x),
Descriptors.VSA_EState7(x),
Descriptors.VSA_EState8(x),
Descriptors.VSA_EState9(x),
Descriptors.fr_Al_COO(x),
Descriptors.fr_Al_OH(x),
Descriptors.fr_Al_OH_noTert(x),
Descriptors.fr_ArN(x),
Descriptors.fr_Ar_COO(x),
Descriptors.fr_Ar_N(x),
Descriptors.fr_Ar_NH(x),
Descriptors.fr_Ar_OH(x),
Descriptors.fr_COO(x),
Descriptors.fr_COO2(x),
Descriptors.fr_C_O(x),
Descriptors.fr_C_O_noCOO(x),
Descriptors.fr_C_S(x),
Descriptors.fr_HOCCN(x),
Descriptors.fr_Imine(x),
Descriptors.fr_NH0(x),
Descriptors.fr_NH1(x),
Descriptors.fr_NH2(x),
Descriptors.fr_N_O(x),
Descriptors.fr_Ndealkylation1(x),
Descriptors.fr_Ndealkylation2(x),
Descriptors.fr_Nhpyrrole(x),
Descriptors.fr_SH(x),
Descriptors.fr_aldehyde(x),
Descriptors.fr_alkyl_carbamate(x),
Descriptors.fr_alkyl_halide(x),
Descriptors.fr_allylic_oxid(x),
Descriptors.fr_amide(x),
Descriptors.fr_amidine(x),
Descriptors.fr_aniline(x),
Descriptors.fr_aryl_methyl(x),
Descriptors.fr_azide(x),
Descriptors.fr_azo(x),
Descriptors.fr_barbitur(x),
Descriptors.fr_benzene(x),
Descriptors.fr_benzodiazepine(x),
Descriptors.fr_bicyclic(x),
Descriptors.fr_diazo(x),
Descriptors.fr_dihydropyridine(x),
Descriptors.fr_epoxide(x),
Descriptors.fr_ester(x),
Descriptors.fr_ether(x),
Descriptors.fr_furan(x),
Descriptors.fr_guanido(x),
Descriptors.fr_halogen(x),
Descriptors.fr_hdrzine(x),
Descriptors.fr_hdrzone(x),
Descriptors.fr_imidazole(x),
Descriptors.fr_imide(x),
Descriptors.fr_isocyan(x),
Descriptors.fr_isothiocyan(x),
Descriptors.fr_ketone(x),
Descriptors.fr_ketone_Topliss(x),
Descriptors.fr_lactam(x),
Descriptors.fr_lactone(x),
Descriptors.fr_methoxy(x),
Descriptors.fr_morpholine(x),
Descriptors.fr_nitrile(x),
Descriptors.fr_nitro(x),
Descriptors.fr_nitro_arom(x),
Descriptors.fr_nitro_arom_nonortho(x),
Descriptors.fr_nitroso(x),
Descriptors.fr_oxazole(x),
Descriptors.fr_oxime(x),
Descriptors.fr_para_hydroxylation(x),
Descriptors.fr_phenol(x),
Descriptors.fr_phenol_noOrthoHbond(x),
Descriptors.fr_phos_acid(x),
Descriptors.fr_phos_ester(x),
Descriptors.fr_piperdine(x),
Descriptors.fr_piperzine(x),
Descriptors.fr_priamide(x),
Descriptors.fr_prisulfonamd(x),
Descriptors.fr_pyridine(x),
Descriptors.fr_quatN(x),
Descriptors.fr_sulfide(x),
Descriptors.fr_sulfonamd(x),
Descriptors.fr_sulfone(x),
Descriptors.fr_term_acetylene(x),
Descriptors.fr_tetrazole(x),
Descriptors.fr_thiazole(x),
Descriptors.fr_thiocyan(x),
Descriptors.fr_thiophene(x),
Descriptors.fr_unbrch_alkane(x),
Descriptors.fr_urea(x),
Descriptors.qed(x)])
            # 将 RDKit 描述符转换为 DataFrame
            rdkit_descriptors_df = pd.DataFrame(list(rdkit_descriptors), columns=['BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n', 'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'EState_VSA1', 'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'ExactMolWt', 'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'FractionCSP3', 'HallKierAlpha', 'HeavyAtomCount', 'HeavyAtomMolWt', 'Ipc', 'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'MaxAbsEStateIndex', 'MaxAbsPartialCharge', 'MaxEStateIndex', 'MaxPartialCharge', 'MinAbsEStateIndex', 'MinAbsPartialCharge', 'MinEStateIndex', 'MinPartialCharge', 'MolLogP', 'MolMR', 'MolWt', 'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles', 'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms', 'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles', 'NumSaturatedRings', 'NumValenceElectrons', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7', 'PEOE_VSA8', 'PEOE_VSA9', 'RingCount', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 'SMR_VSA8', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'VSA_EState1', 'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5', 'VSA_EState6', 'VSA_EState7', 'VSA_EState8', 'VSA_EState9', 'fr_Al_COO', 'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde', 'fr_alkyl_carbamate', 'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole', 'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss', 'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile', 'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester', 'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan', 'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'qed'])


            prefix_rdkit = f'{key}_rdkit_'
            rdkit_descriptors_df = rdkit_descriptors_df.add_prefix(prefix_rdkit)

            rdkit_datasets[key] = rdkit_descriptors_df

    merged_rdkit_result = pd.concat(rdkit_datasets.values(), axis=1)
    merged_rdkit_result.fillna(0, inplace=True)

    merged_rdkit_result.to_csv(path+'/merged_rdkit_result.csv', index=False)

    print(merged_rdkit_result)

    unselected_columns = pd.DataFrame(pd.read_csv(path+'/unselected_columns.csv'))

    merged_rdkit_result.reset_index(drop=True, inplace=True)
    unselected_columns.reset_index(drop=True, inplace=True)

    all_merged_data = pd.concat([merged_rdkit_result, unselected_columns], axis=1)


    all_merged_data.to_csv(path+'/train_test_dataset.csv', index=False)



def featurize_Multicolumn_Smiles_Morgan(path,csvpath):

    import pandas as pd
    def select_columns_by_suffix(df, suffix):
        filtered_columns = df.filter(regex=f'{suffix}$')
        return filtered_columns

    def extract_and_store_columns(csv_file, suffixes):

        df = pd.read_csv(csv_file)

        selected_columns = {}
        for suffix in suffixes:
            selected_columns[suffix] = select_columns_by_suffix(df, suffix)
            print('********************************************************************************')
            print(f"Columns ending with '{suffix}':")
            print('********************************************************************************')
            print(selected_columns[suffix])

            #global df_selected
            df_selected = pd.concat(selected_columns, axis=1)
            # df_combined = pd.concat(selected_columns.values(), axis=1)
            # df_combined.to_csv('selected_columns.csv', index=False)
            selected_columns[suffix].to_csv(path+'/'+f'{suffix}_selected_columns.csv', index=False)


        unselected_columns = df.drop(columns=[col for cols in selected_columns.values() for col in cols.columns])


        unselected_columns.to_csv(path+'/'+'unselected_columns.csv', index=False)

        return selected_columns

    # 用法示例
    file_path = csvpath
    # suffixes = ['Formula', 'Smiles']
    suffixes = ['Smiles']
    selected_columns = extract_and_store_columns(file_path, suffixes)

    original_data = pd.DataFrame(pd.read_csv(path+'/Smiles_selected_columns.csv'))

    import pandas as pd

    # 假设 original_data 是您的原始数据集
    # 创建一个空字典，用于存储新的数据集
    new_datasets = {}

    # 遍历原始数据集的每一列
    for col_name in original_data.columns:
        # 创建新的数据集，将当前列命名为 'Name'
        new_dataset = pd.DataFrame({'Name': original_data[col_name]})

        # 将新数据集存储在字典中，字典的键是 'data1'，'data2'，依此类推
        new_datasets['data' + str(len(new_datasets) + 1)] = new_dataset

    # 打印或使用新的数据集
    for key, value in new_datasets.items():
        print(f"{key}:\n{value}\n")


    # 用于存储特征转换后的数据集
    result_datasets = {}


    # 合并所有数据集
    merged_result = result_datasets

    # 将合并后的结果保存为 CSV 文件
    # merged_result.to_csv(path+'/merged_result.csv', index=False)

    # 打印或使用合并后的结果
    # print(merged_result)

    # 有机部分
    original_data2 = pd.DataFrame(pd.read_csv(path+'/Smiles_selected_columns.csv'))

    new_datasets2 = {}

    # 遍历原始数据集的每一列
    for col_name in original_data2.columns:
        # 创建新的数据集，将当前列命名为 'Name'
        new_dataset2 = pd.DataFrame({'Name': original_data2[col_name]})

        # 将新数据集存储在字典中，字典的键是 'organic_data1'，'organic_data2'，依此类推
        new_datasets2['organic_data' + str(len(new_datasets2) + 1)] = new_dataset2

    # 打印或使用新的数据集
    for key, value in new_datasets2.items():
        print(f"{key}:\n{value}\n")

    import pandas as pd
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem
    from rdkit import Chem
    from rdkit.Chem import Descriptors
    import pandas as pd

    rdkit_datasets = {}


    for key, dataset in new_datasets2.items():

        rdkit_features = dataset['Name'].apply(
            lambda x: AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(x), 2))


        rdkit_features_df = pd.DataFrame(
            list(rdkit_features.apply(lambda x: np.frombuffer(x.ToBinary(), dtype=np.uint8))))

        # 添加前缀
        prefix_rdkit = f'{key}_rdkit_'
        rdkit_features_df = rdkit_features_df.add_prefix(prefix_rdkit)

        # 存储特征化后的数据集
        rdkit_datasets[key] = rdkit_features_df


    # 合并 RDKit 特征化后的数据集
    merged_rdkit_result = pd.concat(rdkit_datasets.values(), axis=1)
    merged_rdkit_result.fillna(0, inplace=True)
    # 将合并后的结果保存为 CSV 文件
    merged_rdkit_result.to_csv(path+'/merged_rdkit_result.csv', index=False)

    # 打印或使用合并后的 RDKit 特征化结果
    print(merged_rdkit_result)

    unselected_columns = pd.DataFrame(pd.read_csv(path+'/unselected_columns.csv'))
    # 合并前重置索引
    # merged_result.reset_index(drop=True, inplace=True)
    merged_rdkit_result.reset_index(drop=True, inplace=True)
    unselected_columns.reset_index(drop=True, inplace=True)

    # 合并三个数据集
    all_merged_data = pd.concat([merged_rdkit_result, unselected_columns], axis=1)

    all_merged_data.to_csv(path+'/train_test_dataset.csv', index=False)




def heatmap_before(path):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    featureData=data.iloc[:,:]
    corMat = pd.DataFrame(featureData.corr())
    corMat.to_csv(path+'/heatmap-before.csv')
    plt.figure(figsize=(20, 30))
    sns.heatmap(corMat, annot=False, vmax=1, square=True, cmap="Blues",linewidths=0)
    plt.savefig(path+'/heatmap-before.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return



def feature_rfe_select1(remain_number,path):

    from sklearn import preprocessing
    from sklearn.feature_selection import RFE, RFECV
    from sklearn.ensemble import RandomForestRegressor
    import csv
    import numpy as np

    # 输入数据归一化
    X = data.values[:, :-1]
    for i in range(X.shape[1]):
        X[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X[:, [i]])

    # rfe步骤
    model = RandomForestRegressor()
    rfe = RFE(estimator=model, n_features_to_select=remain_number, step=1)
    rfe_X = rfe.fit_transform(X, y)
    print("Whether the feature is selected:\n", rfe.support_)                                          # ndarray
    print("Number of remaining features:", rfe_X.shape)                                           # tuple
    list1 = rfe.support_.tolist()

    import pandas as pd
    Features_0 = pd.DataFrame(data=data.iloc[:, :-1].columns, columns=['Features'])
    Features_0
    Features_rfe = pd.DataFrame(data=rfe.support_, columns=['whether selected'])
    Features_rfe
    #     pd.options.display.max_rows=None
    p = pd.concat([Features_0, Features_rfe], axis=1)
    q = p[p['whether selected']>0]
    r = q.reset_index(drop=True)
    global s_rfe
    s_rfe = pd.DataFrame(data=data,columns=r.Features.values)
    global target
    target = pd.DataFrame(data=data.iloc[:,-1])

    global data_rfe
    data_rfe = pd.concat([s_rfe,target], axis=1)
    print("Final features after feature selection (s_rfe):", r.Features.values)                                        # ndarray
    print("Target:", target)
    print("Final data after feature selection (data_rfe):", data_rfe)

    list2 = r.Features.values.tolist()

    # print全输出
    with open(path + "/data.txt", "w") as f:

        f.write("Whether the feature is selected:\n")
        for i in range(len(list1)):
            f.write(str(list1[i])+' ')

        f.write("\nAcquired data feature size:\n")
        f.write('(%s,%s)' % rfe_X.shape)

        f.write("\nS_rfe(Final feature):\n")
        for i in range(len(list2)):
            f.write(str(list2[i]) + '\n')
    target.to_csv(path + "/target.csv",index=None)
    data_rfe.to_csv(path + "/data_rfe.csv",index=None)
    return target,data_rfe


def heatmap_afterRFE(path):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    data_rfe_corMat = pd.DataFrame(data_rfe.corr())
    plt.figure(figsize=(20, 30))
    sns.heatmap(data_rfe_corMat, annot=False, vmax=1, square=True, cmap="Blues",linewidths=0)
    plt.savefig(path+'/heatmap-afterRFE.png', dpi=300, bbox_inches = 'tight')
    plt.close()



def pairplot_afterRFE(path):
    import seaborn as sns
    import matplotlib.pyplot as plt
    g6 = sns.pairplot(data_rfe, kind='reg')
    plt.savefig(path+'/sns-pairplot-remain.png', dpi=300, bbox_inches = 'tight')
    plt.close()



def FeatureImportance_before(rotationDeg,fontsize_axis,figure_size_xaxis,figure_size_yaxis,path):

    import pandas as pd
    featureData = data.iloc[:, :]
    corMat = pd.DataFrame(featureData.corr())
    FirstLine=corMat.iloc[-1,:]
    FirstLine=pd.DataFrame(FirstLine)
    FirstLine_Del_Target=FirstLine.iloc[:-1,:]
    importance=FirstLine_Del_Target.sort_values(by=FirstLine_Del_Target.columns.tolist()[-1],ascending=False)
    # importance=FirstLine_Del_Target.sort_values(by="Potential (v)",ascending=False)
    try:
        print(importance)
    except Exception as e:
        print(e)
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['Times New Roman']
    # plt.rcParams ['font.sans-serif'] ='SimHei'    #显示中文
    plt.rcParams ['axes.unicode_minus']=False    #显示负号
    importance.plot(kind='bar', figsize=(figure_size_xaxis,figure_size_yaxis), rot=rotationDeg, fontsize=8)  #colormap='rainbow'

    plt.savefig(path+'/FeatureImportance_before.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return importance

#5.2 特征选择之后的个别特征的重要性
def FeatureImportance_afterRFE(rotationDeg, fontsize_axis, figure_size_xaxis, figure_size_yaxis,path):
    import pandas as pd
    corMat_rfe = pd.DataFrame(data_rfe.corr())  # corr 求相关系数矩阵

    FirstLine_rfe = corMat_rfe.iloc[-1, :]
    FirstLine_rfe = pd.DataFrame(FirstLine_rfe)
    FirstLine_rfe_Del_Target = FirstLine_rfe.iloc[:-1, :]
    # importance_rfe = FirstLine_rfe_Del_Target.sort_values(by="Potential (v)", ascending=False)
    importance_rfe = FirstLine_rfe_Del_Target.sort_values(by=FirstLine_rfe_Del_Target.columns.tolist()[-1],ascending=False)
    print(importance_rfe)

    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号
    importance_rfe.plot(kind='bar', figsize=(figure_size_xaxis, figure_size_yaxis), rot=rotationDeg,
                        fontsize=8)  # colormap='rainbow'
    plt.savefig(path+'/FeatureImportance_after.png', dpi=300, bbox_inches='tight')
    plt.close()
    return importance_rfe



#6 机器学习建模
# 6.1.1 xgboost默认超参数建模画图
# (n_estimators=2000, max_depth=100, eta=0.1, gamma=0,
# subsample=0.9, colsample_bytree=0.9, learning_rate=0.2)
def xgboost_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split


    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])




    #xgboost建模
    from xgboost import XGBRegressor
    global clf_xgboost_default
    clf_xgboost_default = XGBRegressor(n_estimators=2000, max_depth=100, eta=0.1, gamma=0,
                       subsample=0.9, colsample_bytree=0.9, learning_rate=0.2)
    clf_xgboost_default.fit(X_train, y_train)

    y_prediction=clf_xgboost_default.predict(X_test)


    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)


    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse)+'\n'+"MAE:"+str(MAE)+'\n'+"R2:"+str(R2)+'\n'+"MSE:"+str(MSE)+'\n'


    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)

    plt.tick_params(width=2)                                                  # 刻度线宽度
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)                                   # 控制主次刻度线的长度，宽度
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(10000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)

    plt.axis('tight')
    plt.minorticks_on()

    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)

    #plt.text(.05, .2, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center',transform=ax.transAxes)
    plt.savefig(path+'/xgboost-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()




    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf_xgboost_default, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    print(type(scores))

    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)

    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    #     ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    #     xminorLocator   = MultipleLocator(1000)
    #     yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    #     plt.xlim(1.5,9.5)
    plt.ylim(0, 1.2)
    #     plt.minorticks_on()
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/xgboost-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()





    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf_xgboost_default.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    #plt.text(.05, .2, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center',transform=ax.transAxes)
    plt.savefig(path+'/xgboost-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2


# 6.1.2 xgboost自己修改超参数, 建模
# 画图得到拟合图以及交叉验证图
# (n_estimators=2000xxx, max_depth=100xxx, eta=0.1xxx, gamma=0xxx,
# subsample=0.9xxx, colsample_bytree=0.9xxx, learning_rate=0.2xxx)

def xgboost_modify(a, b, c, d, e, f, g,path,csvName):
    # 数据切分
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt  # 计算准确率xgboost
    from sklearn.model_selection import train_test_split
    import pandas as pd

    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""
    data = pd.DataFrame(pd.read_csv(csvName))

    X = data.values[:, :-1]
    y = data.values[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    # xgboost建模
    from xgboost import XGBRegressor
    global clf_xgboost_modify
    clf_xgboost_modify = XGBRegressor(n_estimators=a, max_depth=b, eta=c, gamma=d,
                       subsample=e, colsample_bytree=f, learning_rate=g)
    clf_xgboost_modify.fit(X_train, y_train)
    Continuous_Xgboost=clf_xgboost_modify.fit(X_train, y_train)
    y_prediction = clf_xgboost_modify.predict(X_test)

    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)

    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    # plt.gcf().text(.05, .2, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
    #          size=20, horizontalalignment='center')
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path+'/xgboost-modify-test.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf_xgboost_modify, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)

    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    #     ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    #     xminorLocator   = MultipleLocator(1000)
    #     yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    #     plt.xlim(1.5,9.5)
    plt.ylim(0, 1.2)
    #     plt.minorticks_on()
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/xgboost_modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf_xgboost_modify.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/xgboost-modify-train-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_Xgboost, open(path+"/Continuous_Xgboost.dat", "wb"))
    return str1, scores, str2



# 6.1.3 xgboost randomSearchCV, 包含了交叉验证
def xgboost_RandomSearchCV(path):
    # 数据切分
    import numpy as np
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt  # 计算准确率xgboost
    from sklearn.model_selection import train_test_split

    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    # 尝试random search
    from sklearn.model_selection import RandomizedSearchCV
    from xgboost import XGBRegressor

    param_distribs = {
        'n_estimators': range(80, 200, 40),
        'max_depth': range(2, 15, 4),
        'learning_rate': np.linspace(0.01, 2, 4),
        'subsample': np.linspace(0.7, 0.9, 4),
        'colsample_bytree': np.linspace(0.5, 0.98, 4),
        'min_child_weight': range(1, 9, 3)
    }

    clf = XGBRegressor()
    global rnd_search_cv_xgboost
    rnd_search_cv_xgboost = RandomizedSearchCV(clf, param_distribs, n_iter=300, cv=10, scoring='neg_mean_squared_error')
    rnd_search_cv_xgboost.fit(X_train, y_train)
    y_prediction = rnd_search_cv_xgboost.predict(X_test)

    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)

    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)

    print("RMSE:", rmse)
    print("MAE:", MAE)

    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)

    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()

    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)

    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path+'/xgboost-RandomizedSearchCV.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(rnd_search_cv_xgboost, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)

    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    #     ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    #     xminorLocator   = MultipleLocator(1000)
    #     yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    #     plt.xlim(1.5,9.5)
    plt.ylim(0, 1.2)
    #     plt.minorticks_on()
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/Xgboost_rnd_search_cv-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()

   # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/xgboost-train-randomSearch.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2



# 6.1.4 xgboost GridSearchCV网格搜索（不随机）, 包含了交叉验证
def xgboost_GridSearchCV(path):
    # 数据切分
    import numpy as np
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt  # 计算准确率xgboost
    from sklearn.model_selection import train_test_split

    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    # 尝试random search
    from sklearn.model_selection import GridSearchCV
    from xgboost import XGBRegressor

    param_distribs = {
        'n_estimators': range(80, 200, 30),
        'max_depth': range(2, 15, 3),
        'learning_rate': np.linspace(0.01, 2, 4),
        'subsample': np.linspace(0.7, 0.9, 4),
        'colsample_bytree': np.linspace(0.5, 0.98, 4),
        'min_child_weight': range(1, 9, 3)
    }

    clf = XGBRegressor()
    grid_search_cv = GridSearchCV(clf, param_distribs, n_iter=300, cv=10, scoring='neg_mean_squared_error')
    grid_search_cv.fit(X_train, y_train)
    y_prediction = grid_search_cv.predict(X_test)

    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)

    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)

    print("RMSE:", rmse)
    print("MAE:", MAE)

    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)

    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()

    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)

    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path+'/xgboost-GridSearchCV.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(grid_search_cv, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)

    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    #     ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    #     xminorLocator   = MultipleLocator(1000)
    #     yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    #     plt.xlim(1.5,9.5)
    plt.ylim(0, 1.2)
    #     plt.minorticks_on()
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/grid_search_cv-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()

   # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Xgboost-grid_search_train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2




#6.2 随机森林机器学习建模
# 6.2.1 随机森林默认超参数建模画图
def RandomForest_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split

    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    #Random forest建模
    from sklearn import ensemble
    global clf_rf_default
    clf_rf_default = ensemble.RandomForestRegressor()
    clf_rf_default.fit(X_train, y_train)

    RF=clf_rf_default.fit(X_train, y_train)

    y_prediction=clf_rf_default.predict(X_test)

    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)

    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()

    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)

    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/randomForest-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()

    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf_rf_default, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)

    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    #     ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    #     xminorLocator   = MultipleLocator(1000)
    #     yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    #     plt.xlim(1.5,9.5)
    plt.ylim(0, 1.2)
    #     plt.minorticks_on()
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/randomForest-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()


    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf_rf_default.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/randomForest-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2



# 6.2.2 Random forest modify 自己修改超参数, 建模
def RandomForest_modify(a, b, c, d, e,path,csvname):
# max_depth, max_features, min_samples_split, n_estimators, random_state
# 20, 0.3, 2, 10, 10
    # 数据切分
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # RandomForest建模
    from sklearn import ensemble
    clf = ensemble.RandomForestRegressor(max_depth=a,max_features=b, min_samples_split=c, n_estimators=d,random_state=e)
    clf.fit(X_train, y_train)
    Continuous_RF=clf.fit(X_train, y_train)
    y_prediction = clf.predict(X_test)
    #看是否有预测集
    # if xxx:
    #     pass
    # else:
    #     print(clf.predict(input))
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse)+'\n'+"MAE:"+str(MAE)+'\n'+"R2:"+str(R2)+'\n'+"MSE:"+str(MSE)+'\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path+'/RandomForest-modify-test.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:",scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i+1,"scores_mean:",scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/RandomForest_modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
            + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/RandomForest-modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_RF, open(path+"/Continuous_RF.dat", "wb"))
    return str1,scores,str2



def RandomForest_GridSearch(path,csvname):
# max_depth, max_features, min_samples_split, n_estimators, random_state
# 20, 0.3, 2, 10, 10
    # 数据切分
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]

    # 数据归一化处理
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # 将归一化后的数据分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=4)
    # 设置参数范围
    param_grid = [
        {'n_estimators': [20,30,50, 100],
         'max_depth': [None, 10, 20],
         'min_samples_split': [2, 5, 10],
         'min_samples_leaf': [1, 2, 4],
         'max_features': ['auto', 'sqrt', 'log2']}
    ]

    # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
    # # 数据归一化
    # for i in range(X_train.shape[1]):
    #     X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    # for i in range(X_test.shape[1]):
    #     X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # RandomForest建模
    from sklearn import ensemble
    # clf = ensemble.RandomForestRegressor(max_depth=a,max_features=b, min_samples_split=c, n_estimators=d,random_state=e)

    from sklearn.model_selection import train_test_split, GridSearchCV
    # 创建随机森林模型
    random_forest_model = RandomForestRegressor()
    # 使用网格搜索进行参数优化
    grid_search = GridSearchCV(estimator=random_forest_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', verbose=2, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # 打印最佳参数
    print("Best parameters found: ", grid_search.best_params_)

    # 使用最佳参数的模型进行预测
    best_model = grid_search.best_estimator_
    y_train_prediction = best_model.predict(X_train)
    y_prediction = best_model.predict(X_test)

    # clf.fit(X_train, y_train)
    # Continuous_RF=clf.fit(X_train, y_train)
    # y_prediction = grid_search.predict(X_test)

    #看是否有预测集
    # if xxx:
    #     pass
    # else:
    #     print(clf.predict(input))
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse)+'\n'+"MAE:"+str(MAE)+'\n'+"R2:"+str(R2)+'\n'+"MSE:"+str(MSE)+'\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path+'/RandomForest-GridSearch-test.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(best_model, X_scaled, y, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:",scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i+1,"scores_mean:",scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/RandomForest-GridSearch-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    # y_train_prediction = grid_search.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
            + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/RandomForest-GridSearch-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(best_model, open(path+"/Continuous_RF-GridSearch.dat", "wb"))
    return str1,scores,str2


from sklearn import ensemble
def Bagging_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn import ensemble
    clf = ensemble.BaggingRegressor()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Bagging-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/Bagging-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Bagging-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.3.2 bagging自定义超参数建模画图
def Bagging_modify(a, b, c,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    # 数据切分
    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn import ensemble
    clf = ensemble.BaggingRegressor(n_estimators=a,max_samples=b, max_features=c)
    clf.fit(X_train, y_train)
    Continuous_Bagging=clf.fit(X_train, y_train)
    y_prediction = clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path + '/Bagging-modify-test.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path + '/Bagging-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:", R2_train)
    print("MSE:", MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train),
             fontproperties='Times New Roman', size=20, horizontalalignment='center')
    plt.savefig(path + '/Bagging-modify-train.png', dpi=300, bbox_inches='tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_Bagging, open(path + "/Continuous_Bagging.dat", "wb"))
    return str1, scores, str2


#6.4 AdaBoost机器学习建模
# 6.4.1 AdaBoost默认超参数建模画图

from sklearn import ensemble
def AdaBoost_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn import ensemble
    clf = ensemble.AdaBoostRegressor()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/AdaBoost-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/AdaBoost-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/AdaBoost-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.4.2 AdaBoost自定义超参数建模画图
def AdaBoost_modify(a, b, c,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    # 数据切分
    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn import ensemble


    if c==0.3:
        loss1='exponential'
    elif c==0.2:
        loss1 = 'square'
    else:
        loss1 = 'linear'



    clf = ensemble.AdaBoostRegressor(n_estimators=a,learning_rate=b,loss=loss1)
    clf.fit(X_train, y_train)
    Continuous_AdaBoost=clf.fit(X_train, y_train)
    y_prediction = clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path + '/AdaBoost-modify.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path + '/AdaBoost-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:", R2_train)
    print("MSE:", MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train),
             fontproperties='Times New Roman', size=20, horizontalalignment='center')
    plt.savefig(path + '/AdaBoost-modify-train.png', dpi=300, bbox_inches='tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_AdaBoost, open(path + "/Continuous_AdaBoost.dat", "wb"))
    return str1, scores, str2


#6.5 GradientBoosting机器学习建模
# 6.5.1 GradientBoosting默认超参数建模画图

from sklearn import ensemble
def GradientBoosting_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn import ensemble
    clf = ensemble.GradientBoostingRegressor()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/GradientBoosting-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/GradientBoosting-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/GradientBoosting-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.5.2 GradientBoosting自定义超参数建模画图
def GradientBoosting_modify(a, b, c,d,e,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn import ensemble
    # (n_estimators': 100, 'max_depth': 3, 'min_samples_split': 2,'min_samples_leaf': 1,'learning_rate': 0.1)
    clf = ensemble.GradientBoostingRegressor(n_estimators=a, max_depth= b,min_samples_split=c,min_samples_leaf=int(d),learning_rate= e)
    clf.fit(X_train, y_train)
    Continuous_GradientBoosting = clf.fit(X_train, y_train)
    y_prediction = clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path + '/GradientBoosting-modify.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path + '/GradientBoosting-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:", R2_train)
    print("MSE:", MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train),
             fontproperties='Times New Roman', size=20, horizontalalignment='center')
    plt.savefig(path + '/GradientBoosting-modify-train.png', dpi=300, bbox_inches='tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_GradientBoosting, open(path + "/Continuous_GradientBoosting.dat", "wb"))
    return str1, scores, str2

#6.6 ExtraTree机器学习建模
# 6.6.1 ExtraTree默认超参数建模画图

def ExtraTree_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.tree import ExtraTreeRegressor
    clf = ExtraTreeRegressor()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/ExtraTree-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/ExtraTree-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/ExtraTree-modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.6.2 ExtraTree自定义超参数建模画图
def ExtraTree_modify(a, b, c,e,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    # 机器学习建模
    from sklearn.tree import ExtraTreeRegressor

    if a==0:
        max_depth1=None
    else:
        max_depth1=a
    if b==0.1:
        max_features1='sqrt'
    elif b==0.2:
        max_features1 = 'log2'
    elif b == 0:
        max_features1 = None
    elif b == 0.3:
        max_features1 = 'auto'
    else:
        max_features1 = b
    if e==0:
        random_state1=None
    else:
        random_state1=e
    # max_depth=None,max_features['sqrt', 'log2', None,'auto']='auto',min_samples_split=2,random_state=None
    clf = ExtraTreeRegressor(max_depth=max_depth1,max_features=max_features1,min_samples_split=c,
                             random_state=random_state1)
    clf.fit(X_train, y_train)
    Continuous_ExtraTree = clf.fit(X_train, y_train)
    y_prediction = clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:", rmse)
    print("MAE:", MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:", R2)
    print("MSE:", MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    # plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties='Times New Roman',
             size=20, horizontalalignment='center')
    plt.savefig(path + '/ExtraTree-modify.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path + '/ExtraTree-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1 / 2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:", R2_train)
    print("MSE:", MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator = MultipleLocator(1000)
    yminorLocator = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties='Times New Roman', size=20)
    plt.ylabel("Prediction", fontproperties='Times New Roman', size=20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train),
             fontproperties='Times New Roman', size=20, horizontalalignment='center')
    plt.savefig(path + '/ExtraTree-modify-train.png', dpi=300, bbox_inches='tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_ExtraTree, open(path+"/Continuous_ExtraTree.dat", "wb"))
    return str1, scores, str2


# 6.7 svm机器学习建模

# 6.7.1 svm默认超参数建模画图
def svm_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn import svm
    clf = svm.SVR()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/svm-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/svm-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()

    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/svm-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.7.2 Svm自定义超参数建模画图
def Svm_modify(a, b,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn import svm
    #C=1.0, epsilon=0.1
    clf = svm.SVR(C=a, epsilon=b)
    clf.fit(X_train, y_train)
    Continuous_Svm = clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Svm-modify.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/Svm-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Svm-modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_Svm, open(path + "/Continuous_Svm.dat", "wb"))
    return str1, scores, str2



# 6.8.2 DecisionTree自定义超参数建模画图
def DecisionTree_modify(a, b,c,d,e,f,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn import tree
    # max_depth=None,max_features=None,min_samples_split=2,min_samples_leaf=1,random_state=None,max_leaf_nodes=None
    if a==0:
        max_depth1=None
    else:
        max_depth1=a
    if b==0.1:
        max_features1='sqrt'
    elif b==0.2:
        max_features1 = 'log2'
    elif b == 0:
        max_features1 = None
    elif b == 0.3:
        max_features1 = 'auto'
    else:
        max_features1 = b
    if e==0:
        random_state1=None
    else:
        random_state1=e
    if f==0:
        max_leaf_nodes1=None
    else:
        max_leaf_nodes1=f
    clf = tree.DecisionTreeRegressor(max_depth=max_depth1,max_features=max_features1,min_samples_split=c,
                                     min_samples_leaf=d,random_state=random_state1,max_leaf_nodes=max_leaf_nodes1)
    clf.fit(X_train, y_train)
    Continuous_DecisionTree = clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/DecisionTree-modify.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/DecisionTree-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/DecisionTree-modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_DecisionTree, open(path + "/Continuous_DecisionTree.dat", "wb"))
    return str1, scores, str2



# 6.9 LinearRegression机器学习建模

# 6.9.1 LinearRegression默认超参数建模画图
def LinearRegression_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.linear_model import LinearRegression
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # datasave = pd.DataFrame([[y_test], [y_prediction]])
    # datasave = pd.DataFrame({'y_test': y_test, 'y_prediction': y_prediction})
    # datasave.to_csv("LR-test.csv")
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/LinearRegression-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/LinearRegression-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/LinearRegression-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.9.2 LinearRegression自定义超参数建模画图
def LinearRegression_modify(a, b,c,d,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.linear_model import LinearRegression
    # fit_intercept=True, normalize=False, copy_X=True, n_jobs=None
    if a==0:
        fit_intercept1=False
    else:
        fit_intercept1 = True
    if b==0:
        normalize1=False
    else:
        normalize1 = True
    if c==0:
        copy_X1=False
    else:
        copy_X1 = True
    if d==0:
        n_jobs1=None
    else:
        n_jobs1 = d
    clf = LinearRegression(fit_intercept=fit_intercept1, normalize=normalize1, copy_X=copy_X1, n_jobs=n_jobs1)
    clf.fit(X_train, y_train)

    Continuous_LinearRegression = clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # datasave = pd.DataFrame([[y_test], [y_prediction]])
    # datasave = pd.DataFrame({'y_test': y_test, 'y_prediction': y_prediction})
    # datasave.to_csv("LR-test.csv")
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/LinearRegression-modify.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/LinearRegression-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/LinearRegression-modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_LinearRegression, open(path + "/Continuous_LinearRegression.dat", "wb"))
    return str1, scores, str2


# 6.10 Ridge机器学习建模

# 6.10.1 Ridge默认超参数建模画图
def Ridge_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.linear_model import Ridge
    clf = Ridge()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Ridge-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/Ridge-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Ridge-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2

# 6.10.2 Ridge自定义超参数建模画图
def Ridge_modify(a, b,c,d,e,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.linear_model import Ridge
    # alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, random_state=None
    if b==0:
        fit_intercept1=False
    else:
        fit_intercept1 = True
    if c==0:
        normalize1=False
    else:
        normalize1 = True
    if d==0:
        copy_X1=False
    else:
        copy_X1 = True
    if e==0:
        random_state1=None
    else:
        random_state1=e
    clf = Ridge(alpha=a, fit_intercept=fit_intercept1, normalize=normalize1, copy_X=copy_X1, random_state=random_state1)
    clf.fit(X_train, y_train)
    Continuous_Ridge = clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Ridge-modify.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/Ridge-modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/Ridge-modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_Ridge, open(path + "/Continuous_Ridge.dat", "wb"))
    return str1, scores, str2


# 6.11 MLP机器学习建模

# 6.11.1 MLP默认超参数建模画图
def MLP_default(path):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # 数据切分
    X = s_rfe
    y = target
    X = X.values[:, :-1]
    y = y.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.neural_network import MLPRegressor
    clf = MLPRegressor()
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/MLP-default.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/MLP-default-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/MLP-default-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    return str1, scores, str2


# 6.11.2 MLP_modify手动修改超参数建模画图
def MLP_modify(l,a,m,ha,hb,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    """X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]"""

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # 数据归一化
    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
    #机器学习建模
    from sklearn.neural_network import MLPRegressor
    # 0.01,0.0001,200000,200,200
    clf = MLPRegressor(solver='lbfgs', activation='relu', learning_rate_init=l, alpha=a, max_iter=m,
                 hidden_layer_sizes=(ha, hb))

    Continuous_MLP = clf.fit(X_train, y_train)
    clf.fit(X_train, y_train)
    y_prediction=clf.predict(X_test)
    # 打印准确率
    mse = mean_squared_error(y_test, y_prediction)
    rmse = mse ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE = mean_absolute_error(y_test, y_prediction)
    print("RMSE:",rmse)
    print("MAE:",MAE)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2 = r2_score(y_test, y_prediction)
    MSE = mean_squared_error(y_test, y_prediction)
    print("R2:",R2)
    print("MSE:",MSE)
    str1 = "RMSE:" + str(rmse) + '\n' + "MAE:" + str(MAE) + '\n' + "R2:" + str(R2) + '\n' + "MSE:" + str(MSE) + '\n'

    #plot图
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_test, y_test, label='Real Data')
    plt.scatter(y_test, y_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE, MSE, R2), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/MLP_modify.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    # 使用KFold交叉验证建模
    from sklearn.model_selection import cross_val_score
    kfold = KFold(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, scoring='r2', cv=kfold)
    # scoring='neg_mean_squared_error'
    print("scores:", scores)
    scores_fold = []
    for i in range(len(scores)):
        scores_mean = scores[:i + 1].mean()
        print(i + 1, "scores_mean:", scores_mean)
        scores_fold.append(scores_mean)
    # 使用KFold交叉验证plot图
    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(range(1, 11), scores_fold, c='r')
    plt.scatter(range(1, 11), scores_fold, c='r')
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4, width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    y_major_locator = MultipleLocator(0.2)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
    plt.ylim(0, 1.2)
    plt.xlabel("k", fontproperties='Times New Roman', size=24)
    plt.ylabel("score", fontproperties='Times New Roman', size=24)
    plt.savefig(path+'/MLP_modify-10-fold-crossvalidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    # 训练集也可以打印准确率并plot图
    y_train_prediction = clf.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_prediction)
    rmse_train = mse_train ** (1/2)
    from sklearn.metrics import mean_absolute_error
    MAE_train = mean_absolute_error(y_train, y_train_prediction)
    print("RMSE:", rmse_train)
    print("MAE:", MAE_train)
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    R2_train = r2_score(y_train, y_train_prediction)
    MSE_train = mean_squared_error(y_train, y_train_prediction)
    print("R2:",R2_train)
    print("MSE:",MSE_train)
    str2 = "RMSE:" + str(rmse_train) + '\n' + "MAE:" + str(MAE_train) + '\n' + "R2:" + str(R2_train) + '\n' \
           + "MSE:" + str(MSE_train) + '\n'

    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.rcParams['font.sans-serif'] = 'Roman'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(y_train, y_train, label='Real Data')
    plt.scatter(y_train, y_train_prediction, label='Predict', c='r')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2)
    plt.tick_params(width=2)
    ax.xaxis.set_tick_params(labelsize=24)
    plt.tick_params(which='major',length=8)
    plt.tick_params(which='minor',length=4,width=2)
    ax.yaxis.set_tick_params(labelsize=24)
    xminorLocator   = MultipleLocator(1000)
    yminorLocator   = MultipleLocator(1000)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    plt.minorticks_on()
    plt.xlabel("True", fontproperties = 'Times New Roman', size = 20)
    plt.ylabel("Prediction", fontproperties = 'Times New Roman', size = 20)
    plt.gcf().text(0.0, -0.3, 'MAE = %.3f \nMSE =  %.3f \nR2 =  %.3f \n' % (MAE_train, MSE_train, R2_train), fontproperties = 'Times New Roman', size = 20, horizontalalignment='center')
    plt.savefig(path+'/MLP_modify-train.png', dpi=300, bbox_inches = 'tight')
    plt.close()
    import pickle
    pickle.dump(Continuous_MLP, open(path + "/Continuous_MLP.dat", "wb"))
    return str1, scores, str2


def dnn_regressor_modify(a, b, c, path, csvname):
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    import matplotlib.pyplot as plt
    import tensorflow as tf
    import pandas as pd

    # 加载数据
    data = pd.read_csv(csvname)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    # 数据划分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 数据标准化
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 构建模型
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['mean_squared_error'])

    # 训练模型
    history = model.fit(X_train_scaled, y_train, epochs=a, batch_size=b, validation_split=c)

    # 评估模型
    loss, mse = model.evaluate(X_test_scaled, y_test)
    print("Test MSE:", mse)

    # 预测测试数据
    y_pred_test = model.predict(X_test_scaled)

    # 预测训练数据
    y_pred_train = model.predict(X_train_scaled)

    # 计算指标
    rmse_test = mean_squared_error(y_test, y_pred_test, squared=False)
    mae_test = mean_absolute_error(y_test, y_pred_test)
    r2_test = r2_score(y_test, y_pred_test)

    rmse_train = mean_squared_error(y_train, y_pred_train, squared=False)
    mae_train = mean_absolute_error(y_train, y_pred_train)
    r2_train = r2_score(y_train, y_pred_train)

    # 打印指标
    print("Test RMSE:", rmse_test)
    print("Test MAE:", mae_test)
    print("Test R2:", r2_test)

    print("Train RMSE:", rmse_train)
    print("Train MAE:", mae_train)
    print("Train R2:", r2_train)

    # 绘制训练和验证损失曲线
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.savefig(path + '/DNN_loss_curve.png')
    plt.close()

    # 绘制预测值与真实值散点图
    plt.scatter(y_test, y_pred_test)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('Predictions vs True Values (Test Set)')
    plt.savefig(path + '/DNN_predictions_vs_true_test.png')
    plt.close()

    plt.scatter(y_train, y_pred_train)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('Predictions vs True Values (Train Set)')
    plt.savefig(path + '/DNN_predictions_vs_true_train.png')
    plt.close()

    # 保存模型
    model.save(path + '/dnn_model.h5')

    # 返回指标字符串
    return f"Test RMSE: {rmse_test}\nTest MAE: {mae_test}\nTest R2: {r2_test}\nTrain RMSE: {rmse_train}\nTrain MAE: {mae_train}\nTrain R2: {r2_train}"


# 10.1
def randomforest_Classifier(a, b, c, d, e, f,path,csvName):
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))


    X = data.values[:, :-1]
    y = data.values[:, -1]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import train_test_split

    param_grid = {
        'n_estimators': [50, 80, 100, 120],
        'max_depth': [6, 7],
        'min_samples_split': [2],
        'min_samples_leaf': [1, 2, 4],
        'max_features': [1, 2],
        'random_state': [0, 1]
    }

    # Create a RandomForestClassifier object
    rfc = RandomForestClassifier()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)

    # Fit the GridSearchCV object to the data
    grid_search.fit(X_train, y_train)

    # Print the best parameters and score
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {grid_search.best_score_}")
    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Best score: {grid_search.best_score_}"

    clf = RandomForestClassifier(max_depth=a, random_state=b, min_samples_leaf=c, max_features=d, min_samples_split=e,
                                 n_estimators=f)
    # clf.fit(X_train, y_train)
    Classified_two_RF = clf.fit(X_train, y_train)

    # 画出ROC曲线 RandomForest test
    y_score = Classified_two_RF.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)


    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/RandomForest_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest test
    # clf.fit(X, y)
    prey = Classified_two_RF.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/RandomForest_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    # 画出ROC曲线 RandomForest train的AUC
    y_score = Classified_two_RF.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/RandomForest_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest train 混淆矩阵
    prey = Classified_two_RF.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/RandomForest_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    pickle.dump(Classified_two_RF, open(path+"/Classified_two_RF.dat", "wb"))

    return str1,str2,str3

# 10.2
def extratrees_classifier(a, b, c, d, e, f,path,csvName):
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.ensemble import ExtraTreesClassifier

    from sklearn.datasets import make_classification
    from sklearn.metrics import accuracy_score, make_scorer

    # # Generate some data for classification
    # X, y = X_train, y_train

    # Define the ExtraTreesClassifier
    et_clf = ExtraTreesClassifier()

    # Define the parameters to search
    params = {
        'n_estimators': [2, 50, 100, 200],
        'max_depth': [None, 5, 7, 10],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2', None]
    }

    # Define the scoring metric
    scoring = make_scorer(accuracy_score)

    # Define the grid search with cross-validation
    grid_search = GridSearchCV(et_clf, params, scoring=scoring, cv=5, n_jobs=-1)

    # Fit the grid search to the data
    grid_search.fit(X, y)

    # Print the best parameters and best score
    print("Best Parameters: ", grid_search.best_params_)
    print("Best Score: ", grid_search.best_score_)
    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Best score: {grid_search.best_score_}"

    if b==0:
        max_depth1=None
    else:
        max_depth1=b
    if e==0.1:
        max_features1='sqrt'
    elif e==0.2:
        max_features1 = 'log2'
    elif e == 0:
        max_features1 = None
    else:
        max_features1 = e


    clf = ExtraTreesClassifier(n_estimators=a, max_depth=max_depth1, min_samples_split=c, random_state=d, max_features=max_features1,
                               min_samples_leaf=f)

    Classified_two_ExtraTrees = clf.fit(X_train, y_train)
    # 画出ROC曲线 ExtraTrees test
    y_score = Classified_two_ExtraTrees.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    #plt.show()
    plt.savefig(path + '/ExtraTrees_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 ExtraTrees
    prey = Classified_two_ExtraTrees.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/ExtraTrees_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    # 画出ROC曲线 ExtraTrees train
    y_score = Classified_two_ExtraTrees.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    #plt.show()
    plt.savefig(path + '/ExtraTrees_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest train 混淆矩阵
    prey = Classified_two_ExtraTrees.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/ExtraTrees_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    import pickle
    pickle.dump(Classified_two_ExtraTrees, open(path + "/Classified_two_ExtraTrees.dat", "wb"))
    return str1, str2, str3

# 10.3
def GaussianProcess_classifier(a, b, c, d, e,path,csvName):
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.datasets import make_classification

    # Define the parameter grid to search over
    param_grid = {
        "kernel": [1.0 * RBF(length_scale=1.0)],
        "optimizer": ['fmin_l_bfgs_b'],
        "n_restarts_optimizer": [0, 1, 2],
        "max_iter_predict": [5, 10, 30, 40, 50, 100]
    }

    # Create a GaussianProcessClassifier object
    clf = GaussianProcessClassifier()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(clf, param_grid=param_grid, cv=5)

    # Fit the GridSearchCV object to the training data
    grid_search.fit(X_train, y_train)

    # Print the best parameters found by GridSearchCV
    print("Best parameters found:", grid_search.best_params_)

    # Evaluate the best estimator on the test data
    print("Test accuracy:", grid_search.score(X_test, y_test))

    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Test accuracy: {grid_search.score(X_test, y_test)}"

    if e==0:
        clf = GaussianProcessClassifier(kernel=a * RBF(length_scale=b), max_iter_predict=c, n_restarts_optimizer=d,
                                        optimizer='fmin_l_bfgs_b')
    Classified_two_GaussianProcess = clf.fit(X_train, y_train)

    # 画出ROC曲线 GaussianProcess test
    y_score = Classified_two_GaussianProcess.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/GaussianProcess_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 GaussianProcess test
    prey = Classified_two_GaussianProcess.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/GaussianProcess_test_CM.png', dpi=300, bbox_inches='tight')
    print("true:", true)
    str2 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    # 画出ROC曲线 GaussianProcess train
    y_score = Classified_two_GaussianProcess.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/GaussianProcess_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 GaussianProcess train
    prey = Classified_two_GaussianProcess.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/GaussianProcess_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    import pickle
    pickle.dump(Classified_two_GaussianProcess, open(path + "/Classified_two_GaussianProcess.dat", "wb"))
    return str1, str2, str3

# 10.4
# def KNeighbors_classifier(a, b, c, d, e, f,csvName,path):
#     import matplotlib.pyplot as plot
#     import seaborn as sns
#     import matplotlib.pyplot as plt
#     from sklearn import svm
#     import numpy as np
#     import pandas as pd
#     from sklearn import preprocessing
#     from pandas import DataFrame
#     from sklearn.ensemble import RandomForestClassifier
#     from sklearn.ensemble import ExtraTreesClassifier
#     from sklearn.gaussian_process import GaussianProcessClassifier
#     from sklearn.gaussian_process.kernels import RBF
#     from sklearn.model_selection import KFold
#     from sklearn.metrics import roc_curve, auc
#     from sklearn.metrics import confusion_matrix
#     from sklearn.model_selection import train_test_split
#     from sklearn.metrics import accuracy_score
#     from sklearn.metrics import f1_score
#     from sklearn.tree import DecisionTreeClassifier
#     from sklearn.neighbors import KNeighborsClassifier
#     from sklearn.svm import SVC
#     from sklearn.model_selection import GridSearchCV
#     from sklearn.metrics import classification_report
#     import pickle
#
#     data = pd.DataFrame(pd.read_csv(csvName))
#
#     X = data.values[:, :-1]
#     y = data.values[:, -1]
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
#
#     for i in range(X_train.shape[1]):
#         X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
#
#     for i in range(X_test.shape[1]):
#         X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])
#
#     clf = KNeighborsClassifier(n_neighbors=8)
#     Classified_KNeighbors = clf.fit(X_train, y_train)
#
#     # 画出ROC曲线 KNeighbors test
#     y_score = Classified_KNeighbors.predict_proba(X_test)
#     fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
#     roc_auc = auc(fpr, tpr)
#     plt.figure()
#     lw = 2
#     plt.figure(figsize=(10, 10))
#     plt.plot(fpr, tpr, color='darkorange',
#              lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
#     print(fpr)
#     print(tpr)
#     plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
#     plt.xlim([0.01, 1.0])
#     plt.ylim([0, 1.05])
#     plt.xlabel('False Positive Rate', fontsize=20)
#     plt.ylabel('True Positive Rate', fontsize=20)
#     plt.xticks(fontsize=20)
#     plt.yticks(fontsize=20)
#
#     plt.title('AUC')
#     plt.legend(loc="lower right", fontsize=20, frameon=False)
#     plt.show()
#
#     # 画出混淆矩阵 KNeighbors test
#     prey = Classified_KNeighbors.predict(X_test)
#     true = 0
#     for i in range(0, len(y_test)):
#         if prey[i] == y_test[i]:
#             true = true + 1
#     C = confusion_matrix(y_test, prey, labels=[0, 1])
#     plt.imshow(C, cmap=plt.cm.Blues)
#     indices = range(len(C))
#     plt.xticks(indices, [0, 1], fontsize=20)
#     plt.yticks(indices, [0, 1], fontsize=20)
#     plt.colorbar()
#     for first_index in range(len(C)):  # 第几行
#         for second_index in range(len(C)):  # 第几列
#             plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
#     plt.show()
#     print("true:", true)
#
#     from sklearn.metrics import accuracy_score
#     score = []
#     for K in range(40):
#         K_value = K + 1
#         knn = KNeighborsClassifier(n_neighbors=K_value, weights='uniform', algorithm='auto')
#         knn.fit(X_train, y_train)
#         y_pred = knn.predict(X_test)
#         score.append(round(accuracy_score(y_test, y_pred) * 100, 2))
#
#     plt.figure(figsize=(12, 6))
#     plt.plot(range(1, 41), score, color='red', linestyle='dashed', marker='o',
#              markerfacecolor='blue', markersize=10)
#     plt.title('The Learning curve')
#     plt.xlabel('K Value')
#     plt.ylabel('Score')

# 10.5
def DecisionTree_classifier(a, b, c, d, e,path,csvName):
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import GridSearchCV
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    # Define the parameter grid to search over
    param_grid = {
        'criterion': ['gini', 'entropy'],
        'max_depth': [5, 10, 15, 20, None],
        'min_samples_split': [2, 5, 10, 15],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['auto', 'sqrt', 'log2', None]
    }

    # Create a DecisionTreeClassifier object
    dtc = DecisionTreeClassifier()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(dtc, param_grid=param_grid, cv=5)

    # Fit the GridSearchCV object to the training data
    grid_search.fit(X_train, y_train)

    # Print the best parameters found by GridSearchCV
    print("Best parameters found:", grid_search.best_params_)

    # Evaluate the best estimator on the test data
    print("Test accuracy:", grid_search.score(X_test, y_test))

    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Test accuracy: {grid_search.score(X_test, y_test)}"

    if a==0.1:
        criterion='gini'
    else:
        criterion = 'entropy'

    if b==0:
        max_depth1=None
    else:
        max_depth1 = b
    if c==0.1:
        max_features_1='auto'
    elif c==0.2:
        max_features_1 = 'sqrt'
    elif c==0.3:
        max_features_1 = 'log2'
    else:
        max_features_1 =None

    clf = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth1, max_features=max_features_1, min_samples_leaf=d,
                                 min_samples_split=e)
    Classified_two_DecisionTree = clf.fit(X_train, y_train)

    # 画出ROC曲线 DecisionTree test
    y_score = Classified_two_DecisionTree.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/DecisionTree_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 DecisionTreeClassifier test
    prey = Classified_two_DecisionTree.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/DecisionTree_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    # 画出ROC曲线 DecisionTreeClassifier train
    y_score = Classified_two_DecisionTree.fit(X, y).predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    #plt.show()
    plt.savefig(path + '/DecisionTree_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 DecisionTree train
    prey = Classified_two_DecisionTree.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/DecisionTree_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    import pickle
    pickle.dump(Classified_two_DecisionTree, open(path + "/Classified_two_DecisionTree.dat", "wb"))

    return str1, str2, str3

# 10.6
def SVM_classifier(a, b, c, d,e,path,csvName):
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    param_grid = {
        'C': [10, 70, 100],
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'degree': [2, 3, 4],
        'gamma': ['scale', 'auto']
    }

    # Create a SVM classifier object
    svc = SVC()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(svc, param_grid=param_grid, cv=5)

    # Fit the GridSearchCV object to the training data
    grid_search.fit(X_train, y_train)

    # Print the best parameters found by GridSearchCV
    print("Best parameters found:", grid_search.best_params_)

    # Evaluate the best estimator on the test data
    print("Test accuracy:", grid_search.score(X_test, y_test))
    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Test accuracy: {grid_search.score(X_test, y_test)}"

    if b==0.1:
        kernel1='linear'
    elif b==0.2:
        kernel1 = 'poly'
    elif b==0.3:
        kernel1 = 'rbf'
    else:
        kernel1 = 'sigmoid'

    if d==0.1:
        gamma1='scale'
    else:
        gamma1 = 'auto'


    if e==0:
        clf = SVC(degree=a, kernel=kernel1, C=c, gamma=gamma1, probability=True)
    Classified_two_SVM = clf.fit(X_train, y_train)

    svc_predictions = Classified_two_SVM.predict(X_test)
    print("Accuracy of SVM using optimized parameters:", accuracy_score(y_test, svc_predictions) * 100)
    print("Report:", classification_report(y_test, svc_predictions))
    print("Score:", Classified_two_SVM.score(X_test, y_test))
    str4 = "Accuracy of SVM using optimized parameters:" + str(accuracy_score(y_test, svc_predictions) * 100) + \
           '\n' + "Report:" + str(classification_report(y_test, svc_predictions)) + \
           "\n" + "Score:" + str(Classified_two_SVM.score(X_test, y_test))


    # 画出ROC曲线 SVM test
    y_score = Classified_two_SVM.fit(X, y).predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)


    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/SVM_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 SVM
    prey = Classified_two_SVM.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/SVM_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)

    # 画出ROC曲线 SVM train
    y_score = Classified_two_SVM.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    #plt.show()
    plt.savefig(path + '/SVM_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵  SVM train
    prey = Classified_two_SVM.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/SVM_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:" + str(fpr) + '\n' + "tpr:" + str(tpr) + "\n" + "true:" + str(true)
    import pickle
    pickle.dump(Classified_two_SVM, open(path + "/Classified_two_SVM.dat", "wb"))

    return str1, str4,str2, str3



def AdaBoost_classifier(a, b, c,path,csvname):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    # 数据切分
def AdaBoost_classifier(a, b, c,path,csvName):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))


    X = data.values[:, :-1]
    y = data.values[:, -1]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import train_test_split

    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.model_selection import GridSearchCV

    param_grid = {
        'n_estimators': [50, 80, 100, 120],
        'learning_rate': [0.01, 0.1, 1, 10],
        'random_state': [0, 1]
    }

    # Create an AdaBoostClassifier object
    abc = AdaBoostClassifier()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(estimator=abc, param_grid=param_grid, cv=5)

    # Fit the GridSearchCV object to the data
    grid_search.fit(X_train, y_train)

    # Print the best parameters and score
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {grid_search.best_score_}")
    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Best score: {grid_search.best_score_}"

    clf = AdaBoostClassifier(n_estimators=a, learning_rate=b, random_state=c)
    Classified_two_ABC = clf.fit(X_train, y_train)


    # 画出ROC曲线 RandomForest test
    y_score = Classified_two_ABC.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)


    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/ABC_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest test
    # clf.fit(X, y)
    prey = Classified_two_ABC.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/ABC_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    # 画出ROC曲线 RandomForest train的AUC
    y_score = Classified_two_ABC.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/ABC_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest train 混淆矩阵
    prey = Classified_two_ABC.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/ABC_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    pickle.dump(Classified_two_ABC, open(path+"/Classified_two_ABC.dat", "wb"))

    return str1,str2,str3

# --------------------------------------------------------
def xgboost_classifier(a, b, c, d, e, f,path,csvName):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    from xgboost import XGBClassifier
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))


    X = data.values[:, :-1]
    y = data.values[:, -1]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import train_test_split

    # from sklearn.ensemble import AdaBoostClassifier
    # from sklearn.model_selection import GridSearchCV
    #
    # param_grid = {
    #     'n_estimators': [50, 80, 100, 120],
    #     'max_depth': [6, 7],
    #     'min_child_weight': [1, 2, 4],
    #     'gamma': [0, 1, 5],
    #     'subsample': [0.6, 0.8, 1.0],
    #     'colsample_bytree': [0.6, 0.8, 1.0],
    #     'random_state': [0, 1]
    # }

    # # Create an XGBClassifier object
    # xgbc = XGBClassifier()
    #
    # # Create a GridSearchCV object
    # grid_search = GridSearchCV(estimator=xgbc, param_grid=param_grid, cv=5)
    #
    # # Fit the GridSearchCV object to the data
    # grid_search.fit(X_train, y_train)
    #
    # # Print the best parameters and score
    # print(f"Best parameters: {grid_search.best_params_}")
    # print(f"Best score: {grid_search.best_score_}")
    # str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Best score: {grid_search.best_score_}"

    clf = XGBClassifier(max_depth=a, random_state=b, min_child_weight=c, subsample=d, colsample_bytree=e,
                        n_estimators=f)
    clf = clf.fit(X_train, y_train)

    # clf = AdaBoostClassifier(n_estimators=a, learning_rate=b, random_state=c)
    # Classified_two_ABC = clf.fit(X_train, y_train)


    # 画出ROC曲线 RandomForest test
    y_score = clf.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)


    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/xgboost_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest test
    # clf.fit(X, y)
    prey = clf.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/xgboost_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    # 画出ROC曲线 RandomForest train的AUC
    y_score = clf.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/xgboost_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest train 混淆矩阵
    prey = clf.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/xgboost_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    pickle.dump(clf, open(path+"/Classified_two_xgboost.dat", "wb"))

    return str2,str3

# -----------------------------------------------------------------------
def CatBoost_classifier(a, b, c,path,csvName):
    from sklearn import preprocessing
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import pickle

    data = pd.DataFrame(pd.read_csv(csvName))


    X = data.values[:, :-1]
    y = data.values[:, -1]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import train_test_split

    from catboost import CatBoostClassifier
    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import train_test_split

    param_grid = {
        'n_estimators': [50, 80, 100, 120],
        'learning_rate': [0.01, 0.1, 1, 10],
        'random_state': [0, 1]
    }

    # Create a CatBoostClassifier object
    cbc = CatBoostClassifier()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(estimator=cbc, param_grid=param_grid, cv=5)

    # Fit the GridSearchCV object to the data
    grid_search.fit(X_train, y_train)

    # Print the best parameters and score
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {grid_search.best_score_}")
    str1 = f"Best parameters: {grid_search.best_params_}" + "\n" + f"Best score: {grid_search.best_score_}"

    # Create a CatBoostClassifier with best parameters
    clf = CatBoostClassifier(n_estimators=a,
                             learning_rate=b,
                             random_state=c)

    # Fit the classifier to the data
    Classified_two_CBC = clf.fit(X_train, y_train)

    # 画出ROC曲线 RandomForest test
    y_score = Classified_two_CBC.predict_proba(X_test)
    fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)


    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/CBC_test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest test
    # clf.fit(X, y)
    prey = Classified_two_CBC.predict(X_test)
    true = 0
    for i in range(0, len(y_test)):
        if prey[i] == y_test[i]:
            true = true + 1
    C = confusion_matrix(y_test, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/CBC_test_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str2 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    # 画出ROC曲线 RandomForest train的AUC
    y_score = Classified_two_CBC.predict_proba(X_train)
    fpr, tpr, threshold = roc_curve(y_train, y_score[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    print(fpr)
    print(tpr)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.01, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=20)
    plt.ylabel('True Positive Rate', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('AUC')
    plt.legend(loc="lower right", fontsize=20, frameon=False)
    #plt.show()
    plt.savefig(path + '/CBC_train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 画出混淆矩阵 RandomForest train 混淆矩阵
    prey = Classified_two_CBC.predict(X_train)
    true = 0
    for i in range(0, len(y_train)):
        if prey[i] == y_train[i]:
            true = true + 1
    C = confusion_matrix(y_train, prey, labels=[0, 1])
    plt.imshow(C, cmap=plt.cm.Blues)
    indices = range(len(C))
    plt.xticks(indices, [0, 1], fontsize=20)
    plt.yticks(indices, [0, 1], fontsize=20)
    plt.colorbar()
    for first_index in range(len(C)):  # 第几行
        for second_index in range(len(C)):  # 第几列
            plt.text(first_index, second_index, C[first_index][second_index], fontsize=20, horizontalalignment='center')
    #plt.show()
    plt.savefig(path + '/CBC_train_CM.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("true:", true)
    str3 = "fpr:"+str(fpr) + '\n' + "tpr:"+str(tpr)+"\n"+"true:"+str(true)

    pickle.dump(Classified_two_CBC, open(path+"/Classified_two_CBC.dat", "wb"))

    return str1,str2,str3






#deep learning classification

def dnn_classifier_tensorflow(a,b,c,csvName, path):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import roc_curve, auc, confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns
    import tensorflow as tf
    # 加载数据
    data = pd.read_csv(csvName)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # 数据划分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 数据标准化
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 构建模型
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 训练模型
    model.fit(X_train_scaled, y_train, epochs=a, batch_size=b, validation_split=c)

    # 评估模型
    loss, accuracy = model.evaluate(X_test_scaled, y_test)
    print(f'Test accuracy: {accuracy}')

    # 预测测试数据
    y_pred_prob_test = model.predict(X_test_scaled)
    y_pred_test = (y_pred_prob_test > 0.5).astype("int32")

    # 预测训练数据
    y_pred_prob_train = model.predict(X_train_scaled)
    y_pred_train = (y_pred_prob_train > 0.5).astype("int32")

    # 绘制测试集ROC曲线
    fpr_test, tpr_test, thresholds_test = roc_curve(y_test, y_pred_prob_test)
    roc_auc_test = auc(fpr_test, tpr_test)

    plt.figure()
    plt.plot(fpr_test, tpr_test, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc_test)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (Test Set)')
    plt.legend(loc="lower right")
    plt.savefig(path + '/DNN_test_ROC.png')
    plt.close()

    # 绘制测试集混淆矩阵
    cm_test = confusion_matrix(y_test, y_pred_test)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_test, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix (Test Set)')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(path + '/DNN_test_CM.png')
    plt.close()

    # 绘制训练集ROC曲线
    fpr_train, tpr_train, thresholds_train = roc_curve(y_train, y_pred_prob_train)
    roc_auc_train = auc(fpr_train, tpr_train)

    plt.figure()
    plt.plot(fpr_train, tpr_train, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc_train)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (Training Set)')
    plt.legend(loc="lower right")
    plt.savefig(path + '/DNN_train_ROC.png')
    plt.close()

    # 绘制训练集混淆矩阵
    cm_train = confusion_matrix(y_train, y_pred_train)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_train, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix (Training Set)')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(path + '/DNN_train_CM.png')
    plt.close()

    # 保存模型
    model.save(path + '/dnn_model_tensorflow.h5')

def cnn_classifier_tensorflow(a,b,c,csvName, path):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import roc_curve, auc, confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns
    import tensorflow as tf

    # 加载数据
    data = pd.read_csv(csvName)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # 数据划分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 数据标准化
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Reshape input data for CNN (assuming 1D input features)
    X_train_reshaped = np.expand_dims(X_train_scaled, axis=-1)
    X_test_reshaped = np.expand_dims(X_test_scaled, axis=-1)

    # 构建模型
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(X_train_reshaped.shape[1], 1)),
        tf.keras.layers.MaxPooling1D(pool_size=2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 训练模型
    model.fit(X_train_reshaped, y_train, epochs=10, batch_size=32, validation_split=0.2)

    # 评估模型
    loss, accuracy = model.evaluate(X_test_reshaped, y_test)
    print(f'Test accuracy: {accuracy}')

    # 预测测试数据
    y_pred_prob_test = model.predict(X_test_reshaped)
    y_pred_test = (y_pred_prob_test > 0.5).astype("int32")

    # 预测训练数据
    y_pred_prob_train = model.predict(X_train_reshaped)
    y_pred_train = (y_pred_prob_train > 0.5).astype("int32")

    # 绘制测试集ROC曲线
    fpr_test, tpr_test, thresholds_test = roc_curve(y_test, y_pred_prob_test)
    roc_auc_test = auc(fpr_test, tpr_test)

    plt.figure()
    plt.plot(fpr_test, tpr_test, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc_test)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (Test Set)')
    plt.legend(loc="lower right")
    plt.savefig(path + '/CNN_test_ROC.png')
    plt.close()

    # 绘制测试集混淆矩阵
    cm_test = confusion_matrix(y_test, y_pred_test)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_test, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix (Test Set)')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(path + '/CNN_test_CM.png')
    plt.close()

    # 绘制训练集ROC曲线
    fpr_train, tpr_train, thresholds_train = roc_curve(y_train, y_pred_prob_train)
    roc_auc_train = auc(fpr_train, tpr_train)

    plt.figure()
    plt.plot(fpr_train, tpr_train, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc_train)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (Training Set)')
    plt.legend(loc="lower right")
    plt.savefig(path + '/CNN_train_ROC.png')
    plt.close()

    # 绘制训练集混淆矩阵
    cm_train = confusion_matrix(y_train, y_pred_train)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_train, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix (Training Set)')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(path + '/CNN_train_CM.png')
    plt.close()

    # 保存模型
    model.save(path + '/cnn_model_tensorflow.h5')

def rnn_classifier_tensorflow(a,b,c,csvName, path):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import roc_curve, auc, confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns
    import tensorflow as tf

    # 加载数据
    data = pd.read_csv(csvName)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # 数据划分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 数据标准化
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Reshape input data for RNN (assuming 1D input features)
    X_train_reshaped = np.expand_dims(X_train_scaled, axis=2)  # 添加一个维度作为时间步
    X_test_reshaped = np.expand_dims(X_test_scaled, axis=2)

    # 构建模型
    model = tf.keras.models.Sequential([
        tf.keras.layers.SimpleRNN(units=32, activation='relu',
                                  input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2])),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 训练模型
    model.fit(X_train_reshaped, y_train, epochs=a, batch_size=b, validation_split=c)

    # 评估模型
    loss, accuracy = model.evaluate(X_test_reshaped, y_test)
    print(f'Test accuracy: {accuracy}')

    # 预测测试数据
    y_pred_prob_test = model.predict(X_test_reshaped)
    y_pred_test = (y_pred_prob_test > 0.5).astype("int32")

    # 预测训练数据
    y_pred_prob_train = model.predict(X_train_reshaped)
    y_pred_train = (y_pred_prob_train > 0.5).astype("int32")

    # 绘制测试集ROC曲线
    fpr_test, tpr_test, thresholds_test = roc_curve(y_test, y_pred_prob_test)
    roc_auc_test = auc(fpr_test, tpr_test)

    plt.figure()
    plt.plot(fpr_test, tpr_test, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc_test)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (Test Set)')
    plt.legend(loc="lower right")
    plt.savefig(path + '/RNN_test_ROC.png')
    plt.close()

    # 绘制测试集混淆矩阵
    cm_test = confusion_matrix(y_test, y_pred_test)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_test, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix (Test Set)')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(path + '/RNN_test_CM.png')
    plt.close()

    # 绘制训练集ROC曲线
    fpr_train, tpr_train, thresholds_train = roc_curve(y_train, y_pred_prob_train)
    roc_auc_train = auc(fpr_train, tpr_train)

    plt.figure()
    plt.plot(fpr_train, tpr_train, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc_train)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (Training Set)')
    plt.legend(loc="lower right")
    plt.savefig(path + '/RNN_train_ROC.png')
    plt.close()

    # 绘制训练集混淆矩阵
    cm_train = confusion_matrix(y_train, y_pred_train)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_train, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix (Training Set)')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(path + '/RNN_train_CM.png')
    plt.close()

    # 保存模型
    model.save(path + '/rnn_model_tensorflow.h5')


# --------------------------------------------------------------------------------------------------------







# 用户导入虚拟数据集(只有输入的smiles和化学式，无target)，自动生成输出结果(实际有2in1特征)
def virtual_two_in_one(path,csvpath):
    # magpie (matminer) and rdkit, 2in1
    import pandas as pd
    import csv
    def is_csv_empty(file_path):
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    return False  # 只要有一行数据，就不为空
        return True  # 如果没有任何数据行，则为空

    def select_columns_by_suffix(df, suffix):
        filtered_columns = df.filter(regex=f'{suffix}$')
        return filtered_columns

    def extract_and_store_columns(csv_file, suffixes):
        # 读取 CSV 文件
        df = pd.read_csv(csv_file)

        selected_columns = {}
        for suffix in suffixes:
            if df.filter(regex=f'{suffix}$').empty:
                filename = f'{suffix}_selected_columns.csv'
                with open(path + '/' + filename, 'w') as file:
                    pass
                continue
            else:
                selected_columns[suffix] = select_columns_by_suffix(df, suffix)
                print('********************************************************************************')
                print(f"Columns ending with '{suffix}':")
                print('********************************************************************************')
                print(selected_columns[suffix])
                # 如果需要保存到新的DataFrame中，取消注释下一行
                # global df_selected
                df_selected = pd.concat(selected_columns, axis=1)
                # df_combined = pd.concat(selected_columns.values(), axis=1)
                # df_combined.to_csv('selected_columns.csv', index=False)
                selected_columns[suffix].to_csv(path + '/' + f'{suffix}_selected_columns.csv', index=False)

        # 获取未被选中的列
        unselected_columns = df.drop(columns=[col for cols in selected_columns.values() for col in cols.columns])

        # 保存未被选中的列到 CSV 文件
        unselected_columns.to_csv(path + '/' + 'unselected_columns.csv', index=False)

        return selected_columns

    # 用法示例
    file_path = csvpath
    suffixes = ['Formula', 'Smiles']
    selected_columns = extract_and_store_columns(file_path, suffixes)

    if is_csv_empty(path + '/Formula_selected_columns.csv'):
        Formular_state = 0
    else:
        Formular_state = 1

    if Formular_state == 1:
        original_data = pd.DataFrame(pd.read_csv(path + '/Formula_selected_columns.csv'))
        import pandas as pd

        # 假设 original_data 是您的原始数据集
        # 创建一个空字典，用于存储新的数据集
        new_datasets = {}

        # 遍历原始数据集的每一列
        for col_name in original_data.columns:
            # 创建新的数据集，将当前列命名为 'Name'
            new_dataset = pd.DataFrame({'Name': original_data[col_name]})

            # 将新数据集存储在字典中，字典的键是 'data1'，'data2'，依此类推
            new_datasets['data' + str(len(new_datasets) + 1)] = new_dataset

        # 打印或使用新的数据集
        for key, value in new_datasets.items():
            print(f"{key}:\n{value}\n")

        import pandas as pd
        from matminer.featurizers.conversions import StrToComposition
        from matminer.featurizers.composition.orbital import AtomicOrbitals
        from matminer.featurizers.composition import ElementProperty
        from matminer.featurizers.composition.element import ElementFraction
        from pymatgen.core import Composition

        ignore_errors = True
        # 假设 new_datasets 是包含拆分数据集的字典，如 'data1', 'data2', ...
        # 每个数据集中应该有 'Name' 列

        # 初始化 StrToComposition
        str_to_comp = StrToComposition(target_col_id='composition')

        # 初始化 AtomicOrbitals
        comp_to_orbital = AtomicOrbitals()

        # 初始化 ElementProperty
        features_element_property = ['Number', 'MendeleevNumber', 'AtomicWeight', 'MeltingT',
                                     'Column', 'Row', 'CovalentRadius', 'Electronegativity',
                                     'NsValence', 'NpValence', 'NdValence', 'NfValence', 'NValence',
                                     'NsUnfilled', 'NpUnfilled', 'NdUnfilled', 'NfUnfilled', 'NUnfilled',
                                     'GSvolume_pa', 'GSbandgap', 'GSmagmom', 'SpaceGroupNumber']
        stats_element_property = ['mean', 'minimum', 'maximum', 'range', 'avg_dev', 'mode']
        element_property_featurizer = ElementProperty(data_source='magpie', features=features_element_property,
                                                      stats=stats_element_property)

        # 初始化 ElementFraction
        element_fraction = ElementFraction()

        # 用于存储特征转换后的数据集
        result_datasets = {}

        # 遍历拆分的数据集
        for i, (key, dataset) in enumerate(new_datasets.items(), start=1):
            # 特征转换1: StrToComposition

            df_comp = str_to_comp.featurize_dataframe(dataset, col_id='Name')

            # 特征转换2: AtomicOrbitals
            orbital_features = comp_to_orbital.featurize_dataframe(df_comp, col_id='composition')
            orbital_features = orbital_features.iloc[:, [4, 7, 8]]  # 选择感兴趣的列

            # 特征转换3: ElementProperty
            element_property_features = element_property_featurizer.featurize_dataframe(df_comp, col_id='composition')
            element_property_features = element_property_features.iloc[:, 2:-1]  # 选择感兴趣的列

            # 特征转换4: ElementFraction
            element_fraction_features = element_fraction.featurize_dataframe(df_comp, col_id='composition')
            element_fraction_features = element_fraction_features.iloc[:, 2:-1]  # 选择感兴趣的列

            # 添加前缀
            prefix_orbital = f'_formula_{i}_orbital_'
            orbital_features = orbital_features.add_prefix(prefix_orbital)

            prefix_element_property = f'_formula_{i}_element_property_'
            element_property_features = element_property_features.add_prefix(prefix_element_property)

            prefix_element_fraction = f'_formula_{i}_element_fraction_'
            element_fraction_features = element_fraction_features.add_prefix(prefix_element_fraction)

            # 合并特征转换后的数据集
            result_datasets[key] = pd.concat([orbital_features, element_property_features, element_fraction_features],
                                             axis=1)

        # 合并所有数据集
        merged_result = pd.concat(result_datasets.values(), axis=1)

        # 将合并后的结果保存为 CSV 文件
        merged_result.to_csv(path + '/merged_result.csv', index=False)

        # 打印或使用合并后的结果
        print(merged_result)

    ######## 有机部分
    if is_csv_empty(path + '/Smiles_selected_columns.csv'):
        Smiles_state = 0
    else:
        Smiles_state = 1

    if Smiles_state == 1:
        original_data2 = pd.DataFrame(pd.read_csv(path + '/Smiles_selected_columns.csv'))

        new_datasets2 = {}

        # 遍历原始数据集的每一列
        for col_name in original_data2.columns:
            # 创建新的数据集，将当前列命名为 'Name'
            new_dataset2 = pd.DataFrame({'Name': original_data2[col_name]})

            # 将新数据集存储在字典中，字典的键是 'organic_data1'，'organic_data2'，依此类推
            new_datasets2['organic_data' + str(len(new_datasets2) + 1)] = new_dataset2

        # 打印或使用新的数据集
        for key, value in new_datasets2.items():
            print(f"{key}:\n{value}\n")

        import pandas as pd
        import numpy as np
        from rdkit import Chem
        from rdkit.Chem import AllChem

        # 假设 new_datasets2 是包含拆分数据集的字典，如 'organic_data1', 'organic_data2', ...
        # 每个数据集中应该有 'Name' 列

        # 用于存储 RDKit 特征化后的数据集
        rdkit_datasets = {}

        # # 遍历拆分的数据集
        # for key, dataset in new_datasets2.items():
        #     # 特征化 RDKit
        #     rdkit_features = dataset['Name'].apply(
        #         lambda x: AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(x), 2))
        #
        #     # 将 RDKit 指纹转换为 DataFrame
        #     rdkit_features_df = pd.DataFrame(
        #         list(rdkit_features.apply(lambda x: np.frombuffer(x.ToBinary(), dtype=np.uint8))))
        #
        #     # 添加前缀
        #     prefix_rdkit = f'{key}_rdkit_'
        #     rdkit_features_df = rdkit_features_df.add_prefix(prefix_rdkit)
        #
        #     # 存储特征化后的数据集
        #     rdkit_datasets[key] = rdkit_features_df
        from rdkit import Chem
        from rdkit.Chem import Descriptors
        import pandas as pd
        for key, dataset in new_datasets2.items():
            # 特征化 RDKit
            rdkit_features = dataset['Name'].apply(lambda x: Chem.MolFromSmiles(x))

            # 检查分子是否有效
            valid_mols = rdkit_features.dropna()

            if not valid_mols.empty:
                # 计算所有 RDKit 描述符
                # rdkit_descriptors = valid_mols.apply(lambda x: [Descriptors.MolWt(x), Descriptors.NumRotatableBonds(x)])
                rdkit_descriptors = valid_mols.apply(lambda x: [Descriptors.BalabanJ(x),
                                                                Descriptors.BertzCT(x),
                                                                Descriptors.Chi0(x),
                                                                Descriptors.Chi0n(x),
                                                                Descriptors.Chi0v(x),
                                                                Descriptors.Chi1(x),
                                                                Descriptors.Chi1n(x),
                                                                Descriptors.Chi1v(x),
                                                                Descriptors.Chi2n(x),
                                                                Descriptors.Chi2v(x),
                                                                Descriptors.Chi3n(x),
                                                                Descriptors.Chi3v(x),
                                                                Descriptors.Chi4n(x),
                                                                Descriptors.Chi4v(x),
                                                                Descriptors.EState_VSA1(x),
                                                                Descriptors.EState_VSA10(x),
                                                                Descriptors.EState_VSA11(x),
                                                                Descriptors.EState_VSA2(x),
                                                                Descriptors.EState_VSA3(x),
                                                                Descriptors.EState_VSA4(x),
                                                                Descriptors.EState_VSA5(x),
                                                                Descriptors.EState_VSA6(x),
                                                                Descriptors.EState_VSA7(x),
                                                                Descriptors.EState_VSA8(x),
                                                                Descriptors.EState_VSA9(x),
                                                                Descriptors.ExactMolWt(x),
                                                                Descriptors.FpDensityMorgan1(x),
                                                                Descriptors.FpDensityMorgan2(x),
                                                                Descriptors.FpDensityMorgan3(x),
                                                                Descriptors.FractionCSP3(x),
                                                                Descriptors.HallKierAlpha(x),
                                                                Descriptors.HeavyAtomCount(x),
                                                                Descriptors.HeavyAtomMolWt(x),
                                                                Descriptors.Ipc(x),
                                                                Descriptors.Kappa1(x),
                                                                Descriptors.Kappa2(x),
                                                                Descriptors.Kappa3(x),
                                                                Descriptors.LabuteASA(x),
                                                                Descriptors.MaxAbsEStateIndex(x),
                                                                Descriptors.MaxAbsPartialCharge(x),
                                                                Descriptors.MaxEStateIndex(x),
                                                                Descriptors.MaxPartialCharge(x),
                                                                Descriptors.MinAbsEStateIndex(x),
                                                                Descriptors.MinAbsPartialCharge(x),
                                                                Descriptors.MinEStateIndex(x),
                                                                Descriptors.MinPartialCharge(x),
                                                                Descriptors.MolLogP(x),
                                                                Descriptors.MolMR(x),
                                                                Descriptors.MolWt(x),
                                                                Descriptors.NHOHCount(x),
                                                                Descriptors.NOCount(x),
                                                                Descriptors.NumAliphaticCarbocycles(x),
                                                                Descriptors.NumAliphaticHeterocycles(x),
                                                                Descriptors.NumAliphaticRings(x),
                                                                Descriptors.NumAromaticCarbocycles(x),
                                                                Descriptors.NumAromaticHeterocycles(x),
                                                                Descriptors.NumAromaticRings(x),
                                                                Descriptors.NumHAcceptors(x),
                                                                Descriptors.NumHDonors(x),
                                                                Descriptors.NumHeteroatoms(x),
                                                                Descriptors.NumRadicalElectrons(x),
                                                                Descriptors.NumRotatableBonds(x),
                                                                Descriptors.NumSaturatedCarbocycles(x),
                                                                Descriptors.NumSaturatedHeterocycles(x),
                                                                Descriptors.NumSaturatedRings(x),
                                                                Descriptors.NumValenceElectrons(x),
                                                                Descriptors.PEOE_VSA1(x),
                                                                Descriptors.PEOE_VSA10(x),
                                                                Descriptors.PEOE_VSA11(x),
                                                                Descriptors.PEOE_VSA12(x),
                                                                Descriptors.PEOE_VSA13(x),
                                                                Descriptors.PEOE_VSA14(x),
                                                                Descriptors.PEOE_VSA2(x),
                                                                Descriptors.PEOE_VSA3(x),
                                                                Descriptors.PEOE_VSA4(x),
                                                                Descriptors.PEOE_VSA5(x),
                                                                Descriptors.PEOE_VSA6(x),
                                                                Descriptors.PEOE_VSA7(x),
                                                                Descriptors.PEOE_VSA8(x),
                                                                Descriptors.PEOE_VSA9(x),
                                                                Descriptors.RingCount(x),
                                                                Descriptors.SMR_VSA1(x),
                                                                Descriptors.SMR_VSA10(x),
                                                                Descriptors.SMR_VSA2(x),
                                                                Descriptors.SMR_VSA3(x),
                                                                Descriptors.SMR_VSA4(x),
                                                                Descriptors.SMR_VSA5(x),
                                                                Descriptors.SMR_VSA6(x),
                                                                Descriptors.SMR_VSA7(x),
                                                                Descriptors.SMR_VSA8(x),
                                                                Descriptors.SMR_VSA9(x),
                                                                Descriptors.SlogP_VSA1(x),
                                                                Descriptors.SlogP_VSA10(x),
                                                                Descriptors.SlogP_VSA11(x),
                                                                Descriptors.SlogP_VSA12(x),
                                                                Descriptors.SlogP_VSA2(x),
                                                                Descriptors.SlogP_VSA3(x),
                                                                Descriptors.SlogP_VSA4(x),
                                                                Descriptors.SlogP_VSA5(x),
                                                                Descriptors.SlogP_VSA6(x),
                                                                Descriptors.SlogP_VSA7(x),
                                                                Descriptors.SlogP_VSA8(x),
                                                                Descriptors.SlogP_VSA9(x),
                                                                Descriptors.TPSA(x),
                                                                Descriptors.VSA_EState1(x),
                                                                Descriptors.VSA_EState10(x),
                                                                Descriptors.VSA_EState2(x),
                                                                Descriptors.VSA_EState3(x),
                                                                Descriptors.VSA_EState4(x),
                                                                Descriptors.VSA_EState5(x),
                                                                Descriptors.VSA_EState6(x),
                                                                Descriptors.VSA_EState7(x),
                                                                Descriptors.VSA_EState8(x),
                                                                Descriptors.VSA_EState9(x),
                                                                Descriptors.fr_Al_COO(x),
                                                                Descriptors.fr_Al_OH(x),
                                                                Descriptors.fr_Al_OH_noTert(x),
                                                                Descriptors.fr_ArN(x),
                                                                Descriptors.fr_Ar_COO(x),
                                                                Descriptors.fr_Ar_N(x),
                                                                Descriptors.fr_Ar_NH(x),
                                                                Descriptors.fr_Ar_OH(x),
                                                                Descriptors.fr_COO(x),
                                                                Descriptors.fr_COO2(x),
                                                                Descriptors.fr_C_O(x),
                                                                Descriptors.fr_C_O_noCOO(x),
                                                                Descriptors.fr_C_S(x),
                                                                Descriptors.fr_HOCCN(x),
                                                                Descriptors.fr_Imine(x),
                                                                Descriptors.fr_NH0(x),
                                                                Descriptors.fr_NH1(x),
                                                                Descriptors.fr_NH2(x),
                                                                Descriptors.fr_N_O(x),
                                                                Descriptors.fr_Ndealkylation1(x),
                                                                Descriptors.fr_Ndealkylation2(x),
                                                                Descriptors.fr_Nhpyrrole(x),
                                                                Descriptors.fr_SH(x),
                                                                Descriptors.fr_aldehyde(x),
                                                                Descriptors.fr_alkyl_carbamate(x),
                                                                Descriptors.fr_alkyl_halide(x),
                                                                Descriptors.fr_allylic_oxid(x),
                                                                Descriptors.fr_amide(x),
                                                                Descriptors.fr_amidine(x),
                                                                Descriptors.fr_aniline(x),
                                                                Descriptors.fr_aryl_methyl(x),
                                                                Descriptors.fr_azide(x),
                                                                Descriptors.fr_azo(x),
                                                                Descriptors.fr_barbitur(x),
                                                                Descriptors.fr_benzene(x),
                                                                Descriptors.fr_benzodiazepine(x),
                                                                Descriptors.fr_bicyclic(x),
                                                                Descriptors.fr_diazo(x),
                                                                Descriptors.fr_dihydropyridine(x),
                                                                Descriptors.fr_epoxide(x),
                                                                Descriptors.fr_ester(x),
                                                                Descriptors.fr_ether(x),
                                                                Descriptors.fr_furan(x),
                                                                Descriptors.fr_guanido(x),
                                                                Descriptors.fr_halogen(x),
                                                                Descriptors.fr_hdrzine(x),
                                                                Descriptors.fr_hdrzone(x),
                                                                Descriptors.fr_imidazole(x),
                                                                Descriptors.fr_imide(x),
                                                                Descriptors.fr_isocyan(x),
                                                                Descriptors.fr_isothiocyan(x),
                                                                Descriptors.fr_ketone(x),
                                                                Descriptors.fr_ketone_Topliss(x),
                                                                Descriptors.fr_lactam(x),
                                                                Descriptors.fr_lactone(x),
                                                                Descriptors.fr_methoxy(x),
                                                                Descriptors.fr_morpholine(x),
                                                                Descriptors.fr_nitrile(x),
                                                                Descriptors.fr_nitro(x),
                                                                Descriptors.fr_nitro_arom(x),
                                                                Descriptors.fr_nitro_arom_nonortho(x),
                                                                Descriptors.fr_nitroso(x),
                                                                Descriptors.fr_oxazole(x),
                                                                Descriptors.fr_oxime(x),
                                                                Descriptors.fr_para_hydroxylation(x),
                                                                Descriptors.fr_phenol(x),
                                                                Descriptors.fr_phenol_noOrthoHbond(x),
                                                                Descriptors.fr_phos_acid(x),
                                                                Descriptors.fr_phos_ester(x),
                                                                Descriptors.fr_piperdine(x),
                                                                Descriptors.fr_piperzine(x),
                                                                Descriptors.fr_priamide(x),
                                                                Descriptors.fr_prisulfonamd(x),
                                                                Descriptors.fr_pyridine(x),
                                                                Descriptors.fr_quatN(x),
                                                                Descriptors.fr_sulfide(x),
                                                                Descriptors.fr_sulfonamd(x),
                                                                Descriptors.fr_sulfone(x),
                                                                Descriptors.fr_term_acetylene(x),
                                                                Descriptors.fr_tetrazole(x),
                                                                Descriptors.fr_thiazole(x),
                                                                Descriptors.fr_thiocyan(x),
                                                                Descriptors.fr_thiophene(x),
                                                                Descriptors.fr_unbrch_alkane(x),
                                                                Descriptors.fr_urea(x),
                                                                Descriptors.qed(x)])
                # 将 RDKit 描述符转换为 DataFrame
                rdkit_descriptors_df = pd.DataFrame(list(rdkit_descriptors),
                                                    columns=['BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n', 'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'EState_VSA1', 'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'ExactMolWt', 'FpDensityMorgan1',
                                                             'FpDensityMorgan2', 'FpDensityMorgan3', 'FractionCSP3', 'HallKierAlpha', 'HeavyAtomCount', 'HeavyAtomMolWt', 'Ipc', 'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'MaxAbsEStateIndex', 'MaxAbsPartialCharge', 'MaxEStateIndex', 'MaxPartialCharge', 'MinAbsEStateIndex', 'MinAbsPartialCharge', 'MinEStateIndex', 'MinPartialCharge', 'MolLogP',
                                                             'MolMR',
                                                             'MolWt', 'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles', 'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms', 'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles',
                                                             'NumSaturatedRings', 'NumValenceElectrons', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7', 'PEOE_VSA8', 'PEOE_VSA9', 'RingCount', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6',
                                                             'SMR_VSA7',
                                                             'SMR_VSA8', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'VSA_EState1', 'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5', 'VSA_EState6', 'VSA_EState7', 'VSA_EState8',
                                                             'VSA_EState9', 'fr_Al_COO', 'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde',
                                                             'fr_alkyl_carbamate',
                                                             'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole',
                                                             'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss', 'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile', 'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_phos_acid',
                                                             'fr_phos_ester',
                                                             'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan', 'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'qed'])

                # 添加前缀
                prefix_rdkit = f'{key}_rdkit_'
                rdkit_descriptors_df = rdkit_descriptors_df.add_prefix(prefix_rdkit)

                # 存储特征化后的数据集
                rdkit_datasets[key] = rdkit_descriptors_df

        # rdkit_datasets 包含了每个数据集的 RDKit 描述符
        # 合并 RDKit 特征化后的数据集
        merged_rdkit_result = pd.concat(rdkit_datasets.values(), axis=1)
        merged_rdkit_result.fillna(0, inplace=True)
        # 将合并后的结果保存为 CSV 文件
        merged_rdkit_result.to_csv(path + '/merged_rdkit_result.csv', index=False)

        # 打印或使用合并后的 RDKit 特征化结果
        print(merged_rdkit_result)

    unselected_columns = pd.DataFrame(pd.read_csv(path + '/unselected_columns.csv'))
    # 合并前重置索引
    unselected_columns.reset_index(drop=True, inplace=True)
    if Formular_state == 1 and Smiles_state == 1:
        merged_result.reset_index(drop=True, inplace=True)
        merged_rdkit_result.reset_index(drop=True, inplace=True)

        # 合并三个数据集
        all_merged_data = pd.concat([merged_result, merged_rdkit_result, unselected_columns], axis=1)
    elif Formular_state == 1 and Smiles_state == 0:
        merged_result.reset_index(drop=True, inplace=True)
        all_merged_data = pd.concat([merged_result, unselected_columns], axis=1)

    elif Formular_state == 0 and Smiles_state == 1:
        merged_rdkit_result.reset_index(drop=True, inplace=True)
        all_merged_data = pd.concat([merged_rdkit_result, unselected_columns], axis=1)

    # 将合并后的结果保存为 CSV 文件
    all_merged_data.to_csv(path + '/train_test_dataset.csv', index=False)
    # 原来的文件保存-------------------------------------------------------------------------------↑----------------

    selected_columns = all_merged_data.loc[:, s_rfe.columns]
    selected_columns.to_csv(path+'/virtual_generate_final.csv', index=False)

def virtual_Multicolumn_Smiles_RDKit(path,csvpath):
    import pandas as pd
    def select_columns_by_suffix(df, suffix):
        filtered_columns = df.filter(regex=f'{suffix}$')
        return filtered_columns

    def extract_and_store_columns(csv_file, suffixes):
        # 读取 CSV 文件
        df = pd.read_csv(csv_file)

        selected_columns = {}
        for suffix in suffixes:
            selected_columns[suffix] = select_columns_by_suffix(df, suffix)
            print('********************************************************************************')
            print(f"Columns ending with '{suffix}':")
            print('********************************************************************************')
            print(selected_columns[suffix])
            # 如果需要保存到新的DataFrame中，取消注释下一行
            # global df_selected
            df_selected = pd.concat(selected_columns, axis=1)
            # df_combined = pd.concat(selected_columns.values(), axis=1)
            # df_combined.to_csv('selected_columns.csv', index=False)
            selected_columns[suffix].to_csv(path + '/' + f'{suffix}_selected_columns.csv', index=False)

        # 获取未被选中的列
        unselected_columns = df.drop(columns=[col for cols in selected_columns.values() for col in cols.columns])

        # 保存未被选中的列到 CSV 文件
        unselected_columns.to_csv(path + '/' + 'unselected_columns.csv', index=False)

        return selected_columns

    # 用法示例
    file_path = csvpath
    suffixes = ['Smiles']
    selected_columns = extract_and_store_columns(file_path, suffixes)

    original_data = pd.DataFrame(pd.read_csv(path + '/Smiles_selected_columns.csv'))

    import pandas as pd

    # 假设 original_data 是您的原始数据集
    # 创建一个空字典，用于存储新的数据集
    new_datasets = {}

    # 遍历原始数据集的每一列
    for col_name in original_data.columns:
        # 创建新的数据集，将当前列命名为 'Name'
        new_dataset = pd.DataFrame({'Name': original_data[col_name]})

        # 将新数据集存储在字典中，字典的键是 'data1'，'data2'，依此类推
        new_datasets['data' + str(len(new_datasets) + 1)] = new_dataset

    # 打印或使用新的数据集
    for key, value in new_datasets.items():
        print(f"{key}:\n{value}\n")


    # 有机部分
    original_data2 = pd.DataFrame(pd.read_csv(path + '/Smiles_selected_columns.csv'))

    new_datasets2 = {}

    # 遍历原始数据集的每一列
    for col_name in original_data2.columns:
        # 创建新的数据集，将当前列命名为 'Name'
        new_dataset2 = pd.DataFrame({'Name': original_data2[col_name]})

        # 将新数据集存储在字典中，字典的键是 'organic_data1'，'organic_data2'，依此类推
        new_datasets2['organic_data' + str(len(new_datasets2) + 1)] = new_dataset2

    # 打印或使用新的数据集
    for key, value in new_datasets2.items():
        print(f"{key}:\n{value}\n")

    import pandas as pd
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem

    # 假设 new_datasets2 是包含拆分数据集的字典，如 'organic_data1', 'organic_data2', ...
    # 每个数据集中应该有 'Name' 列

    # 用于存储 RDKit 特征化后的数据集
    from rdkit import Chem
    from rdkit.Chem import Descriptors
    import pandas as pd

    rdkit_datasets = {}

    for key, dataset in new_datasets2.items():
        # 特征化 RDKit
        rdkit_features = dataset['Name'].apply(lambda x: Chem.MolFromSmiles(x))

        # 检查分子是否有效
        valid_mols = rdkit_features.dropna()

        if not valid_mols.empty:
            # 计算所有 RDKit 描述符
            # rdkit_descriptors = valid_mols.apply(lambda x: [Descriptors.MolWt(x), Descriptors.NumRotatableBonds(x)])
            rdkit_descriptors = valid_mols.apply(lambda x: [Descriptors.BalabanJ(x),
                                                            Descriptors.BertzCT(x),
                                                            Descriptors.Chi0(x),
                                                            Descriptors.Chi0n(x),
                                                            Descriptors.Chi0v(x),
                                                            Descriptors.Chi1(x),
                                                            Descriptors.Chi1n(x),
                                                            Descriptors.Chi1v(x),
                                                            Descriptors.Chi2n(x),
                                                            Descriptors.Chi2v(x),
                                                            Descriptors.Chi3n(x),
                                                            Descriptors.Chi3v(x),
                                                            Descriptors.Chi4n(x),
                                                            Descriptors.Chi4v(x),
                                                            Descriptors.EState_VSA1(x),
                                                            Descriptors.EState_VSA10(x),
                                                            Descriptors.EState_VSA11(x),
                                                            Descriptors.EState_VSA2(x),
                                                            Descriptors.EState_VSA3(x),
                                                            Descriptors.EState_VSA4(x),
                                                            Descriptors.EState_VSA5(x),
                                                            Descriptors.EState_VSA6(x),
                                                            Descriptors.EState_VSA7(x),
                                                            Descriptors.EState_VSA8(x),
                                                            Descriptors.EState_VSA9(x),
                                                            Descriptors.ExactMolWt(x),
                                                            Descriptors.FpDensityMorgan1(x),
                                                            Descriptors.FpDensityMorgan2(x),
                                                            Descriptors.FpDensityMorgan3(x),
                                                            Descriptors.FractionCSP3(x),
                                                            Descriptors.HallKierAlpha(x),
                                                            Descriptors.HeavyAtomCount(x),
                                                            Descriptors.HeavyAtomMolWt(x),
                                                            Descriptors.Ipc(x),
                                                            Descriptors.Kappa1(x),
                                                            Descriptors.Kappa2(x),
                                                            Descriptors.Kappa3(x),
                                                            Descriptors.LabuteASA(x),
                                                            Descriptors.MaxAbsEStateIndex(x),
                                                            Descriptors.MaxAbsPartialCharge(x),
                                                            Descriptors.MaxEStateIndex(x),
                                                            Descriptors.MaxPartialCharge(x),
                                                            Descriptors.MinAbsEStateIndex(x),
                                                            Descriptors.MinAbsPartialCharge(x),
                                                            Descriptors.MinEStateIndex(x),
                                                            Descriptors.MinPartialCharge(x),
                                                            Descriptors.MolLogP(x),
                                                            Descriptors.MolMR(x),
                                                            Descriptors.MolWt(x),
                                                            Descriptors.NHOHCount(x),
                                                            Descriptors.NOCount(x),
                                                            Descriptors.NumAliphaticCarbocycles(x),
                                                            Descriptors.NumAliphaticHeterocycles(x),
                                                            Descriptors.NumAliphaticRings(x),
                                                            Descriptors.NumAromaticCarbocycles(x),
                                                            Descriptors.NumAromaticHeterocycles(x),
                                                            Descriptors.NumAromaticRings(x),
                                                            Descriptors.NumHAcceptors(x),
                                                            Descriptors.NumHDonors(x),
                                                            Descriptors.NumHeteroatoms(x),
                                                            Descriptors.NumRadicalElectrons(x),
                                                            Descriptors.NumRotatableBonds(x),
                                                            Descriptors.NumSaturatedCarbocycles(x),
                                                            Descriptors.NumSaturatedHeterocycles(x),
                                                            Descriptors.NumSaturatedRings(x),
                                                            Descriptors.NumValenceElectrons(x),
                                                            Descriptors.PEOE_VSA1(x),
                                                            Descriptors.PEOE_VSA10(x),
                                                            Descriptors.PEOE_VSA11(x),
                                                            Descriptors.PEOE_VSA12(x),
                                                            Descriptors.PEOE_VSA13(x),
                                                            Descriptors.PEOE_VSA14(x),
                                                            Descriptors.PEOE_VSA2(x),
                                                            Descriptors.PEOE_VSA3(x),
                                                            Descriptors.PEOE_VSA4(x),
                                                            Descriptors.PEOE_VSA5(x),
                                                            Descriptors.PEOE_VSA6(x),
                                                            Descriptors.PEOE_VSA7(x),
                                                            Descriptors.PEOE_VSA8(x),
                                                            Descriptors.PEOE_VSA9(x),
                                                            Descriptors.RingCount(x),
                                                            Descriptors.SMR_VSA1(x),
                                                            Descriptors.SMR_VSA10(x),
                                                            Descriptors.SMR_VSA2(x),
                                                            Descriptors.SMR_VSA3(x),
                                                            Descriptors.SMR_VSA4(x),
                                                            Descriptors.SMR_VSA5(x),
                                                            Descriptors.SMR_VSA6(x),
                                                            Descriptors.SMR_VSA7(x),
                                                            Descriptors.SMR_VSA8(x),
                                                            Descriptors.SMR_VSA9(x),
                                                            Descriptors.SlogP_VSA1(x),
                                                            Descriptors.SlogP_VSA10(x),
                                                            Descriptors.SlogP_VSA11(x),
                                                            Descriptors.SlogP_VSA12(x),
                                                            Descriptors.SlogP_VSA2(x),
                                                            Descriptors.SlogP_VSA3(x),
                                                            Descriptors.SlogP_VSA4(x),
                                                            Descriptors.SlogP_VSA5(x),
                                                            Descriptors.SlogP_VSA6(x),
                                                            Descriptors.SlogP_VSA7(x),
                                                            Descriptors.SlogP_VSA8(x),
                                                            Descriptors.SlogP_VSA9(x),
                                                            Descriptors.TPSA(x),
                                                            Descriptors.VSA_EState1(x),
                                                            Descriptors.VSA_EState10(x),
                                                            Descriptors.VSA_EState2(x),
                                                            Descriptors.VSA_EState3(x),
                                                            Descriptors.VSA_EState4(x),
                                                            Descriptors.VSA_EState5(x),
                                                            Descriptors.VSA_EState6(x),
                                                            Descriptors.VSA_EState7(x),
                                                            Descriptors.VSA_EState8(x),
                                                            Descriptors.VSA_EState9(x),
                                                            Descriptors.fr_Al_COO(x),
                                                            Descriptors.fr_Al_OH(x),
                                                            Descriptors.fr_Al_OH_noTert(x),
                                                            Descriptors.fr_ArN(x),
                                                            Descriptors.fr_Ar_COO(x),
                                                            Descriptors.fr_Ar_N(x),
                                                            Descriptors.fr_Ar_NH(x),
                                                            Descriptors.fr_Ar_OH(x),
                                                            Descriptors.fr_COO(x),
                                                            Descriptors.fr_COO2(x),
                                                            Descriptors.fr_C_O(x),
                                                            Descriptors.fr_C_O_noCOO(x),
                                                            Descriptors.fr_C_S(x),
                                                            Descriptors.fr_HOCCN(x),
                                                            Descriptors.fr_Imine(x),
                                                            Descriptors.fr_NH0(x),
                                                            Descriptors.fr_NH1(x),
                                                            Descriptors.fr_NH2(x),
                                                            Descriptors.fr_N_O(x),
                                                            Descriptors.fr_Ndealkylation1(x),
                                                            Descriptors.fr_Ndealkylation2(x),
                                                            Descriptors.fr_Nhpyrrole(x),
                                                            Descriptors.fr_SH(x),
                                                            Descriptors.fr_aldehyde(x),
                                                            Descriptors.fr_alkyl_carbamate(x),
                                                            Descriptors.fr_alkyl_halide(x),
                                                            Descriptors.fr_allylic_oxid(x),
                                                            Descriptors.fr_amide(x),
                                                            Descriptors.fr_amidine(x),
                                                            Descriptors.fr_aniline(x),
                                                            Descriptors.fr_aryl_methyl(x),
                                                            Descriptors.fr_azide(x),
                                                            Descriptors.fr_azo(x),
                                                            Descriptors.fr_barbitur(x),
                                                            Descriptors.fr_benzene(x),
                                                            Descriptors.fr_benzodiazepine(x),
                                                            Descriptors.fr_bicyclic(x),
                                                            Descriptors.fr_diazo(x),
                                                            Descriptors.fr_dihydropyridine(x),
                                                            Descriptors.fr_epoxide(x),
                                                            Descriptors.fr_ester(x),
                                                            Descriptors.fr_ether(x),
                                                            Descriptors.fr_furan(x),
                                                            Descriptors.fr_guanido(x),
                                                            Descriptors.fr_halogen(x),
                                                            Descriptors.fr_hdrzine(x),
                                                            Descriptors.fr_hdrzone(x),
                                                            Descriptors.fr_imidazole(x),
                                                            Descriptors.fr_imide(x),
                                                            Descriptors.fr_isocyan(x),
                                                            Descriptors.fr_isothiocyan(x),
                                                            Descriptors.fr_ketone(x),
                                                            Descriptors.fr_ketone_Topliss(x),
                                                            Descriptors.fr_lactam(x),
                                                            Descriptors.fr_lactone(x),
                                                            Descriptors.fr_methoxy(x),
                                                            Descriptors.fr_morpholine(x),
                                                            Descriptors.fr_nitrile(x),
                                                            Descriptors.fr_nitro(x),
                                                            Descriptors.fr_nitro_arom(x),
                                                            Descriptors.fr_nitro_arom_nonortho(x),
                                                            Descriptors.fr_nitroso(x),
                                                            Descriptors.fr_oxazole(x),
                                                            Descriptors.fr_oxime(x),
                                                            Descriptors.fr_para_hydroxylation(x),
                                                            Descriptors.fr_phenol(x),
                                                            Descriptors.fr_phenol_noOrthoHbond(x),
                                                            Descriptors.fr_phos_acid(x),
                                                            Descriptors.fr_phos_ester(x),
                                                            Descriptors.fr_piperdine(x),
                                                            Descriptors.fr_piperzine(x),
                                                            Descriptors.fr_priamide(x),
                                                            Descriptors.fr_prisulfonamd(x),
                                                            Descriptors.fr_pyridine(x),
                                                            Descriptors.fr_quatN(x),
                                                            Descriptors.fr_sulfide(x),
                                                            Descriptors.fr_sulfonamd(x),
                                                            Descriptors.fr_sulfone(x),
                                                            Descriptors.fr_term_acetylene(x),
                                                            Descriptors.fr_tetrazole(x),
                                                            Descriptors.fr_thiazole(x),
                                                            Descriptors.fr_thiocyan(x),
                                                            Descriptors.fr_thiophene(x),
                                                            Descriptors.fr_unbrch_alkane(x),
                                                            Descriptors.fr_urea(x),
                                                            Descriptors.qed(x)])
            # 将 RDKit 描述符转换为 DataFrame
            rdkit_descriptors_df = pd.DataFrame(list(rdkit_descriptors),
                                                columns=['BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n', 'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'EState_VSA1', 'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'ExactMolWt', 'FpDensityMorgan1',
                                                         'FpDensityMorgan2', 'FpDensityMorgan3', 'FractionCSP3', 'HallKierAlpha', 'HeavyAtomCount', 'HeavyAtomMolWt', 'Ipc', 'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'MaxAbsEStateIndex', 'MaxAbsPartialCharge', 'MaxEStateIndex', 'MaxPartialCharge', 'MinAbsEStateIndex', 'MinAbsPartialCharge', 'MinEStateIndex', 'MinPartialCharge', 'MolLogP', 'MolMR',
                                                         'MolWt', 'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles', 'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms', 'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles',
                                                         'NumSaturatedRings', 'NumValenceElectrons', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7', 'PEOE_VSA8', 'PEOE_VSA9', 'RingCount', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7',
                                                         'SMR_VSA8', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'VSA_EState1', 'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5', 'VSA_EState6', 'VSA_EState7', 'VSA_EState8',
                                                         'VSA_EState9', 'fr_Al_COO', 'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde', 'fr_alkyl_carbamate',
                                                         'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole',
                                                         'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss', 'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile', 'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester',
                                                         'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan', 'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'qed'])

            # 添加前缀
            prefix_rdkit = f'{key}_rdkit_'
            rdkit_descriptors_df = rdkit_descriptors_df.add_prefix(prefix_rdkit)

            # 存储特征化后的数据集
            rdkit_datasets[key] = rdkit_descriptors_df

    # rdkit_datasets 包含了每个数据集的 RDKit 描述符

    # 合并 RDKit 特征化后的数据集
    merged_rdkit_result = pd.concat(rdkit_datasets.values(), axis=1)
    merged_rdkit_result.fillna(0, inplace=True)
    # 将合并后的结果保存为 CSV 文件
    merged_rdkit_result.to_csv(path + '/merged_rdkit_result.csv', index=False)

    # 打印或使用合并后的 RDKit 特征化结果
    print(merged_rdkit_result)

    unselected_columns = pd.DataFrame(pd.read_csv(path + '/unselected_columns.csv'))
    # 合并前重置索引
    merged_rdkit_result.reset_index(drop=True, inplace=True)
    unselected_columns.reset_index(drop=True, inplace=True)

    # 合并三个数据集
    all_merged_data = pd.concat([merged_rdkit_result, unselected_columns], axis=1)

    # 将合并后的结果保存为 CSV 文件
    all_merged_data.to_csv(path + '/train_test_Multicolumn_Smiles_dataset.csv', index=False)

    selected_columns = all_merged_data.loc[:, s_rfe.columns]
    selected_columns.to_csv(path+'/virtual_generate_Multicolumn_Smiles_RDKit_final.csv', index=False)

def virtual_Multicolumn_Smiles(path,csvpath):
    import pandas as pd
    def select_columns_by_suffix(df, suffix):
        filtered_columns = df.filter(regex=f'{suffix}$')
        return filtered_columns

    def extract_and_store_columns(csv_file, suffixes):
        # 读取 CSV 文件
        df = pd.read_csv(csv_file)

        selected_columns = {}
        for suffix in suffixes:
            selected_columns[suffix] = select_columns_by_suffix(df, suffix)
            print('********************************************************************************')
            print(f"Columns ending with '{suffix}':")
            print('********************************************************************************')
            print(selected_columns[suffix])
            # 如果需要保存到新的DataFrame中，取消注释下一行
            # global df_selected
            df_selected = pd.concat(selected_columns, axis=1)
            # df_combined = pd.concat(selected_columns.values(), axis=1)
            # df_combined.to_csv('selected_columns.csv', index=False)
            selected_columns[suffix].to_csv(path + '/' + f'{suffix}_selected_columns.csv', index=False)

        # 获取未被选中的列
        unselected_columns = df.drop(columns=[col for cols in selected_columns.values() for col in cols.columns])

        # 保存未被选中的列到 CSV 文件
        unselected_columns.to_csv(path + '/' + 'unselected_columns.csv', index=False)

        return selected_columns

    # 用法示例
    file_path = csvpath
    suffixes = ['Smiles']
    selected_columns = extract_and_store_columns(file_path, suffixes)

    original_data = pd.DataFrame(pd.read_csv(path + '/Smiles_selected_columns.csv'))

    import pandas as pd

    # 假设 original_data 是您的原始数据集
    # 创建一个空字典，用于存储新的数据集
    new_datasets = {}

    # 遍历原始数据集的每一列
    for col_name in original_data.columns:
        # 创建新的数据集，将当前列命名为 'Name'
        new_dataset = pd.DataFrame({'Name': original_data[col_name]})

        # 将新数据集存储在字典中，字典的键是 'data1'，'data2'，依此类推
        new_datasets['data' + str(len(new_datasets) + 1)] = new_dataset

    # 打印或使用新的数据集
    for key, value in new_datasets.items():
        print(f"{key}:\n{value}\n")


    # 有机部分
    original_data2 = pd.DataFrame(pd.read_csv(path + '/Smiles_selected_columns.csv'))

    new_datasets2 = {}

    # 遍历原始数据集的每一列
    for col_name in original_data2.columns:
        # 创建新的数据集，将当前列命名为 'Name'
        new_dataset2 = pd.DataFrame({'Name': original_data2[col_name]})

        # 将新数据集存储在字典中，字典的键是 'organic_data1'，'organic_data2'，依此类推
        new_datasets2['organic_data' + str(len(new_datasets2) + 1)] = new_dataset2

    # 打印或使用新的数据集
    for key, value in new_datasets2.items():
        print(f"{key}:\n{value}\n")

    import pandas as pd
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem

    # 假设 new_datasets2 是包含拆分数据集的字典，如 'organic_data1', 'organic_data2', ...
    # 每个数据集中应该有 'Name' 列

    # 用于存储 RDKit 特征化后的数据集
    rdkit_datasets = {}

    # 遍历拆分的数据集
    for key, dataset in new_datasets2.items():
        # 特征化 RDKit
        rdkit_features = dataset['Name'].apply(
            lambda x: AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(x), 2))

        # 将 RDKit 指纹转换为 DataFrame
        rdkit_features_df = pd.DataFrame(
            list(rdkit_features.apply(lambda x: np.frombuffer(x.ToBinary(), dtype=np.uint8))))

        # 添加前缀
        prefix_rdkit = f'{key}_rdkit_'
        rdkit_features_df = rdkit_features_df.add_prefix(prefix_rdkit)

        # 存储特征化后的数据集
        rdkit_datasets[key] = rdkit_features_df

    # 合并 RDKit 特征化后的数据集
    merged_rdkit_result = pd.concat(rdkit_datasets.values(), axis=1)
    merged_rdkit_result.fillna(0, inplace=True)
    # 将合并后的结果保存为 CSV 文件
    merged_rdkit_result.to_csv(path + '/merged_rdkit_result.csv', index=False)

    # 打印或使用合并后的 RDKit 特征化结果
    print(merged_rdkit_result)

    unselected_columns = pd.DataFrame(pd.read_csv(path + '/unselected_columns.csv'))
    # 合并前重置索引
    merged_rdkit_result.reset_index(drop=True, inplace=True)
    unselected_columns.reset_index(drop=True, inplace=True)

    # 合并三个数据集
    all_merged_data = pd.concat([merged_rdkit_result, unselected_columns], axis=1)

    # 将合并后的结果保存为 CSV 文件
    all_merged_data.to_csv(path + '/train_test_Multicolumn_Smiles_dataset.csv', index=False)

    selected_columns = all_merged_data.loc[:, s_rfe.columns]
    selected_columns.to_csv(path+'/virtual_generate_Multicolumn_Smiles_final.csv', index=False)


# 11 基于给定模型预测
def model_modify_predict(csvName,path,model_path):
    """import pandas as pd
    Predict_features = pd.DataFrame(pd.read_csv(csvName))
    featureData1 = Predict_features.values[:, :]
    # StandardScaler.fit(featureData1)
    # featureData2 = StandardScaler.transform(featureData1)
    # print(featureData2)
    predict = clf_xgboost_modify.predict(featureData1)
    predict_Ef = pd.DataFrame(predict)
    predict_Ef.to_csv(path + "/Predict_xgboost_dataset_modify.csv")"""

    import pickle
    import os
    import pandas as pd
    import numpy as np
    import csv
    from sklearn import preprocessing
    loaded_model = pickle.load(open(model_path, "rb"))
    data = pd.DataFrame(pd.read_csv(csvName))
    X = pd.DataFrame(pd.read_csv(csvName)).values[:, :]

    # 特征缩放，映射到0和1之间的范围
    for i in range(X.shape[1]):
        X[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X[:, [i]])
    target = loaded_model.predict(X)
    print(loaded_model.predict(X))
    file_name = "prediction_output("+os.path.basename(model_path)[:-4]+").csv"

    tg = pd.DataFrame(target,columns=["Output"])

    prediction = pd.concat([data, tg], axis=1)
    prediction.to_csv(path +"/"+ file_name,index=None)
    return path +"/"+ file_name

def model_modify_predict_deep(csvName, path, model_path):
    import os
    import pandas as pd
    from tensorflow.keras.models import load_model
    from sklearn import preprocessing

    # 加载模型
    loaded_model = load_model(model_path)
    data = pd.read_csv(csvName)
    X = data.values[:, :]

    for i in range(X.shape[1]):
        X[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X[:, [i]])

    # 预测
    target = loaded_model.predict(X)
    print(target)
    target_classes = (target >= 0.5).astype(int)
    file_name = "prediction_output(" + os.path.basename(model_path)[:-3] + ").csv"
    tg = pd.DataFrame(target_classes, columns=["Output"])

    # 将预测结果附加到原始数据
    prediction = pd.concat([data, tg], axis=1)
    prediction.to_csv(path +"/"+ file_name,index=None)
    return path +"/"+ file_name





def xgboost_default_predict(csvName,path):
    import pandas as pd
    Predict_features = pd.DataFrame(pd.read_csv(csvName))

    predict_Ef = pd.DataFrame(predict)
    predict_Ef.to_csv(path + "/Predict_xgboost_dataset.csv")



def xgboost_modify_predict(csvName,path):

    import pandas as pd
    import numpy as np
    import csv
    from sklearn import preprocessing
    loaded_model = pickle.load(open("Continuous_Xgboost.dat", "rb"))
    data = pd.DataFrame(pd.read_csv(csvName))
    X = data.values[:, :]
    for i in range(X.shape[1]):
        X[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X[:, [i]])
    target = loaded_model.predict(X)
    print(loaded_model.predict(X))



def rnd_search_cv_xgboost_predict(csvName,path):
    # 数据切分
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split

    X = s_rfe
    y = target
    X = X.values[:, :]
    y = y.values[:, :]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])
    for i in range(X_test.shape[1]):

    import pandas as pd
    x_New = pd.read_csv(csvName)
    print("new features dataset: ", x_New)

    y_New_prediction = rnd_search_cv_xgboost.predict(x_New)
    y_New_prediction = pd.DataFrame(y_New_prediction)
    y_New_prediction.columns = ['Output']
    print("new output: ", y_New_prediction)
    NewData = pd.concat([x_New, y_New_prediction], axis=1)
    print("New total Data: ", NewData)
    NewData.to_csv(path+"/New_prediction_total_rnd_search_cv_xgboost.csv")

    return x_New,y_New_prediction, NewData


def randomforest_default_predict(csvName,path):
    import pandas as pd
    Predict_features = pd.DataFrame(pd.read_csv(csvName))
    featureData1 = Predict_features.values[:, :]
    # StandardScaler.fit(featureData1)
    # featureData2 = StandardScaler.transform(featureData1)
    # print(featureData2)
    predict = clf_rf_default.predict(featureData1)
    predict_Ef = pd.DataFrame(predict)
    predict_Ef.to_csv(path + "/Predict_rf_dataset.csv")






def gp_default(r_thresh):  ## 输入参数为皮尔森阈值 ：例如输入0.6后，大于0.6的才显示
    import numpy as np
    from sklearn import preprocessing
    from gplearn import genetic
    X = data.values[:,:-1]
    y = data.values[:,-1]
    for i in range(X.shape[1]):
        X[:,[i]] = preprocessing.MinMaxScaler().fit_transform(X[:,[i]])
    est_gp = genetic.SymbolicTransformer(population_size=1000,
                               generations=91, stopping_criteria=0.01,
                               p_crossover=0.8, p_subtree_mutation=0.05,
                               p_hoist_mutation=0.05, p_point_mutation=0.05,
                               max_samples=0.9, verbose=1,
                               parsimony_coefficient=0.01, random_state=None,n_components=100)
    V=est_gp.fit(X, y)
    px=V.transform(X)
    str1=""
    for i in range(0,50):
        pear=np.corrcoef(px[:,i], y)
        pea=pear[0,1]
        if pea>r_thresh:
            print(pea,i,V[i])
            str1=str1+str(pea)+"  "+str(i)+"  "+str(V[i])+"\n"
    print('\n***************************')
    for i in range(len(data.columns.values.tolist())):
        print(i, data.columns.values.tolist()[i])
    return str1,data

## 9.2 更多运算符
def gp_tan(r_thresh):
    import numpy as np
    from sklearn import preprocessing
    from gplearn import genetic
    X = data.values[:, :-1]
    y = data.values[:, -1]
    for i in range(X.shape[1]):
        X[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X[:, [i]])
    function_set = ['add', 'sub', 'mul', 'div', 'log', 'sqrt', 'abs', 'neg','inv','sin','cos','tan', 'max', 'min']
    est_gp = genetic.SymbolicTransformer(population_size=1000,
                               generations=91, stopping_criteria=0.01,
                               p_crossover=0.8, p_subtree_mutation=0.05,
                               p_hoist_mutation=0.05, p_point_mutation=0.05,
                               max_samples=0.9, verbose=1,function_set=function_set,
                               parsimony_coefficient=0.01, random_state=None,n_components=100)
    V=est_gp.fit(X, y)
    px=V.transform(X)
    str1 = ""
    for i in range(0,50):
        pear=np.corrcoef(px[:,i], y)
        pea=pear[0,1]
        if pea>r_thresh:
            print(pea,i,V[i])
            str1 = str1 + str(pea) + "  " + str(i) + "  " + str(V[i]) + "\n"
    print('\n***************************')
    for i in range(len(data.columns.values.tolist())):
        print(i, data.columns.values.tolist()[i])
    return str1, data

## 9.3 tSR默认形式为(X[:,i]-X[:,j])*(X[:,k]-X[:,n])
def tSR_default(r_thresh,path):
    import numpy as np
    X = data_rfe.values[:, :-1]
    y = data_rfe.values[:, -1]
    for i in range(0,(data_rfe.shape[1]-1)):
         for j in range(0,(data_rfe.shape[1]-1)):
              for k in range(0,(data_rfe.shape[1]-1)):
                    for n in range(0,(data_rfe.shape[1]-1)):
                         px=(X[:,i]-X[:,j])*(X[:,k]-X[:,n])
                         per=np.corrcoef(px, y)
                         if per[0,1]>r_thresh or per[0,1]< -1 * r_thresh:
                              print(per[0,1])
                              print(i,j,k,n)
                              print(data_rfe.columns.values.tolist()[i],data_rfe.columns.values.tolist()[j],data_rfe.columns.values.tolist()[k],data_rfe.columns.values.tolist()[n])
                              print('(',data_rfe.columns.values.tolist()[i],'-',data_rfe.columns.values.tolist()[j],')','*','(',data_rfe.columns.values.tolist()[k],'-',data_rfe.columns.values.tolist()[n],')')
                              print('**********************************************')
                              with open(path+"/data.txt", "a+") as f:
                                  f.write(str(per[0,1])+"\n")
                                  f.write(str(i)+" "+str(j)+" "+str(k)+" "+str(n)+"\n")
                                  f.write(str(data_rfe.columns.values.tolist()[i])+" "
                                          +str(data_rfe.columns.values.tolist()[j])+" "
                                          +str(data_rfe.columns.values.tolist()[k])+" "
                                          +str(data_rfe.columns.values.tolist()[n])+"\n")
                                  f.write("( "+str(data_rfe.columns.values.tolist()[i]) + " - "
                                          + str(data_rfe.columns.values.tolist()[j]) + " ) * ("
                                          + str(data_rfe.columns.values.tolist()[k]) + " - "
                                          + str(data_rfe.columns.values.tolist()[n]) + " )\n")
                                  f.write('**********************************************\n')




def Symbolicregression_Modelconstruction(csvname,path):
    import pickle
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    import pickle
    from gplearn.genetic import SymbolicRegressor
    from sklearn.metrics import mean_squared_error
    import numpy as np
    from sklearn.tree import export_graphviz
    import pydotplus
    import graphviz
    from io import StringIO
    from IPython.display import Image


    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    feature_names = list(data.columns[:-1])


    reg = SymbolicRegressor(population_size=5000, generations=20, verbose=1,
                            function_set=['add', 'sub', 'mul', 'div', 'sqrt', 'log', 'abs', 'neg',
                                          'inv', 'max', 'min', 'sin', 'cos', 'tan'],
                            metric='mean absolute error', stopping_criteria=0.001,
                            random_state=0)

    Symbolic_Regression_Model=reg.fit(X_train, y_train)
    import pickle
    pickle.dump(Symbolic_Regression_Model, open(path + "/Symbolic_Regression_Model.dat", "wb"))

    from sklearn.metrics import mean_absolute_error
    y_pred = reg.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print("MAE:", mae)

    from sklearn.metrics import mean_squared_error, r2_score
    import numpy as np

    mse = mean_squared_error(y_test, y_pred)
    print("MSE:", mse)

    r2 = r2_score(y_test, y_pred)
    print("R2:", r2)

    corrcoef = np.corrcoef(y_test, y_pred)[0, 1]
    print("r (Pearson correlation):", corrcoef)


    import matplotlib.pyplot as plt






    plt.scatter(y_test, y_pred, alpha=0.5)

    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()

    plt.plot([x_min, x_max], [y_min, y_max], color='black', label='Diagonal')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel("True values")
    plt.ylabel("Predictions")
    plt.savefig(path + '/fitting.png', dpi=300, bbox_inches='tight')
    plt.close()

    plt.scatter(y_pred, y_test - y_pred, alpha=0.5)
    plt.hlines(y=0, xmin=x_min, xmax=x_max, colors='r', linestyles='--')
    plt.xlabel("Predictions")
    plt.ylabel("Residuals")
    plt.savefig(path + '/residue.png', dpi=300, bbox_inches='tight')
    plt.close()


    import graphviz
    dot_data = reg._program.export_graphviz()
    graph = graphviz.Source(dot_data)
    graph.render(path + '/tree', format="png")






def Symbolicclassification(csvname,path):
    import pickle
    import matplotlib.pyplot as plot
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import svm
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from pandas import DataFrame
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.svm import SVC
    from sklearn.model_selection import GridSearchCV
    import pickle
    from gplearn.genetic import SymbolicClassifier
    from sklearn.metrics import mean_squared_error
    import numpy as np
    from sklearn.tree import export_graphviz
    import pydotplus
    import graphviz
    from io import StringIO
    from IPython.display import Image

    data = pd.DataFrame(pd.read_csv(csvname))

    X = data.values[:, :-1]
    y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    for i in range(X_train.shape[1]):
        X_train[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_train[:, [i]])

    for i in range(X_test.shape[1]):
        X_test[:, [i]] = preprocessing.MinMaxScaler().fit_transform(X_test[:, [i]])

    # 创建符号分类器
    clf = SymbolicClassifier(population_size=5000, generations=20, tournament_size=20,
                             function_set=['add', 'sub', 'mul', 'div', 'sqrt', 'log', 'abs', 'neg',
                                           'inv', 'max', 'min', 'sin', 'cos', 'tan'],
                             stopping_criteria=0.0, const_range=(-1.0, 1.0), verbose=1)
    clf.fit(X_train, y_train)
    Symbolic_Classification_Model = clf.fit(X_train, y_train)
    import pickle
    pickle.dump(Symbolic_Classification_Model, open(path + "/Symbolic_classification_Model.dat", "wb"))

    print(set(str(clf._program).split()))

    from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
    import matplotlib.pyplot as plt

    # Prediction on test set
    y_pred = clf.predict(X_test)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    plt.imshow(cm, cmap="coolwarm")
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.xticks(np.arange(len(set(y))), set(y))
    plt.yticks(np.arange(len(set(y))), set(y))

    # Adding text to the confusion matrix cells with larger font size
    for i in range(len(set(y))):
        for j in range(len(set(y))):
            plt.text(j, i, cm[i, j], ha='center', va='center', color='black', fontsize=14)
    plt.savefig(path + '/test_confusion.png', dpi=300, bbox_inches='tight')
    plt.close()

    from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
    import matplotlib.pyplot as plt

    # Prediction on test set
    y_pred = clf.predict(X_train)

    # Confusion matrix
    cm = confusion_matrix(y_train, y_pred)
    print("Confusion Matrix:")
    print(cm)

    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.xticks(np.arange(len(set(y))), set(y))
    plt.yticks(np.arange(len(set(y))), set(y))

    # Adding text to the confusion matrix cells with larger font size
    for i in range(len(set(y))):
        for j in range(len(set(y))):
            plt.text(j, i, cm[i, j], ha='center', va='center', color='red', fontsize=14)
    plt.savefig(path + '/train_confusion.png', dpi=300, bbox_inches='tight')
    plt.close()

    # ROC Curve
    y_probs = clf.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_probs)

    # Plotting ROC Curve
    plt.plot(fpr, tpr, label='ROC Curve')
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.savefig(path + '/test_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Accuracy
    accuracy = clf.score(X_test, y_test)
    print("Accuracy:", accuracy)

    # ROC Curve
    y_probs = clf.predict_proba(X_train)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_train, y_probs)

    # Plotting ROC Curve
    plt.plot(fpr, tpr, label='ROC Curve')
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.savefig(path + '/train_ROC.png', dpi=300, bbox_inches='tight')
    plt.close()


    from sklearn.tree import export_graphviz
    from io import StringIO
    from IPython.display import Image
    import graphviz
    dot_data = clf._program.export_graphviz()
    graph = graphviz.Source(dot_data)
    graph.render(path + '/tree', format="png")



# shap 回归，导入和出结果
def Result_regression(csvname,path,model_path):


    shap.summary_plot(shap_values.values[:, :], X, show=False, plot_type='dot')
    plt.tight_layout()
    plt.subplots_adjust(left=0.1, right=0.9)

    plt.savefig(path+'/summary_plot.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()




    shap.force_plot(explainer.expected_value, shap_values.values[0, :], X.iloc[0, :],
                    matplotlib=True, show=False)
    plt.tight_layout()

    plt.savefig(path+'/Forceplot.png', bbox_inches='tight', dpi=300)
    plt.close()

    import seaborn as sns



    plt.figure(figsize=(10, 6))
    sns.barplot(x=shap_mean_sorted.values, y=shap_mean_sorted.index)
    plt.xlabel('Mean |SHAP| value', fontsize=13)
    plt.title('Feature Importance Rankings', fontsize=16)
    plt.savefig(path+'/Feature_ranking_bar.png', bbox_inches='tight', dpi=300)
    plt.close()


def Result_classification(csvname,path,model_path):
    import pandas as pd
    import matplotlib.pyplot as plt
    import shap
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import ExtraTreesClassifier
    import pickle
    import numpy as np

    np.bool = np.bool_

    data = pd.read_csv(csvname)

    import pickle

    model1 = pickle.load(open(model_path, "rb"))


    X = data.iloc[:, :-1]

    y = data.iloc[:, -1]


    explainer = shap.Explainer(model1, X)


    shap_values = explainer(X)


    shap_df = pd.DataFrame(shap_values.values[:, :, 1], columns=X.columns)









def plot_word_vectors_tsne(model, highlight_words_blue, highlight_words_red, highlight_words_yellow,highlight_words_green, highlight_words_orange,path):
    import logging
    import gensim
    from gensim.models import word2vec, KeyedVectors
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.decomposition import PCA
    import numpy as np
    import itertools
    from gensim.models import KeyedVectors
    from gensim.models import Word2Vec
    from gensim.models.word2vec import LineSentence
    from sklearn.manifold import TSNE
    # model1 = pickle.load(open(model_path, "rb")
    # ------------------------------------------------global model--------------------
    global model_NLP
    model_NLP =model
    global word_vectors_tsne



    # -----------------------------------------------------
    # model = KeyedVectors.load_word2vec_format(open(model_path))
    # model_path=
    # loaded_model =KeyedVectors.load.word2vec_format(model_path)
    word_vectors = model.vectors
    tsne = TSNE(n_components=2, random_state=42)
    word_vectors_tsne = tsne.fit_transform(word_vectors)

    word_vectors_dict = {}
    for i, word in enumerate(model.index_to_key):
        word_vectors_dict[word] = model.get_vector(word)

    plt.figure(figsize=(12, 8))
    dpi = 2000
    plt.scatter(word_vectors_tsne[:, 0], word_vectors_tsne[:, 1], color='lightgray')


    for word in highlight_words_blue:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='blue')
            # plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_red:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='red')
            # plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_yellow:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='yellow')
            # plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_green:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='green')
            # plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_orange:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='orange')
            # plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_blue:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='blue')
            plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_red:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='red')
            plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_yellow:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='yellow')
            plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)

    for word in highlight_words_green:
        if word in word_vectors_dict:
            index = list(word_vectors_dict.keys()).index(word)
            plt.scatter(word_vectors_tsne[index, 0], word_vectors_tsne[index, 1], color='green')
            plt.annotate(word, (word_vectors_tsne[index, 0], word_vectors_tsne[index, 1]), fontsize=12)




def visualize_word_embeddings(path,words, word1, word2,word3,word4,word5):

    import matplotlib.pyplot as plt
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    from gensim.models import KeyedVectors
    from sklearn.manifold import TSNE
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    import matplotlib.pyplot as plt


    word_vectors = model_NLP.vectors

    words_set = model_NLP.index_to_key


    word_index = words_set.index(words[0])

    word1_index = words_set.index(word1[0])
    word2_index = words_set.index(word2[0])
    word3_index = words_set.index(word3[0])
    word4_index = words_set.index(word4[0])
    word5_index = words_set.index(word5[0])




    cosine_similarities = cosine_similarity(word_vectors, [word_vectors[word_index]])



    cmap = plt.cm.Blues



    # 可视化词向量图
    plt.figure(figsize=(10, 8))


    colors = plt.cm.Blues(cosine_similarities.ravel())
    plt.scatter(word_vectors_tsne[:, 0], word_vectors_tsne[:, 1], c=colors, alpha=0.5)


    plt.scatter(word_vectors_tsne[word1_index, 0], word_vectors_tsne[word1_index, 1], c='red', marker='*', s=100, label=word1)
    plt.scatter(word_vectors_tsne[word2_index, 0], word_vectors_tsne[word2_index, 1], c='green', marker='^', s=100, label=word2)
    plt.scatter(word_vectors_tsne[word3_index, 0], word_vectors_tsne[word3_index, 1], c='blue', marker='*', s=100, label=word3)
    plt.scatter(word_vectors_tsne[word4_index, 0], word_vectors_tsne[word4_index, 1], c='violet', marker='^', s=100, label=word4)
    plt.scatter(word_vectors_tsne[word5_index, 0], word_vectors_tsne[word5_index, 1], c='orange', marker='*', s=100, label=word5)





    plt.xlabel('t-SNE Dimension 1')
    plt.ylabel('t-SNE Dimension 2')
    plt.title('t-SNE Visualization of Word Embeddings with Cosine Similarity')
    plt.legend()


    #cbar = plt.colorbar()

    # 添加颜色条

    #cbar.set_label('Cosine Similarity')
    #cbar.set_ticks(np.linspace(0,1,6))
    #cbar.ax.tick_params(axis='y', colors='blue')
    plt.savefig(path + '/tsne_highlight.png')
    #plt.show()









def cosine_similarity_model(a,path):
    related_words = model_NLP.most_similar(a, topn=1000)  # 打印选择的向量名
    with open(path + '/cosine_similarity.csv', 'w', encoding='utf-8') as f:
        for word in related_words:
            f.write(f"{word[0]}, {word[1]}\n")
    #for word in related_words:
     #   print(word)




























