# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental_dp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x65xperimental_dp.proto\x12\x10smiles.model.exp\x1a\x1cgoogle/protobuf/struct.proto\"\xe7\x0f\n\x0e\x45xperimentalDP\x12\x17\n\x0f\x64\x61ta_product_id\x18\x01 \x01(\t\x12#\n\x16parent_data_product_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ndye_family\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tstructure\x18\x05 \x01(\x0cH\x03\x88\x01\x01\x12\x13\n\x0bother_names\x18\x06 \x03(\t\x12\x11\n\x04note\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06mol_id\x18\x08 \x01(\tH\x05\x88\x01\x01\x12\x13\n\x06\x63\x61s_nr\x18\t \x01(\tH\x06\x88\x01\x01\x12\x0f\n\x02mw\x18\n \x01(\x01H\x07\x88\x01\x01\x12\x16\n\tmw_source\x18\x0b \x01(\tH\x08\x88\x01\x01\x12\x17\n\nmw_monoiso\x18\x0c \x01(\x01H\t\x88\x01\x01\x12\x10\n\x03rdb\x18\r \x01(\x01H\n\x88\x01\x01\x12\x19\n\x0cvalidated_by\x18\x0e \x01(\tH\x0b\x88\x01\x01\x12\x14\n\x07journal\x18\x0f \x01(\tH\x0c\x88\x01\x01\x12\x19\n\x0c\x61uth_of_intr\x18\x10 \x01(\tH\r\x88\x01\x01\x12\x15\n\x08jour_cit\x18\x11 \x01(\tH\x0e\x88\x01\x01\x12\x16\n\tyear_publ\x18\x12 \x01(\x05H\x0f\x88\x01\x01\x12\x15\n\x08\x64oi_link\x18\x13 \x01(\tH\x10\x88\x01\x01\x12\x17\n\ncomp_class\x18\x14 \x01(\tH\x11\x88\x01\x01\x12\x12\n\x05\x63uniq\x18\x15 \x01(\tH\x12\x88\x01\x01\x12\x16\n\tcalc_perf\x18\x16 \x01(\x08H\x13\x88\x01\x01\x12\x14\n\x07org_met\x18\x17 \x01(\tH\x14\x88\x01\x01\x12\x15\n\x08mol_chrg\x18\x18 \x01(\x03H\x15\x88\x01\x01\x12\x18\n\x0binter_thngs\x18\x19 \x01(\tH\x16\x88\x01\x01\x12>\n\x0fstructural_data\x18\x1a \x01(\x0b\x32 .smiles.model.exp.StructuralDataH\x17\x88\x01\x01\x12:\n\rspectral_data\x18\x1b \x01(\x0b\x32\x1e.smiles.model.exp.SpectralDataH\x18\x88\x01\x01\x12@\n\x10\x65lectro_chemical\x18\x1c \x01(\x0b\x32!.smiles.model.exp.ElectroChemicalH\x19\x88\x01\x01\x12\x17\n\x0frelated_records\x18\x1d \x03(\t\x12\x18\n\ndensity_20\x18\xa1\x07 \x01(\x01H\x1a\x88\x01\x01\x12\x1f\n\x11\x64\x65nsity_20_source\x18\xa2\x07 \x01(\tH\x1b\x88\x01\x01\x12 \n\x12\x64\x65\x66\x61ult_warn_level\x18\xa3\x07 \x01(\x01H\x1c\x88\x01\x01\x12\x12\n\x04n_20\x18\xa4\x07 \x01(\x01H\x1d\x88\x01\x01\x12\x19\n\x0bn_20_source\x18\xa5\x07 \x01(\tH\x1e\x88\x01\x01\x12\x14\n\x06mp_low\x18\xa6\x07 \x01(\x01H\x1f\x88\x01\x01\x12\x15\n\x07mp_high\x18\xa7\x07 \x01(\x01H \x88\x01\x01\x12\x17\n\tmp_source\x18\xa8\x07 \x01(\tH!\x88\x01\x01\x12\x14\n\x06\x62p_low\x18\xa9\x07 \x01(\x01H\"\x88\x01\x01\x12\x15\n\x07\x62p_high\x18\xaa\x07 \x01(\x01H#\x88\x01\x01\x12\x16\n\x08\x62p_press\x18\xab\x07 \x01(\x01H$\x88\x01\x01\x12\x18\n\npress_unit\x18\xac\x07 \x01(\tH%\x88\x01\x01\x12\x17\n\tbp_source\x18\xad\x07 \x01(\tH&\x88\x01\x01\x12\x16\n\x08safety_r\x18\xae\x07 \x01(\tH\'\x88\x01\x01\x12\x16\n\x08safety_h\x18\xaf\x07 \x01(\tH(\x88\x01\x01\x12\x16\n\x08safety_s\x18\xb0\x07 \x01(\tH)\x88\x01\x01\x12\x16\n\x08safety_p\x18\xb1\x07 \x01(\tH*\x88\x01\x01\x12\x19\n\x0bsafety_text\x18\xb2\x07 \x01(\tH+\x88\x01\x01\x12\x18\n\nsafety_sym\x18\xb3\x07 \x01(\tH,\x88\x01\x01\x12\x1c\n\x0esafety_sym_ghs\x18\xb4\x07 \x01(\tH-\x88\x01\x01\x12\x1b\n\rsafety_source\x18\xb5\x07 \x01(\tH.\x88\x01\x01\x42\x19\n\x17_parent_data_product_idB\x07\n\x05_nameB\r\n\x0b_dye_familyB\x0c\n\n_structureB\x07\n\x05_noteB\t\n\x07_mol_idB\t\n\x07_cas_nrB\x05\n\x03_mwB\x0c\n\n_mw_sourceB\r\n\x0b_mw_monoisoB\x06\n\x04_rdbB\x0f\n\r_validated_byB\n\n\x08_journalB\x0f\n\r_auth_of_intrB\x0b\n\t_jour_citB\x0c\n\n_year_publB\x0b\n\t_doi_linkB\r\n\x0b_comp_classB\x08\n\x06_cuniqB\x0c\n\n_calc_perfB\n\n\x08_org_metB\x0b\n\t_mol_chrgB\x0e\n\x0c_inter_thngsB\x12\n\x10_structural_dataB\x10\n\x0e_spectral_dataB\x13\n\x11_electro_chemicalB\r\n\x0b_density_20B\x14\n\x12_density_20_sourceB\x15\n\x13_default_warn_levelB\x07\n\x05_n_20B\x0e\n\x0c_n_20_sourceB\t\n\x07_mp_lowB\n\n\x08_mp_highB\x0c\n\n_mp_sourceB\t\n\x07_bp_lowB\n\n\x08_bp_highB\x0b\n\t_bp_pressB\r\n\x0b_press_unitB\x0c\n\n_bp_sourceB\x0b\n\t_safety_rB\x0b\n\t_safety_hB\x0b\n\t_safety_sB\x0b\n\t_safety_pB\x0e\n\x0c_safety_textB\r\n\x0b_safety_symB\x11\n\x0f_safety_sym_ghsB\x10\n\x0e_safety_source\"\xcd\x02\n\x0f\x45lectroChemical\x12\x14\n\x07temp_cv\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x16\n\treduc_pot\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x18\n\x0bhw_or_pk_rp\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08oxid_pot\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x18\n\x0bhw_or_pk_op\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x17\n\nsolvent_cv\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x18\n\x0b\x65lectrolyte\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x18\n\x0bref_electrd\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\n\n\x08_temp_cvB\x0c\n\n_reduc_potB\x0e\n\x0c_hw_or_pk_rpB\x0b\n\t_oxid_potB\x0e\n\x0c_hw_or_pk_opB\r\n\x0b_solvent_cvB\x0e\n\x0c_electrolyteB\x0e\n\x0c_ref_electrd\"\xe4\x03\n\x0cSpectralData\x12\x18\n\x0bstate_ofmat\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x63olor_white\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08\x63olor_uv\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nabsorb_max\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x17\n\nsolvent_ae\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06\x61\x62sorb\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12\x11\n\x04\x63onc\x18\x07 \x01(\x01H\x06\x88\x01\x01\x12\x13\n\x06\x65xtinc\x18\x08 \x01(\x01H\x07\x88\x01\x01\x12\x15\n\x08\x65mis_max\x18\t \x01(\x01H\x08\x88\x01\x01\x12\x15\n\x08temp_abs\x18\n \x01(\x01H\t\x88\x01\x01\x12\x14\n\x07\x65mis_qy\x18\x0b \x01(\x01H\n\x88\x01\x01\x12\x15\n\x08temp_ems\x18\x0c \x01(\x01H\x0b\x88\x01\x01\x12\x15\n\x08lifetime\x18\r \x01(\x01H\x0c\x88\x01\x01\x42\x0e\n\x0c_state_ofmatB\x0e\n\x0c_color_whiteB\x0b\n\t_color_uvB\r\n\x0b_absorb_maxB\r\n\x0b_solvent_aeB\t\n\x07_absorbB\x07\n\x05_concB\t\n\x07_extincB\x0b\n\t_emis_maxB\x0b\n\t_temp_absB\n\n\x08_emis_qyB\x0b\n\t_temp_emsB\x0b\n\t_lifetime\"\xe4\x02\n\x0eStructuralData\x12\x13\n\x06smiles\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rsmiles_stereo\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05inchi\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x38\n\x13molfile_blob_source\x18\x04 \x01(\x0b\x32\x16.google.protobuf.ValueH\x03\x88\x01\x01\x12\x18\n\x0b\x65mp_formula\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1d\n\x10\x65mp_formula_sort\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x1f\n\x12\x65mp_formula_source\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\t\n\x07_smilesB\x10\n\x0e_smiles_stereoB\x08\n\x06_inchiB\x16\n\x14_molfile_blob_sourceB\x0e\n\x0c_emp_formulaB\x13\n\x11_emp_formula_sortB\x15\n\x13_emp_formula_sourceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental_dp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXPERIMENTALDP._serialized_start=74
  _EXPERIMENTALDP._serialized_end=2097
  _ELECTROCHEMICAL._serialized_start=2100
  _ELECTROCHEMICAL._serialized_end=2433
  _SPECTRALDATA._serialized_start=2436
  _SPECTRALDATA._serialized_end=2920
  _STRUCTURALDATA._serialized_start=2923
  _STRUCTURALDATA._serialized_end=3279
# @@protoc_insertion_point(module_scope)
